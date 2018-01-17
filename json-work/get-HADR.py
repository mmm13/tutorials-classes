#! /usr/bin/python
import json
from pprint import pprint

json_file='/tmp/mich.json'

json_data=open(json_file)
data=json.load(json_data)

pprint(data)
