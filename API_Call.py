import requests
import xml.etree.ElementTree as ET

r = requests.get("http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id=X1-ZWz1hf0g4zbv2j_65xu9&address=525+20th+Street&citystatezip=San+Francisco%2C+CA")
root = ET.fromstring(r.content)

for child in root.iter('*'):

    print(child.tag, child.text)
