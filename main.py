# -*- coding: utf-8 -*-
"""
Main entry point for the FHIR JSON to MySQL pipeline.
Created on Sun Jun 23 17:44:26 2024

@author: Haroon
"""

from src.tools.etl.read_json_data import get_data_from_json
from src.tools.etl.create_sql_schema import write_sql_create_table_statements
from src.tools.etl.prepare_and_load_to_mysql import insert_data_into_mysql_db
from src.tools import logger  # This runs the setup
import logging
from src.tools.db.mysql_connection import  mysql_connection
from src.tools.logger import setup_logger

logger = setup_logger()

logger.info("Starting the data pipeline.")
mysql_engine,mysql_connection =  mysql_connection()
logging.info(type(mysql_engine))
logging.info(type(mysql_connection))

def main():
   
   try:
      
       
       # Read and parse Json files into resource maps
       resource_map, file_tracking_map = get_data_from_json()
       logger.info(f"Extracted resources: {list(resource_map.keys())}")
       
       # Generate and execute SQL Table creation statements 
       write_sql_create_table_statements(mysql_engine,mysql_connection,resource_map)
       
       # Insert data into mysql tables
       insert_data_into_mysql_db(mysql_engine,mysql_connection,resource_map, file_tracking_map)
     
   except Exception as e: 
       logger.exception(f"Pipelines execution failed:{e}")      
   
   
if __name__ == '__main__':
    main()
