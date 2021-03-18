import unittest
from dollar import Dollar, Franc

class MoneyTest(unittest.TestCase) :
    def testMultiplication(self) :
        five = Dollar(5)
        self.assertEqual(Dollar(10).amount, five.times(2).amount) 
        self.assertEqual(Dollar(15).amount, five.times(3).amount)
    
    def testEquality(self) :
        dollar_five = Dollar(5)
        franc_five = Franc(5)
        self.assertTrue(dollar_five.equals(Dollar(5)))
        self.assertFalse(dollar_five.equals(Dollar(6)))
        self.assertTrue(franc_five.equals(Franc(5)))
        self.assertFalse(franc_five.equals(Franc(4)))   
        
    def testFrancMultiplication(self) :
        five = Franc(5)
        self.assertEqual(Franc(10).amount, five.times(2).amount) 
        self.assertEqual(Franc(15).amount, five.times(3).amount)
    
if __name__ == '__main__':
    unittest.main()
