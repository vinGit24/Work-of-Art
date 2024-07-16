import json
import urllib
import csv
from urllib.parse import urlencode 
from urllib.request import Request, urlopen
import pandas as pd
from flatten_json import flatten

#url endpoint
url			= 'https://vuldb.com/?api'									
post_fields	= { 'apikey': 'f513624a85ec4842d2766f69c50bc8a1', 'recent': '10' }	#request

request = Request(url, urlencode(post_fields).encode())
data = urllib.request.urlopen(request).read().decode()
response_data = json.loads(data)
result_data = response_data.get('result', [])

#print(result_data)
print(type(result_data))

# Flatten the nested JSON
df = pd.json_normalize(result_data)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''ANALYSIS'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print(df.info())
# Display the flattened data
#Analysis -> Display first 5 records
print(df.head())
null_counts = df.isnull().sum()
print(f"Number of nulls found {null_counts}")

#This will create a DataFrame with True where cells contain empty strings and False otherwise.
empty_strings = df.applymap(lambda x: x == '')
print(f"Info about empty strings: {empty_strings.info()}")

# Save as CSV
df.to_csv("latestVulns.csv", index=False) 
# Save as Excel (XLSX) 
df = pd.read_csv('latestVulns.csv')
df.to_excel('latestVulns.xlsx', index=False)





