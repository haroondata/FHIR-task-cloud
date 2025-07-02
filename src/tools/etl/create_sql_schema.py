# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 18:01:54 2025

@author: Haroon
"""
import os 
import pandas as pd
import logging
from src.tools.utils.helper_function_cleaning_df import clean_fhir_column_names
from src.tools.utils.df_preprocessor import df_processor
from src.tools.etl.generate_sql_create_queries import generate_mysql_create_table_query
from src.tools.db.execute_create_table_sql import  execute_create_table_sql_queries,create_audit_log_table
from src.tools.db.update_table_with_new_column import  sync_table_schema

logger = logging.getLogger("pipeline")

def write_sql_create_table_statements(mysql_engine,mysql_connection,resource_map):
    """
    
    This function will loop through resource map normalise the records
    Clean the header of the dataframe
    
    Returns
    -------
    None.

    """
    #create log table
    create_audit_log_table(mysql_connection)
    sql_dir = "./sql_tables"
    os.makedirs(sql_dir, exist_ok=True)
    
    for resource_type, records in resource_map.items():
        
        # Normalize the records: ensure all columns are included
        df_list = [pd.json_normalize(record) for record in records]
        if not df_list:
            continue

        # Combine all into one unified DataFrame
        df = pd.concat(df_list, ignore_index=True).fillna(pd.NA)
        # Clean columns names
        df = clean_fhir_column_names(df)
        
        # Proecess df adding addtional columns and creating patient id3
        df = df_processor(df)
        
        # Check if the dataframe is empty
        if not df.empty:
            # Get the table name in lower case
            table_name = resource_type.lower()
            
            # Function to get the create statement by the resource
            sql_code = generate_mysql_create_table_query(df, table_name)
            
            #Execute the create statement
            execute_create_table_sql_queries(mysql_connection,sql_code)
            
            # Save to file
            sql_path = os.path.join(sql_dir, f"{table_name}.sql")
          
            with open(sql_path, "w", encoding="utf-8") as f:
                f.write(sql_code)
            
    
            logger.info(f"Saved SQL DDL to {sql_path}")
    
    # if any new keys are in the JSON the table will be update with the column
    sync_table_schema(mysql_engine,mysql_connection, df, table_name)