# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, name, number, balance):
        self.__name = name
        self.__number = number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            charge = self.__service_charge()
            self.__balance -= charge
        else:
            raise ValueError

    def withdraw(self, amount: float):
        if amount <= self.__balance:
            self.__balance -= amount
            charge = self.__service_charge()
            self.__balance -= charge
        else:
            raise ValueError

    def __service_charge(self):
        return 0.01 * self.__balance
