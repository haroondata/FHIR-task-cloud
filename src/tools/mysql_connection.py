# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:50:52 2024

@author: Haroon
"""

from urllib.parse import quote_plus

import configparser
import sqlalchemy



# mysql connection
def mysql_connection():
    # Initialize the ConfigParser
    config = configparser.ConfigParser(interpolation=None)
    # Read the config
    config.read('C:/Users/Haroon/Documents/config/config.txt')
    
       
    #config to get the MYSQL info
    db_username = config.get('DEFAULT', 'username')
    db_password = quote_plus(config.get('DEFAULT', 'password'))
    db_host = config.get('DEFAULT', 'host')
    db_port = '3306'
    db_name = config.get('DEFAULT', 'database')
    
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