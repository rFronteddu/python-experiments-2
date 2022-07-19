import csv
import os


def simple_file_example():
    # data.to_csv("new_data.csv")

    with open("weather_data.csv") as data_file:
        data = csv.reader(data_file)
        temperatures = []
        for row in data:
            if row[1] == "temp":
                continue
            temperatures.append(int(row[1]))
            print(row)
        print(temperatures)

    with open("my_file.txt", mode="w") as file:
        file.write("Test")

    # w write, a append
    with open("my_file.txt") as file:
        content = file.read()
        print(content)

    os.remove("my_file.txt")
