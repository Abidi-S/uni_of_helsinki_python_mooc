# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"

class Room:
    def __init__(self):
        self.people = []

    def add(self, person: Person):
        self.people.append(person)

    def is_empty(self):
        return (len(self.people) == 0)

    def contents(self):
        total_height = 0
        for person in self.people:
            total_height += person.height
        return total_height

    def print_contents(self):
        total_height = self.contents()
        print(f"There are {len(self.people)} persons in the room, and their combined height is {total_height} cm")
        for person in self.people:
            print(person)

    def tallest(self):
        tallest = 0
        for person in self.people:
            if person.height > tallest:
                tallest = person.height
        return tallest

    def shortest(self):
        if (len(self.people) > 0):
            tallest = self.tallest()
            shortest = ""
            for person in self.people:
                if person.height <= tallest:
                    tallest = person.height
                    shortest = person
            return shortest
        return None

    def remove_shortest(self):
        shortest = self.shortest()
        if shortest:
            removed = self.people.pop(self.people.index(shortest))
            return removed
        return None
