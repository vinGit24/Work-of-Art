# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 15:05:32 2024

@author: Vincente
"""
import json
# Define a JSON string
json_str = '{"type": "Fruit", "name": "Apple", "color": "Red", "Age of Fruit": 3}'

"""""""""""""""""""""""""""""""""""""""""""""
json.loads():
Takes a STRING OBJECT (a valid JSON string) as an argument.
Parses the JSON string and converts it into a Python dictionary.
Mainly used for deserializing native strings or byte arrays containing JSON data.
"""""""""""""""""""""""""""""""""""""""""""""""""""

parsed_data = json.loads(json_str)
# Print the result and access data
print(parsed_data)
print(f"Color: {parsed_data['color']}")
print("The converted object is of type:" + str(type(parsed_data)))


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
json.load()
Convert JSON FILE OBJECT to Python Dictionary object 
Takes a file object as an argument.
Reads JSON-encoded data from the file and converts it into a Python dictionary.
Deserializes the file itself
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import json
# Open a JSON file
filepath = 'C:/Python Script Lib/Scripts Lib/Customers.json'
with open(filepath,"r") as file:
      data = json.load(file)
# Analyzing loaded data

print(f"Total Items: {len(data)}")
for key, value in data.items():    
    print(f"{key}: {value}")


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
json.dumps()
Converts a Python object (e.g., a dictionary) into a JSON-formatted string.
Takes additional parameters like indent for pretty printing.
Useful for returning JSON data from a backend to a frontend (e.g., in web applications).
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Define a Python dictionary
person_dict = {"name": "Jane", "skills": ["coding", "data analysis"], "interests": ["music", "travel"]}

# Convert to JSON
person_json = json.dumps(person_dict)

# Print the JSON string
print(person_json)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
json.dump()
Writes a Python serialized object (e.g., a dictionary) as JSON-formatted data into a file.
Takes a file pointer (opened in write or append mode) as an argument.
Produces a compact JSON representation to save file space.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Python dictionary
person_info = {"name": "Alice", "role": "Developer"}

# Write to a file
with open('info.json', 'w') as file:
    json.dump(person_info, file)
    
  
 
    