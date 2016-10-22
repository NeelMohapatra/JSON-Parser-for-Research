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
for file in files:
    json_file = open(JSON_DIR + '/' + file)
    data = json.load(json_file)
    keys.extend(data.keys())
    try:
        print()
        pprint(data['markets'])
    except KeyError:
        errors.append(file)
print(len(files) - len(errors))
print(set(keys))
for error in errors:
	pprint(error)
