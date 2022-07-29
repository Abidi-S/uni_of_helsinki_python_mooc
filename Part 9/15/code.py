# Write your solution here:
class Item:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    def __str__(self):
        return f"{self.name()} ({self.weight()} kg)"

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

class Suitcase:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__items = []

    def __str__(self):
        weight = self.weight()
        if len(self.__items) == 1:
            return f"{len(self.__items)} item ({weight} kg)"
        return f"{len(self.__items)} items ({weight} kg)"

    def add_item(self, item: Item):
        weight = self.weight()

        if (weight + item.weight()) <= self.max_weight:
            self.__items.append(item)

    def weight(self):
        weight = 0
        for item in self.__items:
            weight += item.weight()
        return weight

    def print_items(self):
        for item in self.__items:
            print(item)

    def heaviest_item(self):
        weight = 0
        heaviest = ""
        if len(self.__items) > 0:
            for item in self.__items:
                if item.weight() > weight:
                    weight = item.weight()
                    heaviest = item
            return heaviest
        return None

class CargoHold:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__cargo = []

    def __str__(self):
        weight = self.__cargo_weight()
        if len(self.__cargo) == 1:
            return f"{len(self.__cargo)} suitcase, space for {self.max_weight - weight} kg"
        return f"{len(self.__cargo)} suitcases, space for {self.max_weight - weight} kg"

    def add_suitcase(self, suitcase: Suitcase):
        weight = self.__cargo_weight()
        if suitcase.weight() + weight <= self.max_weight:
            self.__cargo.append(suitcase)

    def __cargo_weight(self):
        weight = 0
        for suitcase in self.__cargo:
            weight += suitcase.weight()
        return weight

    def print_items(self):
        for suitcase in self.__cargo:
            (suitcase.print_items())
