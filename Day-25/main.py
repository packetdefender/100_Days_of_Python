# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     tempreatures = []
#     for row in data:
#         if row[1] != "temp":
#             tempreatures.append(int(row[1]))
#     print(tempreatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()

# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# print(data['temp'].max())
#
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# print((int(monday.temp) * 9/5) + 32)

#Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("student_scores.csv")