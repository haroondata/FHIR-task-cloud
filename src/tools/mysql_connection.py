# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:50:52 2024

@author: Haroon
"""

from urllib.parse import quote_plus
import os
import configparser
import sqlalchemy



# mysql connection
def mysql_connection():
  
    #config to get the MYSQL info
    db_username = os.getenv('DB_USER')
    print(db_username)
    db_password = quote_plus(os.getenv('DB_PASSWORD'))
    db_host     = os.getenv('DB_HOST')
    db_port     = os.getenv('DB_PORT', '3306')
    db_name     = os.getenv('DB_NAME')
    
    #-----Portal 4 Configurations whilst running in parallel-----#
    # Create the database URL
    database_url = f'mysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
    
    # Create the SQLAlchemy engine
    engine = sqlalchemy.create_engine(database_url)
       
    try:
        connection = engine.connect()
        print("Connected to the MYSQL database.")
    except Exception as e:
        raise Exception("Connection failed:", e)
    return engine,connection