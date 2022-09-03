#import csv
#with open('weather_data.csv') as data_files:
#    data = csv.reader(data_files)
#    temperature = []
#    for row in data:
#        if row[1] != "temp":
#            temperature.append(int(row[1]))
#
#print(temperature)
import pandas
data = pandas.read_csv("weather_data.csv")
#print(data["temp"])
data_dic = data.to_dict()
data_list = data["temp"].to_list()
total = 0
for num in data_list:
    total += num
average = total/len(data_list)
#......or
ave = sum(data_list)/len(data_list)
print(average)
print(ave)
#......or by using pandas liberary we get
#print(data["temp"].mean())
#print(data["temp"].max())
#Get data in columns
#print(data["condition"])
#print(data.condition)
#Get data in Row
#print(data[data.day == "Sunday"])
#print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print()
monday_temp = int(monday.temp)
temperature = monday_temp*1.8 + 32
print(temperature)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

data = pandas.read_csv("weather_data.csv")
print(type(data["temp"]))