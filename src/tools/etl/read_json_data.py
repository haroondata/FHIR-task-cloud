# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 12:00:00 2025

@author: Haroon
"""
import logging
import os
import json
from collections import defaultdict


def flatten_json(nested_json: dict) -> dict:
    """
    

    Parameters
    ----------
    nested_json : TYPE
        DESCRIPTION.

    Returns
    -------
    flat : TYPE
        DESCRIPTION.

    """
    flat = {}

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

    flat = flatten_json(resource)

    # Extract name: combine first name and family name if available
    name_info = resource.get("name", [{}])[0]
    family = name_info.get("family", "")
    given = " ".join(name_info.get("given", [])) if isinstance(name_info.get("given"), list) else name_info.get("given", "")
    full_name = f"{given} {family}".strip()

    # Extract telecoms: phone and email
    telecom_entries = resource.get("telecom", [])
    phone = email = None
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
    
    keys_to_remove = [k for k in flat if k.startswith("name.") or k == "name" or k.startswith("telecom.")or k == "telecom"]
    for key in keys_to_remove:
        flat.pop(key, None)
    return flat

def get_data_from_json():
    """
    

    Returns
    -------
    resource_map : TYPE
        DESCRIPTION.

    """
    # === File Path ===
    data_dir = os.path.join("/app/data")

    
    resource_map = defaultdict(list)
    file_tracking_map = {} 
    #mysql connection
    # === Loop over all JSON files ===
    for file in os.listdir(data_dir):
        if file.endswith(".json"):
            file_path = os.path.join(data_dir, file)
            logging.info(f"Processing file: {file_path}")
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    bundle = json.load(f)
            except (json.JSONDecodeError, UnicodeDecodeError) as e:
                logging.error(f"Invalid JSON file: {file_path} — {e}")
                continue


    
            # === Flatten and group by resourceType ===
            if 'entry' not in bundle or not bundle['entry']:
                logging.warning(f"No 'entry' found in {file_path}. Skipping.")
                continue
            entries = bundle.get('entry', [])
            for item in entries:
                resource = item.get('resource', {})
                resource_type = resource.get('resourceType', 'Unknown')
                if resource_type == "Patient":
                    flat = extract_patient_data(resource)
                else:
                    flat = flatten_json(resource)
                resource_map[resource_type].append(flat)
                file_tracking_map[resource_type] = file 
    return resource_map, file_tracking_map






    



    