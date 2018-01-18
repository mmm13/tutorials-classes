#! /usr/bin/python
import json
#from pprint import pprint
#pprint(data)

json_file='/tmp/mich.json'
with open(json_file, "r") as jf:
    data = json.load(jf)
#print data["hits"]["hits"][4]["_source"]["plat"]
# for k,v in data.items():
#     print("K: "+ k)
#     print(v)
platforms=[]
for hit in data["hits"]["hits"]:
    #print hit["_source"]["plat"]
    platforms.append(hit["_source"]["plat"])
for platform in platforms:
    print "Platform : "+ platform
