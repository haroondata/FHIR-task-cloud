# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:48:23 2024

@author: Haroon
"""

from sqlalchemy import text
import pandas as pd

#create df
def create_table(mysql_connection,sql_code):
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
    sql_query_select = text(sql_code)
    print(sql_query_select)
    mysql_connection.execute(sql_query_select)
    print("Table created successfully.")

   
   
   