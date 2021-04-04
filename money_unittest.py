import unittest
from money import Money, Dollar, Franc


class MoneyTest(unittest.TestCase):
    def testMultiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10).amount, five.times(2).amount)
        self.assertEqual(Money.dollar(15).amount, five.times(3).amount)

    def testEquality(self):
        dollar_five = Money.dollar(5)
        franc_five = Money.franc(5)
        self.assertTrue(dollar_five == Money.dollar(5))
        self.assertFalse(dollar_five == Money.dollar(6))
        self.assertTrue(franc_five == Money.franc(5))
        self.assertFalse(franc_five == Money.franc(4))
        self.assertFalse(dollar_five == franc_five)

    def testFrancMultiplication(self):
        five = Money.franc(5)
        self.assertEqual(Franc(10).amount, five.times(2).amount)
        self.assertEqual(Franc(15).amount, five.times(3).amount)

    def testCurrency(self):
        self.assertEqual("USD", Money.dollar(5).currency())
        self.assertEqual("CHF", Money.franc(4).currency())
        self.assertNotEqual("USD", Money.franc(6).currency())


if __name__ == '__main__':
    unittest.main()
