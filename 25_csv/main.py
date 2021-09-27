# data = []

# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()

# print(data)

# import csv


# with open("./weather_data.csv") as data_file:
#      data = csv.reader(data_file)
#      temperatures = []
#      for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))

# print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# data_list = data["temp"].to_list()
# print(data_list)
# print(data["temp"].max())
# print(data.temp.max())
# print(data[data.day == "Monday"])


# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(monday_temp)

# new_list = [x for x in data.day if x == "Monday" ]
# print(new_list)

# import pandas

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# data_list = list(dict.fromkeys(data["Primary Fur Color"].to_list()))
# print(data_list)

