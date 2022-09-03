import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(data["Primary Fur Color"])
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]
print(len(gray_squirrels))
print(len(cinnamon_squirrels))
print(len(black_squirrels))

fur_color = {
             "Fur Color": ["grey", "cinnamon", "black"],
             "count": [2473, 392, 103]
             }
fur_data = pandas.DataFrame(fur_color)
fur_data.to_csv("fur_color")

