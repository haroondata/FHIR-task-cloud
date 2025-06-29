# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 12:00:00 2025

@author: Haroon
"""

from sqlalchemy import text

import logging

def execute_create_table_sql_queries(mysql_connection,sql_code):
    """
    

    Parameters
    ----------
    connection : TYPE
        DESCRIPTION.

    Returns
    -------
    df : TYPE
        DESCRIPTION.

    """
    if not sql_code.strip():
        logging.warning("No SQL code provided to create_table.")
        return
    try:
        sql_query_select = text(sql_code)
        mysql_connection.execute(sql_query_select)
        logging.info("Table created successfully.")
    except Exception as e:
        logging.error(f"Failed to create table. SQL: {sql_code[:100]}...")
        logging.exception(e)
    
   
   
   