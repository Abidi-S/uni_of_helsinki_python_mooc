
# WRITE YOUR SOLUTION HERE:
#Note! Do not change the class Person!

class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class BabyCentre:
    def __init__(self):
        self.number_of_weigh_ins = 0

    def weigh(self, person: Person):
        # return the weight of the person passed as an argument
        self.number_of_weigh_ins += 1
        return person.weight

    def feed(self, person: Person):
        person.weight += 1

    def weigh_ins(self):
        return self.number_of_weigh_ins