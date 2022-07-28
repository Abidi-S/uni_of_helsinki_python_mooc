# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        if payment >= 2.50:
            payment -= 2.50
            self.funds += 2.50
            self.lunches += 1
        return payment

    def eat_special(self, payment: float):
        if payment >= 4.30:
            payment -= 4.30
            self.funds += 4.30
            self.specials += 1
        return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        if card.balance >= 2.50:
            card.balance -= 2.50
            self.lunches += 1
            return True
        return False

    def eat_special_lunchcard(self, card: LunchCard):
        if card.balance >= 4.30:
            card.balance -= 4.30
            self.specials += 1
            return True
        return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        self.funds += amount
        card.balance += amount
        return card.balance
