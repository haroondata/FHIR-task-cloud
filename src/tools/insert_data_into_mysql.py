# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 18:06:00 2024

@author: Haroon
"""

from sqlalchemy import text


#insert data
def insert_data_into_mysql(mysql_connection,df):
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
    for index, row in df.iterrows():
        
        invoice_number = row['invoice_number']
        stock_code = row['stock_code']
        description = row['description']
        description =str(description)
        description=description.replace("'","''")
        quantity = row['quantity']
        invoice_date = row['invoice_date']
        unit_price= row['unit_price']
        customer_id = row['customer_id']
        country = row['country']
        print(country)
        sql_insert = """INSERT INTO retail_data (invoice_number	,stock_code,	description,	quantity,	invoice_date,unit_price,	customer_id,	country)
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}','{5}', '{6}', '{7}');""".format(invoice_number	,stock_code,	description,	quantity,	invoice_date,unit_price,	customer_id,	country)
        sql_query_insert = text(sql_insert)
        mysql_connection.execute(sql_query_insert) 
    #connection.commit()