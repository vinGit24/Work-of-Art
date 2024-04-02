# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 22:47:52 2024

@author: Vincente
"""

import pandas as pd

def json_to_csv(json_file_path, csv_file_path):
    try:
        # Load the JSON file into a pandas DataFrame
        df = pd.read_json(json_file_path)
    except ValueError as e:
        print(f"Error occurred while reading the JSON file: {e}")
        return
    except FileNotFoundError as e:
        print(f"Error occurred because the JSON file was not found: {e}")
        return

    try:
        # Write the DataFrame to a CSV file
        df.to_csv(csv_file_path, index=False)
    except Exception as e:
        print(f"Error occurred while writing to the CSV file: {e}")
        return

    print("Successfully converted the JSON file to a CSV file.")

# Usage
json_file_path = "C:/Python Script Lib/Scripts Lib/Pandas/nasa.json"
csv_file_path = 'C:/Python Script Lib/Scripts Lib/Pandas/nasa.csv'
json_to_csv(json_file_path, csv_file_path)

