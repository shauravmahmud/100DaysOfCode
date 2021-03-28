with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

import csv

temperatures = []

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

#average = sum(temp_list) / len(temp_list)
#print(average)

print(data["temp"].mean())
print(data["temp"].max())
print(data["temp"].min())

print(data["condition"])
print(data.condition)

max_temp = data["temp"].max()
#Get Row in Data
print(data[data.temp == max_temp])

#or
print(data[data.temp == data.temp.max()])

#Get data in a row, we can also find conditions
monday = data[data.day == "Monday"]
print(monday.condition)

#Create a dataframe from scratch
#data = pandas.DataFrame(data_dict)