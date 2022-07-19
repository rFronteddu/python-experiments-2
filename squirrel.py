import pandas


# Read the squirrel csv and create another csv with the primary fur color count
def analyze_squirrel():
    data = pandas.read_csv("squirrel_count.csv")
    fur_color_list = data["Primary Fur Color"].to_list()
    fur_dict = {}
    for color_element in fur_color_list:
        if color_element in fur_dict:
            fur_dict[color_element] = fur_dict[color_element] + 1
        else:
            fur_dict[color_element] = 1
    print(fur_dict)

    counts = []
    for color in fur_dict.keys():
        counts.append(fur_dict[color])

    out_dict = {
        "Fur Color": fur_dict.keys(),
        "Count": counts
    }

    pandas.DataFrame(out_dict).to_csv("squirrel_count_test.csv")


# Same thing but using a set and more pandas facilities
def analyze_squirrel2():
    data = pandas.read_csv("squirrel_count.csv")
    fur_color_list = data["Primary Fur Color"].to_list()
    fur_set = set()
    for color_element in fur_color_list:
        fur_set.add(color_element)
    counts = []
    for color in fur_set:
        counts.append(len(data[data["Primary Fur Color"] == color]))
    out_dict = {
        "Fur Color": list(fur_set),
        "Count": counts
    }
    pandas.DataFrame(out_dict).to_csv("squirrel_count_test2.csv")
