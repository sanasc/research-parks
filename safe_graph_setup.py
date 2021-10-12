import pandas as pd
import json

filename = "allPh"
pdata = pd.read_csv("data/" + filename + ".csv")
#pdata['date'] = pd.to_datetime(pdata["date_range_start"][0:10])
#pdata.sort_values("date")

dict = {}
dict['date'] = []
dict['visits'] = []
for index in parkdata["index"]:
    month = parkdata["date"][index]
    month = month.strftime("%Y-%m-")

    if row["visits_by_day"] != "visits_by_day":
        arr = json.loads(row["visits_by_day"])
        index = 1

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
resultdf.to_csv(path_or_buf="data/" + filename + "Output.csv", index=False)
