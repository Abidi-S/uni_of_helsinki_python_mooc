class Person:
    def __init__(self, name):
        self.__name = name
        self.__numbers = []
        self.__address = [] #RECONSIDER


    def __repr__(self):
        return f"{self.numbers()} {self.address()}"
# UNNECESSARY

    def name(self):
        return self.__name

    def numbers(self):
        return self.__numbers

    def address(self):
        if len(self.__address) == 0:
            return None
        return self.__address[0]

    def add_number(self, number: str):
        self.__numbers.append(number)

    def add_address(self, address: str):
        self.__address.append(address)

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

    def get_entry(self, name: str):
        numbers = None
        address = None
        if not name in self.__persons:
            return None

        if len(self.__persons[name].numbers()) != 0:
            numbers = self.__persons[name].numbers()

        if self.__persons[name].address() != None:
            address = self.__persons[name].address()

        return numbers, address
# REWRITE HOT GARBAGE GET ENTRy

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        # below is surprisinly, and unfortunately, largely identical to mode solution
        name = input("name: ")
        if self.__phonebook.get_entry(name) != None:
            numbers, addresses = self.__phonebook.get_entry(name)
        else:
            numbers = None
            addresses = None

        if addresses != None:
            print(addresses)
        else:
            print("address unknown")

        if numbers != None:
            for number in numbers:
                print(number)
        else:
            print("number unknown")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

# phonebook = PhoneBook()
# phonebook.add_address("Eric", "cuckoo")
# print(phonebook.get_entry("Eric"))
# print(phonebook.get_entry("Emily"))