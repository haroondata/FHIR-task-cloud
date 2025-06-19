# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 18:06:00 2024

@author: Haroon
"""

from sqlalchemy import text


#insert data
def insert_data_into_mysql(mysql_connection,df,table_name):
    """
    

    Parameters
    ----------
    mysql_connection : TYPE
        DESCRIPTION.
    df : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """    
    df.to_sql(table_name, con=mysql_connection, if_exists="append", index=False)
