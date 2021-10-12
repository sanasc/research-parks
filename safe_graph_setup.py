import pandas as pd
import json

parkdata = pd.read_csv("data/phoenix.csv")
parkdata.columns=["index","placekey","low_svi_percentage","safegraph_place_id","parent_placekey","parent_safegraph_place_id","location_name","street_address","city","region","postal_code","safegraph_brand_ids","brands","time","date_range_end","raw_visit_counts","raw_visitor_counts","visits_by_day","poi_cbg","visitor_home_cbgs","visitor_daytime_cbgs","visitor_country_of_origin","distance_from_home","median_dwell","bucketed_dwell_times","related_same_day_brand","related_same_month_brand","popularity_by_hour","popularity_by_day","device_type"]
parkdata["date"] = pd.to_datetime(parkdata["time"].str[0:10])
parkdata.sort_values("date")

dict = {}
dict['date'] = []
dict['visits'] = []
for index in parkdata["index"]:
    month = parkdata["date"][index]
    month = month.strftime("%Y-%m-")

    #print(type(parkdata["visits_by_day"][index]))
    #print(month)

    arr = json.loads(parkdata["visits_by_day"][index])
    index = 1
    for x in arr:
        #print(x)
        date = ('0' + str(index)) if index < 10 else str(index)
        #print(date)
        #dict[month + date] = [x]
        dict['date'].append(month + date)
        dict["visits"].append(x)
        index+=1
#print(dict)

resultdf = pd.DataFrame.from_dict(dict)
resultdf.to_csv(path_or_buf="data/phoenixoutput.csv", index=False)
