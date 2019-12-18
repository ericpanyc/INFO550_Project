import pandas as pd
import re
from datetime import datetime
from dateutil.parser import parse
import missingno as msno
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import json
import folium


table = pd.read_csv("training_control_inc_rate_diff_test.csv")
table['rate'] = pd.to_numeric(table['rate'],errors='coerce')
#table.rate = table.rate.astype(int)
table.zipcodes = table.zipcodes.astype(str)
#print(table.dtypes)
def create_map(table, zips, mapped_feature, add_text = ''):
    # reading of the updated GeoJSON file
    la_geo = r'updated-file.json'
    # initiating a Folium map with LA's longitude and latitude
    m = folium.Map(location = [34.0522, -118.2437], zoom_start = 10)
    # creating a choropleth map
    folium.Choropleth(
        geo_data = la_geo,
        fill_opacity = 0.7,
        line_opacity = 1.0,
        data = table,
        # refers to which key within the GeoJSON to map the ZIP code to
        key_on = 'feature.properties.name',
        # first element contains location information, second element contains feature of interest
        columns = [zips, mapped_feature],
        fill_color = 'PuBuGn',
        legend_name = 'rank in increasing ' + (' ').join(mapped_feature.split('_')).title() + ' difference' + add_text
    ).add_to(m)




    #folium.LayerControl().add_to(m)
    # save map with filename based on the feature of interest
    m.save(outfile = mapped_feature + '_map.html')

create_map(table, 'zipcodes', 'rate', '')
