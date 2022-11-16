
import pandas

# if __name__ == '__main__':
#     with open("weather_data.csv") as weather_data:
#         data = csv.reader(weather_data)
#         temperatures = []
#         for row in data:
#             temp = row[1]
#             if temp.isdigit():
#                  temperatures.append(int(row[1]))
#
# data = pandas.read_csv("weather_data.csv")
# print(data.temp)
# max = data.temp.max()
# print(data[data.temp == max])

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Squirrels": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

df = pandas.DataFrame(squirrel_dict)
df.to_csv("squirrel_count.csv")