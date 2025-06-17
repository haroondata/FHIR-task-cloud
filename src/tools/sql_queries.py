# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:48:23 2024

@author: Haroon
"""

from sqlalchemy import text
import pandas as pd

#create df
def create_df(connection):
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
    sql_select = """Select * from data_projects.dbo.retail_data"""
    sql_query_select = text(sql_select)
    print(sql_query_select)
    data = connection.execute(sql_query_select).fetchall()
    df = pd.DataFrame(data)
   
    return df
