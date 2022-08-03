# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02} eur"

    def __eq__(self, another):
        return (self._euros == another._euros and self._cents == another._cents)

    def __gt__(self, another):
        if self._euros == another._euros:
            return self._cents > another._cents
        return (self._euros > another._euros)

    def __lt__(self, another):
        if self._euros == another._euros:
            return self._cents < another._cents
        return (self._euros < another._euros)

    def __ne__(self, another):
        if self._euros == another._euros:
            return self._cents != another._cents
        return (self._euros != another._euros)

    def __add__(self, another):
        more_monies = Money(0, 0)
        more_monies._euros = self._euros + another._euros
        more_monies._cents = self._cents + another._cents
        if more_monies._cents >= 100:
            more_monies._euros += more_monies._cents//100
            more_monies._cents %= 100

        return more_monies

    def __sub__(self, another):
        less_monies = Money(0,0)
        a = self._euros*100 + self._cents
        b = another._euros*100 + another._cents
        remaining = a - b
        if remaining < 0:
            raise ValueError
        less_monies._euros = remaining//100
        less_monies._cents = remaining%100
        return less_monies

# e1 = Money(4, 5)
# e2 = Money(2, 95)

# e3 = e1 + e2
# e4 = e1 - e2

# print(e3)
# print(e4)

# e5 = e2-e1