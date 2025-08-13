import pandas as pd
import sys

flyers = pd.read_csv("./my_data.csv")

# Method that takes in an id and returns wether they are an instructor
def is_instructor(id):
    result = flyers.loc[flyers["id"] == id, "instructor"].values[0]
    if result == 1: 
        return "They are an Instructor!"
    return "Not Instructor!"

# Method that takes in an id and returns their flying level
def flyer_level(id):
    result = flyers.loc[flyers["id"] == id, "level"].values[0]
    return f"Their flying level is {result}!"

# Method that takes in an id and returns wether they are current or not
def is_current(id):
    result = flyers.loc[flyers["id"] == id, "current"].values[0]
    if result == 1: 
        return "They are current!"
    return "Not current!"

id_input = int(input("prompt: "))
print(is_instructor(id_input))
print(flyer_level(id_input))
print(is_current(id_input))