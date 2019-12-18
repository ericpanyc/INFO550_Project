import pandas as pd
import re
from datetime import datetime
from dateutil.parser import parse
import missingno as msno
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import json


zipList = ['91107','91775','91006','91024','91016','91706','91010','91702','91722','91741','91740','90064','90249','90808','90630','90621','90631','92805','90068','91506','91762']
with open('la_zipcode.geojson', 'r') as jsonFile:
    data = json.load(jsonFile)
tmp = data

# remove ZIP codes not in our dataset
geozips = []
for i in range(len(tmp['features'])):
    if tmp['features'][i]['properties']['name'] in zipList:
        geozips.append(tmp['features'][i])

# creating new JSON object
new_json = dict.fromkeys(['type','features'])
new_json['type'] = 'FeatureCollection'
new_json['features'] = geozips

# save JSON object as updated-file
open("updated-file.json", "w").write(
    json.dumps(new_json, sort_keys=True, indent=4, separators=(',', ': '))
)
