import dollar 

class MoneyTest :
    def testMultiplication(self) :
        five = Dollar(5)
        five.times(2)
        assert five.amount == 10 , "Error"

test = MoneyTest()
test.testMultiplication()