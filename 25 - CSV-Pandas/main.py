import pandas
import csv
'''import csv
temperatures = []

with open("weather_data.csv") as f:
    data = csv.reader(f)
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

print(temperatures)'''



# tempsum = 0
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data.temp)
#
# print(data["temp"].mean())
#
#
# row = data[data.day == "Monday"]
# temp = int(row.temp.get(0)) * 9/5 + 32
#
# print(temp)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": []
}
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

for color in ["Gray", "Cinnamon", "Black"]:
    c_rows = data[data["Primary Fur Color"] == color]
    count = c_rows["Unique Squirrel ID"].count()
    data_dict["Count"].append(count)

# Pandas dataframes constructor import dicts natively and applies the keys as column names
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
print(data_dict)
print(df)



