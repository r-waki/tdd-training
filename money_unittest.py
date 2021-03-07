import unittest
from dollar import Dollar 

class MoneyTest(unittest.TestCase) :
    def testMultiplication(self) :
        five = Dollar(5)
        self.assertEqual(Dollar(10).amount, five.times(2).amount) 
        self.assertEqual(Dollar(15).amount, five.times(3).amount)
    
    def testEquality(self) :
        five = Dollar(5)
        self.assertTrue(five.equals(Dollar(5)))
        self.assertFalse(five.equals(Dollar(6)))

if __name__ == '__main__':
    unittest.main()
