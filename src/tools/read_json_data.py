# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 18:51:37 2025

@author: Haroon
"""

import os
import json
import pandas as pd
from collections import defaultdict
#mysql connection 
from src.tools.insert_data_into_mysql import insert_data_into_mysql
import getpass

#mysql connection 
from src.tools.mysql_connection import  mysql_connection
from src.tools.sql_queries import create_table


check_stack = []
resource_type_list = []
#mysql connection
mysql_engine,mysql_connection =  mysql_connection()


def get_username():
    """
    

    Returns
    -------
    username : TYPE
        DESCRIPTION.

    """
    username = getpass.getuser()
    return username

def flatten_json(nested_json):
    """
    

    Parameters
    ----------
    nested_json : TYPE
        DESCRIPTION.

    Returns
    -------
    flat : TYPE
        DESCRIPTION.

    """
    flat = {}

    def recurse(obj, path=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_path = f"{path}.{key}" if path else key
                recurse(value, new_path)

        elif isinstance(obj, list):
            if all(isinstance(i, dict) for i in obj):
                # Store list of dicts as-is; will process separately
                flat[path] = obj
            else:
                for idx, item in enumerate(obj):
                    new_path = f"{path}.{idx}" if path else str(idx)
                    recurse(item, new_path)

        else:
            flat[path] = obj

    recurse(nested_json)
    return flat


def generate_mysql_create_table(df, table_name):
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


def get_data_from_json(username):
    """
    

    Returns
    -------
    None.

    """
    # === File Path ===
    data_dir = os.path.join("/app/data")

    
    resource_map = defaultdict(list)
    #mysql connection
    # === Loop over all JSON files ===
    for file in os.listdir(data_dir):
        if file.endswith(".json"):
            file_path = os.path.join(data_dir, file)
            print(file_path)
            with open(file_path, 'r', encoding='utf-8') as f:
                bundle = json.load(f)
    
            # === Flatten and group by resourceType ===
            entries = bundle.get('entry', [])
            for item in entries:
                resource = item.get('resource', {})
                resource_type = resource.get('resourceType', 'Unknown')
                flat = flatten_json(resource)
                resource_map[resource_type].append(flat)
    return resource_map
                



def clean_fhir_column_names(df):
    """
    

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.

    Returns
    -------
    df : TYPE
        DESCRIPTION.

    """
    df.columns = (
        df.columns
        .str.replace(r'\.', '_', regex=True)          # replace dots with underscores
        .str.replace(r'\W+', '_', regex=True)         # remove weird characters
        .str.strip('_')                               # trim leading/trailing underscores
        .str.lower()                                  # lowercase for uniformity
       )
    return df
 
def write_sql_create_table_statements(resource_map):
    """
    

    Returns
    -------
    None.

    """
    sql_dir = "./sql_tables"
    os.makedirs(sql_dir, exist_ok=True)
    
    for resource_type, records in resource_map.items():
        resource_type_list.append(resource_type)
        # Normalize the records: ensure all columns are included
        df_list = [pd.json_normalize(record) for record in records]
        if not df_list:
            continue

        # Combine all into one unified DataFrame
        df = pd.concat(df_list, ignore_index=True).fillna(pd.NA)
        df = clean_fhir_column_names(df)
        
        if not df.empty:
            table_name = resource_type.lower()
            sql_code = generate_mysql_create_table(df, table_name)
            create_table(mysql_connection,sql_code)
            # Save to file
            sql_path = os.path.join(sql_dir, f"{table_name}.sql")
            with open(sql_path, "w", encoding="utf-8") as f:
                f.write(sql_code)
            print(f"Saved SQL DDL to {sql_path}")

def create_csv_files_and_insert_data_into_mysql_db(resource_map):
    """
    

    Returns
    -------
    None.

    """
    # === Save each resourceType as its own CSV ===
    output_dir = "./output"
    os.makedirs(output_dir, exist_ok=True)
    for resource_type, records in resource_map.items():
        df = pd.DataFrame(records)
        df = clean_fhir_column_names(df)
        # Clean each DataFrame before inserting to SQL
        for col in df.columns:
            if df[col].apply(lambda x: isinstance(x, (list, dict))).any():
                df[col] = df[col].apply(json.dumps)
        csv_path = os.path.join(output_dir, f"{resource_type}_flat.csv")
        df.to_csv(csv_path, index=False)
        print(f"Saved {resource_type} records to {csv_path}")
        #insert data into mysql
        table_name = resource_type.lower()
        # insert data into mysql
        insert_data_into_mysql(mysql_engine,mysql_connection,df,table_name)
    check_if_connection_is_closed()
    
def check_if_connection_is_closed():  
    """
    

    Returns
    -------
    None.

    """
    #Check if connection is closed
    mysql_connection.close()
    if mysql_connection.closed:
          print("Connection is closed")
    else:
          print("Connection is open")

    