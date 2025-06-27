# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 12:00:00 2025

@author: Haroon
"""

from sqlalchemy import text
from sqlalchemy.exc import OperationalError
import time
import logging

max_retries = 3

def insert_data_into_mysql(mysql_engine, mysql_connection, df, table_name, source_file=None):
    """
        Insert DataFrame into MySQL table, delete existing data, insert new data, and verify count.
    
        Parameters
        ----------
        mysql_engine : TYPE
            DESCRIPTION.
        mysql_connection : TYPE
            DESCRIPTION.
        df : TYPE
            DESCRIPTION.
        table_name : TYPE
            DESCRIPTION.
        source_file : TYPE, optional
            DESCRIPTION. The default is None.
    
        Returns
        -------
        None.

    """
    row_count = len(df)
    logging.info(f"Inserting {row_count} rows into table `{table_name}`")

    for attempt in range(max_retries):
        try:
        
            # Insert df to sql database table
            df.to_sql(table_name, con=mysql_engine, if_exists="append", index=False)
            logging.info(f"Inserted {row_count} rows into `{table_name}`.")

            # Verify the count of inserted rows
            with mysql_engine.connect() as connection:
                result = connection.execute(text(f"SELECT COUNT(*) FROM `{table_name}`"))
                db_row_count = result.scalar()  # .scalar() gets first column of first row

            if db_row_count != row_count:
                logging.warning(
                    f"[{source_file}] MISMATCH in `{table_name}`: expected {row_count}, found {db_row_count}"
                )
            else:
                logging.info(
                    f"[{source_file}] Verified row count for `{table_name}`: {db_row_count} rows."
                )

            break  # Exit loop after success

        except OperationalError as e:
            logging.error(f"OperationalError (attempt {attempt + 1}/{max_retries}): {e}")
            if "Lock wait timeout" in str(e) and attempt < max_retries - 1:
                time.sleep(2)
            else:
                break

        except Exception as e:
            logging.error(f"Failed to insert into `{table_name}` from {source_file}: {e}")
            break
