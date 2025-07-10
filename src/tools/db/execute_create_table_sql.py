# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 12:00:00 2025

@author: Haroon
"""

from sqlalchemy import text

import logging

logger = logging.getLogger("pipeline")

def execute_create_table_sql_queries(mysql_connection,sql_code):
    """
    
    Check if the sql_code is avalable raise na warning



    Parameters
    ----------
    connection : db connection
       This is the database connection.
    sql_code : String
        This is the sql strings.

    Returns
    -------
    None.

    """
   
    # Check if sql code is provided
    if not sql_code.strip():
        logger.warning("No SQL code provided to create_table.")
        return
    try:
        # Convert raw SQL string to SQLAlchemy raw string
        sql_query_select = text(sql_code)
        # Execute sql query
        mysql_connection.execute(sql_query_select)
        mysql_connection.commit() 
        logger.info("Table created successfully.")
    except Exception as e:
        logger.error(f"Failed to create table. SQL: {sql_code[:100]}...")
        logger.exception(e)
    
   
   
def create_audit_log_table(mysql_connection):
    try:
        audit_log_create_statement = """CREATE TABLE IF NOT EXISTS pipeline_audit_log (
                                    id INT AUTO_INCREMENT PRIMARY KEY,
                                    resource_type VARCHAR(255),
                                    inserted_rows INT,
                                    inserted_at DATETIME DEFAULT CURRENT_TIMESTAMP
                                        );
                                """
        sql_query_select = text(audit_log_create_statement)
        mysql_connection.execute(sql_query_select)
        mysql_connection.commit() 
        logger.info("Table created successfully.")
        
    except Exception as e:
        logger.error(f"Failed to create table. SQL: {audit_log_create_statement[:100]}...")
        logger.exception(e)
    