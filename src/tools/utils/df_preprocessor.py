# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 11:28:59 2025

@author: Haroon
"""
import logging
import numpy as np
from datetime import datetime, timezone
import json

logger = logging.getLogger("pipeline")
def df_processor(df):
    """
    

    Parameters
    ----------
    df : Dataframe by resource 
        The dataframe will be past here to clean and ad columns and getthe patient ID .

    Raises
    ------
    ValueError
        Raises Error when dataframe is empty .

    Returns
    -------
    df : Data Frame after cleaning and adding columns
        resouce Dataframe.

    """
    # Current time
    now = datetime.now(timezone.utc).replace(microsecond=0)
    
    #replace string Nan values
    df = df.replace(["NaN", "nan"], np.nan)
    
    # Replace string Nan values with None
    df = df.applymap(lambda x: None if str(x).lower() in ['nan', 'none'] else x)
    
    
    # Try to find subject_reference column split the string after 'urn:uuid:'   and take the patient and create a new column called 
    # patient_reference_uuid
    try:
         df['patient_reference_uuid'] = df['subject_reference'].apply(
          lambda x: x.split(':')[-1] if isinstance(x, str) and x.startswith('urn:uuid:') else None)
    except:
       pass
    
    # Try to find subject_reference column split the string after 'urn:uuid:'   and take the patient and create a new column called 
    # patient_reference_uuid
    try:
         df['patient_reference_uuid'] = df['patient_reference'].apply(
          lambda x: x.split(':')[-1] if isinstance(x, str) and x.startswith('urn:uuid:') else None)
    except:
       pass

    # Check if df is empty and ad current time to new columns called created_at nad updated_at
    if not df.empty:
        df['created_at'] = now
        df['updated_at'] = now
    else:
        raise ValueError("DataFrame is None. Possible read failure.")

   
    # Clean each DataFrame before inserting to SQL
    # It will convert the this into a json string 
    for col in df.columns:
         if df[col].apply(lambda x: isinstance(x, (list, dict))).any():
             df[col] = df[col].apply(lambda x: json.dumps(x) if isinstance(x, (list, dict)) else x)
    
    return df