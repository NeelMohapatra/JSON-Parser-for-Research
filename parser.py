#! /usr/bin/env python3
# Goes through each files in the directory and checks for keys.
# TODO: Accumulate all data in a csv file and make them easier to parse.
# Might have to figure out connections between companies for more insights

import json, os, csv, re
from pprint import pprint
JSON_DIR = '/Users/swojit/Downloads/companies'
files = os.listdir(JSON_DIR)
errors = []
keys = []
working_files = []
for file in files:
    json_file = open(JSON_DIR + '/' + file)
    data = json.load(json_file)
    keys.extend(data.keys())
    try:
        working_files.append(data)
#        print()
#        pprint(data['markets'])
    except KeyError:
        errors.append(file)
print(len(files) - len(errors))
keys = set(keys)
print(keys)
for error in errors:
    pprint(error)
outputfile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputfile)
outputWriter.writerow([key for key in keys])
for file in working_files:
    row = []
    for key in keys:
        try:
            row.append(file[key])
        except KeyError:
            row.append('NOTHING_HERE')
    if not file['hidden']:
       outputWriter.writerow(row)
outputfile.close()
