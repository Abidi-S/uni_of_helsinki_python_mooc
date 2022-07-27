# Write your solution here:
class Person:
    def __init__(self, name):
        self.name = name

    def return_first_name(self):
        names = self.name.split(" ")
        return names[0]

    def return_last_name(self):
        names = self.name.split(" ")
        return names[1]