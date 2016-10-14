#! /usr/bin/env python3

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
        pprint(data)
    except KeyError:
        errors.append(file)
print(len(files) - len(errors))
print(set(keys))
