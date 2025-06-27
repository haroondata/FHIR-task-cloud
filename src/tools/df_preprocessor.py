# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 11:28:59 2025

@author: Haroon
"""
import logging
import numpy as np
from datetime import datetime, timezone
import json

def df_processor(df):
    now = datetime.now(timezone.utc).replace(microsecond=0)
    
    df = df.replace(["NaN", "nan"], np.nan)

    df = df.applymap(lambda x: None if str(x).lower() in ['nan', 'none'] else x)
    
    for col in df.columns:
       logging.debug(f"Column '{col}' has dtype {df[col].dtype}")
       
       
    try:
         df['patient_reference_uuid'] = df['subject_reference'].apply(
          lambda x: x.split(':')[-1] if isinstance(x, str) and x.startswith('urn:uuid:') else None)
    except:
       pass

    try:
         df['patient_reference_uuid'] = df['patient_reference'].apply(
          lambda x: x.split(':')[-1] if isinstance(x, str) and x.startswith('urn:uuid:') else None)
    except:
       pass


    if not df.empty:
        df['created_at'] = now
        df['updated_at'] = now
    else:
        raise ValueError("DataFrame is None. Possible read failure.")

   
    # Clean each DataFrame before inserting to SQL
    for col in df.columns:
         if df[col].apply(lambda x: isinstance(x, (list, dict))).any():
             df[col] = df[col].apply(lambda x: json.dumps(x) if isinstance(x, (list, dict)) else x)
    
    return df