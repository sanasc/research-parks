import pandas as pd
import json

filename = "allHouston" # allChicago, allHouston, allLA, allNY, allPh
pdata = pd.read_csv("data/" + filename + ".csv")

# Create lists for each column
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

# Iterate through entire dataframe
for index, row in pdata.iterrows():
    month = row["date_range_start"]
    month = str(month)[0:10] # Grab the date portion of the timestamp

    # Quick check to make sure it isn't the column header row
    if row["bucketed_dwell_times"] != "bucketed_dwell_times":
        arr = json.loads(row["bucketed_dwell_times"])

        # Append data to lists inside of the dictionary
        dict["month"].append(month)

        dict["<5"].append(arr["<5"])
        dict["5-10"].append(arr["5-10"])
        dict["11-20"].append(arr["11-20"])
        dict["21-60"].append(arr["21-60"])
        dict["61-120"].append(arr["61-120"])
        dict["121-240"].append(arr["121-240"])
        dict[">240"].append(arr[">240"])

# Create a new dataframe from the dictionary and write a csv file
resultdf = pd.DataFrame.from_dict(dict)
resultdf.to_csv(path_or_buf="data/" + filename + "Dwell.csv", index=False)
