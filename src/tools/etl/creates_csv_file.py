# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 17:56:29 2025

@author: Haroon
"""
import logging
import os 

logger = logging.getLogger("pipeline")
def create_csv_files(output_dir,resource_type,df):
    """
    Store the DF by resource type in a csv file in the output folder 
   
    Parameters
    ----------
    df : Dataframe
        Dataframe of the data per resrouce.

    Returns
    -------
    None.

    """
    csv_path = os.path.join(output_dir, f"{resource_type}_flat.csv")
   
    df.to_csv(csv_path, index=False)
    
    logger.info(f"Saved {resource_type} records to {csv_path}")