
class Money :
    def __init__ (self, amount) :
        self.amount = amount
    
    def __eq__(self, money) :
        return self.amount == money.amount and self.__class__ == money.__class__


