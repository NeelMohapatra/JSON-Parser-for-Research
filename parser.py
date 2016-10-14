#! /usr/bin/env python3

import json, os, csv, re
from pprint import pprint
JSON_DIR = '/Users/swojit/Downloads/companies'
files = os.listdir(JSON_DIR)
errors = []
for file in files:
    json_file = open(JSON_DIR + '/' + file)
    data = json.load(json_file)
    try:
        print(data['name'])
    except KeyError:
        errors.append(file)
for file in errors:
    data = json.load(open(JSON_DIR + '/' + file))
    pprint(data)
