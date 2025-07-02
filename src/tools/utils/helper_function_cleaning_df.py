# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 11:28:59 2025

@author: Haroon
"""

def clean_fhir_column_names(df):
    """
    
    Clean dataframe columns
    Parameters
    ----------
    df : Dataframe 
         Datafame will be cleaned
        

    Returns
    -------
    df : Dataframe
        return dataframe will clean column names.

    """
    df.columns = (
        df.columns
        .str.replace(r'\.', '_', regex=True)          # replace dots with underscores
        .str.replace(r'\W+', '_', regex=True)         # remove weird characters
        .str.strip('_')                               # trim leading/trailing underscores
        .str.lower()                                  # lowercase for uniformity
       )


    return df