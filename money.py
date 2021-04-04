from abc import ABCMeta


class Money(metaclass=ABCMeta):
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, money):
        return (self.amount == money.amount
                and self.__class__ == money.__class__)

    def dollar(amount):
        return Dollar(amount)

    def franc(amount):
        return Franc(amount)


class Dollar(Money):
    def times(self, multiplier):
        return Money(self.amount * multiplier)

#    def currency(self):
#        return "USD"


class Franc(Money):
    def times(self, multiplier):
        return Money(self.amount * multiplier)

#    def currency(self):
#        return "CHF"
