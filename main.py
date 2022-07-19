from file_example import simple_file_example
from nato import nato_exercise
from squirrel import analyze_squirrel, analyze_squirrel2
from weather import analyze_weather

# simple_file_example()
# analyze_weather()
# analyze_squirrel2()
nato_exercise()
# list comprehension:
# new_list = [new_item for item in list] for example: [n + 1 for n in list] n + 1 is
# the rule that will use each element n in list to create a new el in new list.
# you can also do [new_item for item in list if test] to only add if test on item is passed

# Something similar can be done for dictionaries:
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}