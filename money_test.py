from dollar import Dollar 

class MoneyTest :
    def testMultiplication(self) :
        five = Dollar(5)
        five.times(2)
        assert five.amount == 10 , "times method Error"

test = MoneyTest()
test.testMultiplication()