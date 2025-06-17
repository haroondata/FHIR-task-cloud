# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:44:26 2024

@author: Haroon
"""
import configparser
import sqlalchemy

import urllib



def mssql_connection():
    # Initialize the ConfigParser
    config = configparser.ConfigParser(interpolation=None)
    # Read the config
    config.read('config.txt')
    
    username = config.get('DEFAULT', 'mssql_username')
    password = config.get('DEFAULT', 'mssql_password')
    server = config.get('DEFAULT', 'mssql_server')
    db_name = config.get('DEFAULT', 'mssql_db_name')
    # database = config.get('DEFAULT', 'dataclean_database')
    
    # # Create connections to the SQL db
    # # Adjust the parameters to connect to different SQL dbs
    # connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};'
    # connection_string += 'SERVER=' + server + ';'
    # connection_string += 'DATABASE=' + db_name + ';'
    # connection_string += 'UID=' + username + ';'
    # connection_string += 'PWD=' + password + ';'
    
    params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"
                                     "SERVER="+server+";"
                                     "DATABASE="+db_name+";"
                                     "UID="+username+";"
                                     "PWD="+password+";")
    
    engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
    
    try:
        connection = engine.connect()
        print("Connected to the MSSQL database.")
    except Exception as e:
        raise Exception("Connection failed:", e)
    return engine,connection