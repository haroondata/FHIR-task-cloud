# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 23:35:10 2025

@author: Haroon
"""

from sqlalchemy import inspect
from sqlalchemy import text


def sync_table_schema(mysql_engine, mysql_connection, df, table_name):
    """
    
    Check if any new columns are need to be added to table 
    Parameters
    ----------
    mysql_engine : sqlalchemy.engine.Engine  
        SQLAlchemy engine object used for database operations.

    mysql_connection : sqlalchemy.engine.Connection  
        Active SQLAlchemy connection to the MySQL database.

    df : pandas.DataFrame  
        The DataFrame containing processed and cleaned FHIR resource data.

    table_name : str  
        Name of the MySQL table (typically derived from resource type, in lowercase).

    Returns
    -------
    None.

    """
    inspector = inspect(mysql_engine)
    existing_columns = [col['name'] for col in inspector.get_columns(table_name)]
    new_columns = [col for col in df.columns if col not in existing_columns]

    alter_statements = []
    for col in new_columns:
        dtype = str(df[col].dtype)
        sql_type = {
            'int64': 'BIGINT',
            'float64': 'FLOAT',
            'object': 'VARCHAR(255)',
            'bool': 'BOOLEAN',
            'datetime64[ns]': 'DATETIME'
        }.get(dtype, 'VARCHAR(255)')
        
        alter_statements.append(f"ADD COLUMN `{col}` {sql_type} DEFAULT NULL")

    if alter_statements:
        alter_sql = f"ALTER TABLE `{table_name}` " + ", ".join(alter_statements) + ";"
        with mysql_engine.connect() as mysql_connection:
            mysql_connection.execute(text(alter_sql))
        print(f"Updated schema for table `{table_name}`: Added {len(new_columns)} columns.")
    else:
        print(f"No schema change needed for `{table_name}`.")
