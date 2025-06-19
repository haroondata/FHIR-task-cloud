# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:44:26 2024

@author: Haroon
"""

from src.tools.read_json_data import get_username,get_data_from_json,write_sql_create_table_statements,create_csv_files_and_insert_data_into_mysql_db


if __name__ == '__main__':


   username = get_username()
   resource_map = get_data_from_json(username)
   write_sql_create_table_statements(resource_map)
   create_csv_files_and_insert_data_into_mysql_db(resource_map)
    
