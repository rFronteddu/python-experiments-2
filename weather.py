import pandas


def analyze_weather():
    data = pandas.read_csv("weather_data.csv")
    print(data)
    print(type(data))

    temp_list = data["temp"].to_list()
    avg = sum(temp_list) / len(temp_list)
    print(data.temp)
    print(avg)
    print(data.temp.mean())
    print(data["temp"].max())

    print(data[data.day == "Monday"])
    print(data[data.temp == data.temp.max()])
    print("----------------")
    monday = data[data.day == "Monday"]
    monday_temp = int(monday.temp)
    monday_temp_f = monday_temp * 9 / 5 + 32
    print(f"Monday temp: {monday_temp_f}F")

    data_dict = {
        "students": ["Amy", "Lara", "Luca"],
        "scores": [75, 50, 60]
    }
    data2 = pandas.DataFrame(data_dict)
    print(data2)
