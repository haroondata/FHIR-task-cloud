# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 12:00:00 2025

@author: Haroon
"""
import logging
import os
import json
from collections import defaultdict

logger = logging.getLogger("pipeline")

def flatten_json(nested_json: dict) -> dict:
    """
    Recursively flattens a nested JSON object (dict with possible nested dicts/lists) 
    into a single-level dictionary with dot-separated keys.

   Parameters
   ----------
   nested_json : dict
       The nested JSON dictionary to flatten.

   Returns
   -------
   dict
       A flattened dictionary with compound keys representing the original hierarchy.
   """
    # Dictionary flat that will have the dicitonary per resource
    flat = {}
    
    # Recurse function to check if each key in the resource dict 
    # TThe function will go to each item in the json file go to each dicitonary  
    
    def recurse(obj, path=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_path = f"{path}.{key}" if path else key
                recurse(value, new_path)

        elif isinstance(obj, list):
            if all(isinstance(i, dict) for i in obj):
                # Store list of dicts as-is; will process separately
                flat[path] = obj
            else:
                for idx, item in enumerate(obj):
                    new_path = f"{path}.{idx}" if path else str(idx)
                    recurse(item, new_path)

        else:
            flat[path] = obj

    recurse(nested_json)
    return flat

def extract_patient_data(resource: dict) -> dict:
    """
    

    Parameters
    ----------
    resource : dict
        Patient  dicitonary.

    Returns
    -------
    dict
        return the dictioanry.

    """
    # Get the Resource dicotnary for Patient
    flat = flatten_json(resource)

    # Extract name: combine first name and family name if available
    name_info = resource.get("name", [{}])[0]
    
    # Get the family name
    family = name_info.get("family", "")
    # Get the last name
    given = " ".join(name_info.get("given", [])) if isinstance(name_info.get("given"), list) else name_info.get("given", "")
    
    # Make a full name by combining given and family name 
    full_name = f"{given} {family}".strip()

    # Extract telecoms: phone and email
    telecom_entries = resource.get("telecom", [])
    # Set phone and email to None
    phone = email = None
    
    # This forl oop will go through the telcom column and check if phpne or email is None
    # if it is not None it will ge the value
    for entry in telecom_entries:
        if entry.get("system") == "phone" and not phone:
            phone = entry.get("value")
        elif entry.get("system") == "email" and not email:
            email = entry.get("value")

    # Add extracted fields to the flat dictionary
    flat["first_name"] = given
    flat["last_name"] = family
    flat["name_full"] = full_name
    flat["telecom_phone"] = phone
    flat["telecom_email"] = email
    
    # Remove the data with key name and telecom 
    keys_to_remove = [k for k in flat if k.startswith("name.") or k == "name" or k.startswith("telecom.")or k == "telecom"]
    for key in keys_to_remove:
        flat.pop(key, None)
    return flat

def get_data_from_json():
    """
    This function will get each JSON file and get each section of JSON file by 
    resource and create a dictionary for each

    Returns
    -------
    resource_map : dict
        Get data from .
    file_tracking_map : TYPE
        DESCRIPTION.

    """
    #  File Path 
    data_dir = os.path.join("/app/data")

    
    resource_map = defaultdict(list)
    file_tracking_map = {} 
    
    # Loop over all JSON files 
    for file in os.listdir(data_dir):
        # Check for files that the files extension .json
        if file.endswith(".json"):
            # Get the file with the full file path
            file_path = os.path.join(data_dir, file)
            
            logger.info(f"Processing file: {file_path}")
            try:
                # Open file 
                with open(file_path, 'r', encoding='utf-8') as f:
                    bundle = json.load(f)
            except (json.JSONDecodeError, UnicodeDecodeError) as e:
                logger.error(f"Invalid JSON file: {file_path} — {e}")
                continue
            
            # Flatten and group by resourceType 
            # Check if JSON file has the JSON fil has the key bundle
            
            if 'entry' not in bundle or not bundle['entry']:
                logger.warning(f"No 'entry' found in {file_path}. Skipping.")
                continue
            # Got to dicitonary with key Entry
            entries = bundle.get('entry', [])
            # Loop through each dictioanry 
            for item in entries:
                # Get data by resource
                resource = item.get('resource', {})
                # Get the the resource type if it is not now us Unknown
                resource_type = resource.get('resourceType', 'Unknown')
                # Check for resource_type Patient
                if resource_type == "Patient":
                    # Function to get extract patient data
                    flat = extract_patient_data(resource)
                else:
                    # Flatten JSON File
                    flat = flatten_json(resource)
                # Append flat JSON
                resource_map[resource_type].append(flat)
                
                # Add File 
                file_tracking_map[resource_type] = file 
    return resource_map, file_tracking_map






    



    