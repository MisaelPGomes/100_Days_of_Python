#with open("weather_data.csv") as file:
#    data = file.readlines()
#    print(data)

import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
#data = pandas.read_csv("weather_data.csv")
#print(data)
# #data_dict = data.to_dict()
# #print(data_dict)

# #temp_list = data["temp"].to_list()

# #print(data["temp"].mean())
# #print(data["temp"].max())
# #print(data.condition)

# monday = data[data.day == "Monday"]
# celcius_temp = int(monday.temp)
# # (9*Tc/5) + 32  = Tf

# farenheint = celcius_temp*(9/5) + 32
# print(farenheint)


# # Create a Data frame from stratch
# data_dict = {
#     "Students": ["Ammy", "James", "Angela"],
#     "Score": [76, 56, 65]

# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
    }

df = pandas.DataFrame(data_dict)
df.to_csv("colors_new_squirrels")

#colors = data.pivot_table(columns=["Primary Fur Color"], aggfunc="size")

#colors.to_csv("Squire_Colors.csv")



