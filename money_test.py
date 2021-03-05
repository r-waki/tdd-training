from dollar import Dollar 

class MoneyTest :
    def testMultiplication(self) :
        five = Dollar(5)
        product = five.times(2)
        assert product.amount == 10 , "times func(2) method Error"
        product = five.times(3)
        assert product.amount == 15 , "times func(3) method Error"

test = MoneyTest()
test.testMultiplication()