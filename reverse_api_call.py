import requests
import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import json
import ssl
import sys
import re
import getopt

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lon = str(37.7812808)
lat = str(-122.4152363)


url = "https://nominatim.openstreetmap.org/reverse?format=geojson&lat=lat_hold&lon=lon_hold"
url = url.replace("lat_hold", lat)
url = url.replace("lon_hold", lon)

uh = urllib.request.urlopen("https://nominatim.openstreetmap.org/reverse?format=geojson&lat=44.50155&lon=11.33989", context=ctx)
data = uh.read()
js = json.loads(data)
print(json.dumps(js, indent = 4,  sort_keys = True))
