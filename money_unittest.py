import unittest
from dollar import Dollar 

class MoneyTest(unittest.TestCase) :
    def testMultiplication(self) :
        five = Dollar(5)
        five.times(2)
        self.assertEqual(five.amount, 10) 

if __name__ == '__main__':
    unittest.main()