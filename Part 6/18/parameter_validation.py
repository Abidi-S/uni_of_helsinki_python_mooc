# Write your solution here
def new_person(name: str, age: int):
    if (age < 0) or (age > 150) or len(name) > 40 or len(name) <= 0 or len(name.split(" ")) < 2:
        raise ValueError("The parameters passed to function are not valid")
    new_tup = (name, age)
    return new_tup