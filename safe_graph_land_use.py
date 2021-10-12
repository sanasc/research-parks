import pandas as pd
import os
import json
import glob

uDict = {}
uDict["date"] = []
uDict["visits"] = []

pDict = {}
pDict["date"] = []
pDict["visits"] = []

city = "Houston" # Chicago, Houston, LA, NewYork, Phoenix
urbanType = "distanceFromCenter" # walkability or distanceFromCenter

csv_urban = glob.glob("C:/Users/12068/Documents/GitHub/research-parks/data/drive-download-20210924T225303Z-001/" + city + "/" + urbanType + "/urban/*.csv")
csv_notUrban = glob.glob("C:/Users/12068/Documents/GitHub/research-parks/data/drive-download-20210924T225303Z-001/" + city + "/" + urbanType + "/notUrban/*.csv")

for f in csv_urban:
    df = pd.read_csv(f)
    df.columns = ["placekey","safegraph_place_id","parent_placekey","parent_safegraph_place_id","location_name","street_address","city","region","postal_code","safegraph_brand_ids","brands","date_range_start","date_range_end","raw_visit_counts","raw_visitor_counts","visits_by_day","poi_cbg","visitor_home_cbgs","visitor_daytime_cbgs","visitor_country_of_origin","distance_from_home","median_dwell","bucketed_dwell_times","related_same_day_brand","related_same_month_brand","popularity_by_hour","popularity_by_day","device_type"]

    for index, row in df.iterrows():
        month = row["date_range_start"]
        month = str(month)[0:7]

        if row["visits_by_day"] != "visits_by_day":
            arr = json.loads(row["visits_by_day"])
            index = 1

            for x in arr:
                date = ('0' + str(index)) if index < 10 else str(index)
                uDict["date"].append(month + "-" + date)
                uDict["visits"].append(x)
                index+=1

for f in csv_notUrban:
    df = pd.read_csv(f)
    df.columns = ["placekey","safegraph_place_id","parent_placekey","parent_safegraph_place_id","location_name","street_address","city","region","postal_code","safegraph_brand_ids","brands","date_range_start","date_range_end","raw_visit_counts","raw_visitor_counts","visits_by_day","poi_cbg","visitor_home_cbgs","visitor_daytime_cbgs","visitor_country_of_origin","distance_from_home","median_dwell","bucketed_dwell_times","related_same_day_brand","related_same_month_brand","popularity_by_hour","popularity_by_day","device_type"]

    for index, row in df.iterrows():
        month = row["date_range_start"]
        month = str(month)[0:7]

        if row["visits_by_day"] != "visits_by_day":
            arr = json.loads(row["visits_by_day"])
            index = 1

            for x in arr:
                date = ('0' + str(index)) if index < 10 else str(index)
                uDict["date"].append(month + "-" + date)
                uDict["visits"].append(x)
                index+=1

urban_df = pd.DataFrame.from_dict(uDict)
not_urban_df = pd.DataFrame.from_dict(pDict)

urban_df.to_csv(path_or_buf="data/LandType/" + city + "-" + urbanType + "-Urban.csv", index=False)
not_urban_df.to_csv(path_or_buf="data/LandType/" + city + "-" + urbanType + "-NonUrban.csv", index=False)

