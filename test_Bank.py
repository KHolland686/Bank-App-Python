from BankUtility import *
from CoinCollector import *
from Account import *
from Bank import *
import unittest


class Test_BankUtility(unittest.TestCase):

    def test_isNumeric(self):
        self.assertIs(BankUtility.isNumeric('15'), True)
        self.assertIs(BankUtility.isNumeric('a'), False)

    def test_convertFromDollarsToCents(self):
        self.assertEqual(BankUtility.convertFromDollarsToCents(1.50), 150)
        self.assertIs(BankUtility.convertFromDollarsToCents('a'), False)
        self.assertEqual(BankUtility.convertFromDollarsToCents('1.50'),150)

    def test_generateRandomInteger(self):
        b=[4,5,6,7,8]
        self.assertIsInstance(BankUtility.generateRandomInteger(0,2), int)
        self.assertIn(BankUtility.generateRandomInteger(4,8),b)


class Test_CoinCollector(unittest.TestCase):

    def test_parseChange(self):
        self.assertEqual(CoinCollector.parseChange('WQP'), 126)
        self.assertEqual(CoinCollector.parseChange('X'), 0)
        self.assertIsInstance(CoinCollector.parseChange('H'), int)
        

class Test_Account(unittest.TestCase):

    def test_deposit(self):
        a = Account(Balance = 100)
        self.assertIs(a.deposit(-50), False)
        self.assertEqual(a.deposit(100), 200)

    def test_withdraw(self):
        b= Account(Balance=100.50)
        self.assertEqual(b.withdraw(50),50.50)
        self.assertIs(b.withdraw(500), False)

    def test_isValidPIN(self):
        c = Account(PIN = '6442')
        self.assertIs(c.isValidPIN('6442'), True)
        self.assertIs(c.isValidPIN('0123'), False)
        

class Test_Bank(unittest.TestCase):
    
    def test_addAccountToBank(self):
        d = Bank(Acc_Max=5) 
        e = Account(AccountNum= 1)
        f = Account(AccountNum= 2)
        g = Account(AccountNum= 3)
        h = Account(AccountNum= 4)
        i = Account(AccountNum= 5)
        j = Account(AccountNum= 6)
        d.addAccountToBank(f)
        d.addAccountToBank(g)
        d.addAccountToBank(h)
        d.addAccountToBank(i)

        self.assertIs(d.addAccountToBank(e), True)
        self.assertIs(d.addAccountToBank(j), False)
      

    def test_removeAccountFromBank(self):
        k = Bank()
        l = Account(AccountNum=7)
        m = Account(AccountNum=8)
        k.addAccountToBank(l)

        self.assertIsNone(k.removeAccountFromBank(l))
        self.assertIs(k.removeAccountFromBank(m), False)


    def test_findAccount(self):
        n = Bank()
        o = Account(AccountNum= 9)
        p = Account(AccountNum= 10)
        n.addAccountToBank(o)

        self.assertEqual(n.findAccount(9),o)
        self.assertIsNone(n.findAccount(p))
        

    def test_addMonthlyInterest(self):
        q = Bank()
        r = Account(Balance = 100)
        s = Account(Balance = 500)
        t = [100.83, 504.17]
        q.addAccountToBank(r)
        q.addAccountToBank(s)
        z = q.addMonthlyInterest(10)

        self.assertListEqual(z,t)
        self.assertEqual(z[0], 100.83)


if __name__ == '__main__':
    unittest.main()