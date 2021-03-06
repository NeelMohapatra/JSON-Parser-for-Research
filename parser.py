#! /usr/bin/env python3
# Goes through each files in the directory and checks for keys.
# Might have to figure out connections between companies for more insights

import json, os, csv, re
from pprint import pprint
JSON_DIR = '/Users/swojit/Downloads/final_companies'
files = os.listdir(JSON_DIR)
errors = []
keys = []
markets = []
working_files = []
decode_errors = []
for file in files:
    try:
        json_file = open(JSON_DIR + '/' + file)
        data = json.load(json_file)
        keys.extend(data.keys())
        try:
             markets.append(data['markets'])
             working_files.append(data)
        except KeyError:
             errors.append(file)
    except:
        decode_errors.append(file) # files that raise decoding errors
keys = set(keys)
print(keys)
outputfile = open('output2.csv', 'w', newline='')
outputWriter = csv.writer(outputfile)
outputWriter.writerow([key for key in keys]) # Header
for file in working_files:
   row = []
   for key in keys:
       try:
           row.append(file[key])
       except KeyError:
            row.append('NOTHING_HERE')
   if not file['hidden']:
       outputWriter.writerow(row)
markets_dict = []
count = set()
for market in markets:
   if len(market):
       for individual in market:
           markets_dict.append(individual)
           count.add(individual['id'])
print("Count of all files:" +  str(len(files)))
# Whoops :P
# print("Working files \n" + str(working_files))
print("Files with decoding errors: \n" + str(decode_errors))
print("Number of unique markets: " + str(len(count)))
print("Number of outgrees: " + str(len(markets_dict)))
outputfile.close()
