# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 18:51:37 2025

@author: Haroon
"""

import os
import json
import pandas as pd
from collections import defaultdict
check_stack = []

def flatten_json(nested_json):
    flat = {}

    def recurse(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, (dict, list)):
                    recurse(value)
                else:
                    flat[key] = value  
        elif isinstance(obj, list):
            for item in obj:
                recurse(item)

    recurse(nested_json)
    return flat



# === File Path ===
data_dir = "C:/Users/Haroon/Downloads/exa-data-eng-assessment-main (1)/exa-data-eng-assessment-main/data/"

resource_map = defaultdict(list)
# === Loop over all JSON files ===
for file in os.listdir(data_dir):
    if file.endswith(".json"):
        file_path = os.path.join(data_dir, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            bundle = json.load(f)

        # === Flatten and group by resourceType ===
        entries = bundle.get('entry', [])
        
        
        for item in entries:
            print(item)
            resource = item.get('resource', {})
            resource_type = resource.get('resourceType', 'Unknown')
            flat = flatten_json(resource)
            resource_map[resource_type].append(flat)

# === Save each resourceType as its own CSV ===
output_dir = "./output"
os.makedirs(output_dir, exist_ok=True)

for resource_type, records in resource_map.items():
    df = pd.DataFrame(records)
    csv_path = os.path.join(output_dir, f"{resource_type}_flat.csv")
    df.to_csv(csv_path, index=False)
    print(f"Saved {resource_type} records to {csv_path}")
for rtype, records in resource_map.items():
    print(f"{rtype}: {len(records)} entries")