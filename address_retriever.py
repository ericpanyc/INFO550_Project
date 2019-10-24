import requests
import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import json
import ssl
import sys
import getopt

mapquest_api_key = '02a91AFeVAgZZESVRXJWG1PqBZsj5CBs'
zillow_id ='X1-ZWz1hf0g4zbv2j_65xu9'


def creat_geo_list(lati_given, longi_given, geometry_lst):
    lati_str = str(lati_given)
    longi_str = str(longi_given)
    left_lati_str = lati_str.split('.')[0]
    right_lati_str = lati_str.split('.')[1]
    left_longi_str = longi_str.split('.')[0]
    right_longi_str = longi_str.split('.')[1]

    for lati in range(int(right_lati_str)-50000, int(right_lati_str)+50000, 10000):
        for longi in range(int(right_longi_str)-50000, int(right_longi_str)+50000, 10000):
            lati_float = float(left_lati_str+'.'+str(lati))
            longi_float = float(left_longi_str+'.'+str(longi))
            geometry = [lati_float, longi_float]
            geometry_lst.append(geometry)
    return geometry_lst

lati = 0
longi = 0
fullCmdArguments = sys.argv
argumentList = fullCmdArguments[1:]
unixOptions = "l:g:"
gnuOptions = ["lati=", "longi="]
try:
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    print (str(err))
    sys.exit(2)
for currentArgument, currentValue in arguments:
    if currentArgument in ("-l", "--lati"):
        lati = currentValue
    elif currentArgument in ("-g", "--longi"):
        longi = currentValue
#
geometry_lst = []
geometry_lst = creat_geo_list(lati, longi, geometry_lst)


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


full_string = ''
for geometry in geometry_lst:
    single_string = 'location=' + str(geometry[0]) + ',' + str(geometry[1]) + '&'
    full_string = full_string + single_string

url = "http://www.mapquestapi.com/geocoding/v1/batch?key=KEY&LHOLDERignoreLatLngInput=false"
url = url.replace('KEY', mapquest_api_key)
url = url.replace("LHOLDER", full_string)


address_list = []
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
js = json.loads(data)
for element in js['results']:
    address = element['locations'][0]["street"] + ' ' + element['locations'][0]["adminArea5"]
    address_list.append(address)


with open('test_zillow_data.txt', 'w') as output:
    for idx in range(0,len(address_list)):
        address = address_list[idx]
        address = address.replace(' ', '+')
        url = "http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id=IDHOLDER&address=ADDRESS&citystatezip=Los+Angeles%2C+CA"
        url = url.replace('IDHOLDER', zillow_id)
        url = url.replace('ADDRESS', address)
        r = requests.get(url)
        root = ET.fromstring(r.content)
        details = []
        details.append(str(idx+1))
        for child in root.iter('*'):
            if child.tag == 'code':
                #print(child.text)
                if int(child.text) != 0:
                    details.append('wrong address')
                    break
            if child.tag == 'street':
                if child.text:#print(child.text)
                    details.append(child.text)
                else:
                    details.append('NA')
            if child.tag == 'city':
                if child.text:#print(child.text)
                    details.append(child.text)
                else:
                    details.append('NA')
            if child.tag == 'latitude':
                if child.text:#print(child.text)
                    details.append(child.text)
                else:
                    details.append('NA')
            if child.tag == 'longitude':
                if child.text:#print(child.text)
                    details.append(child.text)
                else:
                    details.append('NA')
            if child.tag == 'bedrooms':
                if child.text:#print(child.text)
                    details.append(child.text)
                else:
                    details.append('NA')
            if child.tag == 'amount':
                if child.text:#print(child.text)
                    details.append(child.text)
                else:
                    details.append('NA')
            if child.tag == 'region':
                if child.attrib['name']:#print(child.text)
                    details.append(child.attrib['name'])
                else:
                    details.append('NA')
        s = ","
        s = s.join(details)
        output.write(s + '\n')
