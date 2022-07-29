# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"

class Box:
    def __init__(self):
        self.items = []

    def add_present(self, present: Present):
        self.items.append(present)
    def total_weight(self):
        total = 0
        for item in self.items:
            total += item.weight
        return total