# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:41:42 2024
This script use the get JSON data from a web API call to ESPN NHL stats and then use the json.loads() function to parse it.
@author: Vincente
"""

import requests
import json

# Fetch JSON data from a web API
response = requests.get("https://site.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard")

# Parse JSON data
data = json.loads(response.text)

# Print data
print(data)
# Write to a file


try:    
    compact_json = json.dumps(data, separators=(",", ":"))    
except json.JSONDecodeError as e:
    print(e)    

try:    
    sorted_json = json.dumps(compact_json, sort_keys=True)
    with open('NHL.json', 'w') as file:
        json.dump(sorted_json, file)
except json.JSONDecodeError as e:
    print(e)     
finally:
    file.close()
    