# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 12:00:00 2025

@author: Haroon
"""

from urllib.parse import quote_plus
import os
import sqlalchemy
import logging
import urllib.parse


logger = logging.getLogger("pipeline")


def mysql_connection():
    """
    Establishes a connection to a MySQL database using SQLAlchemy.
    
    Raises
    ------
    Exception: If connection fails.

    Returns
    -------
    engine (sqlalchemy.engine.Engine): SQLAlchemy engine object.
    connection (sqlalchemy.engine.Connection): Active DB connection.

    """
  
    #config to get the MYSQL info
    db_username = os.getenv('DB_USER')
    #db_password = quote_plus(os.getenv('DB_PASSWORD'))
    db_password = urllib.parse.quote_plus(os.getenv('DB_PASSWORD'))
    db_host     = os.getenv('DB_HOST')
    db_port     = os.getenv('DB_PORT', 3306)
    db_name     = os.getenv('DB_NAME')
    
  
    # Create the database URL
    database_url = f'mysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
    
    # Create the SQLAlchemy engine
    engine = sqlalchemy.create_engine(database_url)
       
    try:
        connection = engine.connect()
        logger.info("Connected to the MySQL database.")
    except Exception as e:
        raise Exception("Connection failed:", e)
    return engine, connection