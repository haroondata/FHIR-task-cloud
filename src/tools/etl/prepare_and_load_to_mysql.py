# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 17:58:14 2025

@author: Haroon
"""
import os
import pandas as pd 

from src.tools.utils.helper_function_cleaning_df import clean_fhir_column_names
from src.tools.utils.df_preprocessor import df_processor
from src.tools.etl.creates_csv_file import create_csv_files
from src.tools.db.db_inserter import insert_data_into_mysql,log_file_load
from src.tools.db.check_connection import check_if_connection_is_closed




def insert_data_into_mysql_db(mysql_engine,mysql_connection,resource_map, file_tracking_map):
    """
    
    Dataframe will be store in the CSV and inserted into MySQL
    Returns
    -------
    None.

    """
    # Save each resourceType as its own CSV 
    output_dir = "./output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Loop through resourcemap
    for resource_type, records in resource_map.items():
   
        # Get records by resource
        df = pd.DataFrame(records)
        # Clean column names
        df = clean_fhir_column_names(df)
        
        # Process the Dataframe
        df = df_processor(df)
        
        create_csv_files(output_dir,resource_type,df)
        
        # Get the table name in lowercase
        table_name = resource_type.lower()
        
        
        source_file = file_tracking_map.get(resource_type, "Unknown")
        
        # Insert data into mysql
        insert_data_into_mysql(mysql_engine,mysql_connection,df,table_name,source_file=source_file)
        log_file_load(mysql_connection, resource_type, len(df))
    # Check if connection is closed
    check_if_connection_is_closed(mysql_connection)