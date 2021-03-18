from money import Money

class Dollar(Money):
    def times(self, multiplier) :
        return Dollar(self.amount * multiplier)
    
    def equals(self, dollar) :
        return self.amount == dollar.amount

class Franc(Money):

    def times(self, multiplier) :
        return Franc(self.amount * multiplier)
    
    def equals(self, dollar) :
        return self.amount == dollar.amount

