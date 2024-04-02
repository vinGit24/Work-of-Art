# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 23:45:16 2024

@author: Vincente
"""
import json
import csv
import pandas as pd


def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


json_file_path = "C:/Python Script Lib/json Files/NHL-Unflat.json"
json_flatten_file_path = "C:/Python Script Lib/json Files/NHL-Flat.json"
csv_file_path = "C:/Python Script Lib/csv Files/NHL-flattend.csv"

# Load JSON data from a file
try:
    
    with open(json_file_path) as f:
        data = json.load(f)
    
    # Flatten the JSON data
    flattened_data = flatten_json(data)
    
    # Write the flattened JSON data to a new file
    with open("C:/Python Script Lib/json Files/NHL-Flat.json", 'w') as f:
        json.dump(flattened_data, f)
    
    print("This is the Flattened JSON data " + str(flattened_data))    
    
except Exception as e:
    print(f"Error occurred while flattening the JSON file: {e}")


# To alleviate the ValuError: "If using all scalar values, you must pass an index" AND-
#if you have multiple rows of data stored in a dictionary, convert it to a list of dictionaries. - 
#Each dictionary represents a row, and Pandas will automatically assign an index.
try:
    df = pd.DataFrame([flattened_data])
    print("The DataFrame with the flattened JSON: " + str(df))
    df.to_csv(csv_file_path, index=False)
except Exception as e:
    print(f"Error creating the csv file: {e}")










