import pandas as pd
import json

filename = "allHouston"
pdata = pd.read_csv("data/" + filename + ".csv")
#pdata['date'] = pd.to_datetime(pdata["date_range_start"][0:10])
#pdata.sort_values("date")

# <5, 5-10, 11-20, 21-60, 61-120, 121-240, >240
dict = {}
dict["month"] = []
dict["<5"] = []
dict["5-10"] = []
dict["11-20"] = []
dict["21-60"] = []
dict["61-120"] = []
dict["121-240"] = []
dict[">240"] = []

for index, row in pdata.iterrows():
    month = row["date_range_start"]
    #print(month)
    month = str(month)[0:10]
    if month == "NaT":
        print("hi")

    if row["bucketed_dwell_times"] != "bucketed_dwell_times":
        arr = json.loads(row["bucketed_dwell_times"])

        dict["month"].append(month)

        dict["<5"].append(arr["<5"])
        dict["5-10"].append(arr["5-10"])
        dict["11-20"].append(arr["11-20"])
        dict["21-60"].append(arr["21-60"])
        dict["61-120"].append(arr["61-120"])
        dict["121-240"].append(arr["121-240"])
        dict[">240"].append(arr[">240"])

resultdf = pd.DataFrame.from_dict(dict)
resultdf.to_csv(path_or_buf="data/" + filename + "Dwell.csv", index=False)
