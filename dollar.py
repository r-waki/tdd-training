
class Dollar:
    def __init__ (self, multiplier) :
        self.multiplier = multiplier
        self.amount = 0

    def times(self, times) :
        self.amount = times * self.multiplier 
    