# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()
    persons = json.loads(data)
    for person in persons:
        name = person["name"]
        age = person["age"]
        hobbies = (", ").join(person["hobbies"])
        print(f"{name} {age} years ({hobbies})")