# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 18:04:16 2025

@author: Haroon
"""


def generate_mysql_create_table_query(df, table_name):
    """
    Generate the create statements based on the Dataframe 

    Parameters
    ----------
    df : DataFrame
        df of the resources.
    table_name : String
        Name of the table that will be created.

    Returns
    -------
    sql_code
        This will return the sql_code for creating the tables by resource.

    """
    sql_types = {
        'int64': 'BIGINT',
        'float64': 'FLOAT',
        'object': 'VARCHAR(255)',
        'bool': 'BOOLEAN',
        'datetime64[ns]': 'DATETIME'
    }
    
    # Lines list  which will append each column with the datatype
    lines = [f"CREATE TABLE IF NOT EXISTS `{table_name}` ("]
    
    # List to append  
    col_defs = []
    for col in df.columns:
        # Replace spaces and dots with underscores
        col_name = col.replace(" ", "_").replace(".", "_").lower()
        try:
            # Get data type of column
            dtype = str(df[col].dtype)
        except Exception as e:
            print(f"Error getting dtype for column '{col}': {e}")
           
        # If the dtype is not found it will default to VARCHAR(255)
        sql_type = sql_types.get(dtype, 'VARCHAR(255)')
        
        # Append line for each datatype in SQL
        col_defs.append(f"  `{col_name}` {sql_type} DEFAULT NULL")

    #  Join columns with commas, and ensure no trailing comma
    lines.append(",\n".join(col_defs))

    lines.append(") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;")
    
    return "\n".join(lines)