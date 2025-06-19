# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 18:06:00 2024

@author: Haroon
"""

from sqlalchemy import text


#insert data
def insert_data_into_mysql(mysql_engine,mysql_connection,df,table_name):
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
    try:
        print("Inserting into table:", table_name)
        print(df)
        df.to_sql(table_name, con=mysql_engine, if_exists="append", index=False)
        print("Data inserted successfully.")
    except Exception as e:
        print("Error inserting data:", e)
