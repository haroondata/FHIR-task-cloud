# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 17:54:39 2025

@author: Haroon
"""
import logging

logger = logging.getLogger("pipeline")

def check_if_connection_is_closed(mysql_connection):  
    """
    
    This function will check if the connection is closed 
    Returns
    -------
    None.

    """
    #Check if connection is closed
    try:
        mysql_connection.close()
        logger.info("MySQL connection is closed")
    except Exception as e:
        logger.info(f"Failed to close connection:{e}")