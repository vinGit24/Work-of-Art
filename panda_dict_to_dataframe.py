# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 20:19:51 2024

@author: Vincente
"""

import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)
print(df)