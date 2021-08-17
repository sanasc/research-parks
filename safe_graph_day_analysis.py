
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
import warnings
from datetime import datetime,date
import ast
import os
import json

parkdata=pd.read_csv("data/phoenix.csv")
parkdata.columns=["index","placekey","low_svi_percentage","safegraph_place_id","parent_placekey","parent_safegraph_place_id","location_name","street_address","city","region","postal_code","safegraph_brand_ids","brands","time","date_range_end","raw_visit_counts","raw_visitor_counts","visits_by_day","poi_cbg","visitor_home_cbgs","visitor_daytime_cbgs","visitor_country_of_origin","distance_from_home","median_dwell","bucketed_dwell_times","related_same_day_brand","related_same_month_brand","popularity_by_hour","popularity_by_day","device_type"]

parkdata["date"] = pd.to_datetime(parkdata["time"].str[0:10])

parkdata.sort_values('date')

mask1 = (parkdata["date"] < pd.to_datetime('2020-03-01'))
mask2 = (parkdata["date"] >= pd.to_datetime('2020-03-01')) & (parkdata["date"] <= pd.to_datetime('2020-03-31'))
mask3 = (parkdata["date"] > pd.to_datetime('2020-03-31'))

parkdataPRE = parkdata.loc[mask1]
parkdataSAHO = parkdata.loc[mask2]
parkdataPOST = parkdata.loc[mask3]

a = [[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]]
count = 0
for entry in parkdataPRE["popularity_by_day"]:

    map = json.loads(entry)
    i = 0
    for x in map:
        a[0][i] += map[x]
        i+=1
        #print(map[x])
    count+=1
print(count)
count = 0
for entry in parkdataPOST["popularity_by_day"]:

    map = json.loads(entry)
    i = 0
    for x in map:
        a[1][i] += map[x]
        i+=1
        #print(map[x])
    count+=1
print(count)

print(a)
