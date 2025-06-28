# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 17:56:29 2025

@author: Haroon
"""
import logging
import os 
def create_csv_files(output_dir,resource_type,df):
    """
    

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    csv_path = os.path.join(output_dir, f"{resource_type}_flat.csv")
   
    df.to_csv(csv_path, index=False)
    
    logging.info(f"Saved {resource_type} records to {csv_path}")