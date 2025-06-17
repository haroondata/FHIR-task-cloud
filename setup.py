# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:44:26 2024

@author: Haroon
"""


#ms sql connection 
from src.tools.mssql_connection import  mssql_connection

#mysql connection 
from src.tools.mysql_connection import  mysql_connection

#create df 
from src.tools.sql_queries import create_df

#insert data into db table
from src.tools.insert_data_into_mysql import insert_data_into_mysql



if __name__ == '__main__':
    # mssql connection 
   engine,connection =  mssql_connection()
   
   #mysql connection
   mysql_engine,mysql_connection =  mysql_connection()
  
    
   #select data from mssql 
   df = create_df(connection)
   
   
   #insert data into mysql
   insert_data_into_mysql(mysql_connection,df)
   
   
   # # Check if connection is closed
   connection.close()
   if connection.closed:
         print("Connection is closed")
   else:
         print("Connection is open")