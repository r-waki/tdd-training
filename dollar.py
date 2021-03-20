from money import Money

class Dollar(Money):
    def times(self, multiplier) :
        return Money(self.amount * multiplier)
    
class Franc(Money):

    def times(self, multiplier) :
        return Money(self.amount * multiplier)
