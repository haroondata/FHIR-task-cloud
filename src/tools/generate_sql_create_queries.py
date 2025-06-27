# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 18:04:16 2025

@author: Haroon
"""


def generate_mysql_create_table_query(df, table_name):
    """
    

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.
    table_name : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    sql_types = {
        'int64': 'BIGINT',
        'float64': 'FLOAT',
        'object': 'VARCHAR(255)',
        'bool': 'BOOLEAN',
        'datetime64[ns]': 'DATETIME'
    }

    lines = [f"CREATE TABLE IF NOT EXISTS `{table_name}` ("]
    
    col_defs = []
    for col in df.columns:
        col_name = col.replace(" ", "_").replace(".", "_").lower()
        try:
            dtype = str(df[col].dtype)
        except Exception as e:
            print(f"Error getting dtype for column '{col}': {e}")
            dtype = 'object'
        sql_type = sql_types.get(dtype, 'VARCHAR(255)')
        col_defs.append(f"  `{col_name}` {sql_type} DEFAULT NULL")

    #  Join columns with commas, and ensure no trailing comma
    lines.append(",\n".join(col_defs))

    lines.append(") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;")
    
    return "\n".join(lines)