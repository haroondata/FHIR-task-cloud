# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 12:00:00 2025

@author: Haroon
"""

from sqlalchemy import text
from sqlalchemy.exc import OperationalError
import time
import logging
from datetime import datetime
from uuid import uuid4


logger = logging.getLogger("pipeline")
max_retries = 3

def insert_data_into_mysql(mysql_engine, mysql_connection, df, table_name, source_file=None):
    """
        Insert DataFrame into MySQL table, delete existing data, insert new data, and verify count.
    
        Parameters
        ----------
        mysql_engine : sqlalchemy.engine.Engine
            SQLAlchemy engine object used to connect to the MySQL database.
        mysql_connection : sqlalchemy.engine.Connection
            Active database connection obtained from the SQLAlchemy engine.
        df : pandas.DataFrame
            The DataFrame containing the data to be inserted into the table.
        table_name : str
           Name of the target table in the database where data will be inserted.
        source_file : str, optional
            Name of the source file the data came from (used for logging or tracking). Default is None.
     
        Returns
        -------
        None.

    """
    batch_id = str(uuid4())
    row_count = len(df)
    logger.info(f"Inserting {row_count} rows into table `{table_name}`with batch_id={batch_id}")
    
    
    for attempt in range(max_retries):
        try:
        
            # Insert df to sql database table
            df.to_sql(table_name, con=mysql_engine, if_exists="append", index=False)
            logger.info(f"Inserted {row_count} rows into `{table_name}`.")

            # Verify the count of inserted rows
            with mysql_engine.connect() as connection:
                result = connection.execute(text(f"SELECT COUNT(*) FROM `{table_name}`"))
                db_row_count = result.scalar()  # .scalar() gets first column of first row
            
            if db_row_count < row_count:
                logger.warning(
                    f"[{source_file}] MISMATCH in `{table_name}`: expected {row_count}, found {db_row_count}"
                )
            else:
                logger.info(
                    f"[{source_file}] Verified row count for `{table_name}`: {db_row_count} rows."
                )

            break  # Exit loop after success

        except OperationalError as e:
            logger.error(f"OperationalError (attempt {attempt + 1}/{max_retries}): {e}")
            if "Lock wait timeout" in str(e) and attempt < max_retries - 1:
                time.sleep(2)
            else:
                break

        except Exception as e:
            logger.error(f"Failed to insert into `{table_name}` from {source_file}: {e}")
            break




def log_file_load(mysql_connection, resource_type, row_count):
    """
    

    Parameters
    ----------
   mysql_connection : sqlalchemy.engine.Connection
    resource_type : String
        Resource type is the table name used for the tables.
    row_count : Count of rows
        Count of each batch of rows 

    Returns
    -------
    None.

    """
    sql = text("""
        INSERT INTO pipeline_audit_log (resource_type, inserted_rows, inserted_at)
        VALUES (:resource_type, :inserted_rows, :inserted_at)
    """)
    mysql_connection.execute(sql, {
        "resource_type": resource_type,
        "inserted_rows": row_count,
        "inserted_at": datetime.utcnow()
    })
    mysql_connection.commit()
