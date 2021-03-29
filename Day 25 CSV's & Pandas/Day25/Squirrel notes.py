#Create a CSV with Squirrel Count, with Fur Colour and Count within it
import pandas as pd

#Get hold of data
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(data["Primary Fur Color"])
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]

grey_squirrels_ct = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_ct = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_ct = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_ct)
print(red_squirrels_ct)
print(black_squirrels_ct)

data_dict = {
    "Fur Colour": ["Gray", "Cinnamon" , "Black"],
    "Count": [grey_squirrels_ct , red_squirrels_ct , black_squirrels_ct]
}

#Create a dataframe from scratch
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")