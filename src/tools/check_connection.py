# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 17:54:39 2025

@author: Haroon
"""
import logging

def check_if_connection_is_closed(mysql_connection):  
    """
    
    
    Returns
    -------
    None.

    """
    #Check if connection is closed
    try:
        mysql_connection.close()
        logging.info("MySQL connection is closed")
    except Exception as e:
        logging.info(f"Failed to cose connection:{e}")