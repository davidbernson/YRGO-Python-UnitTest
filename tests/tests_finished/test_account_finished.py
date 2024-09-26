"""Unit tests for the account class"""
import unittest
from account import Account


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account()

    def test_createNewAccount(self):

        actual = self.account.get_balance()

        self.assertEqual(0, actual)

    def test_deposit100toAccount(self):
        self.account.deposit(100)

        actual = self.account.get_balance()

        self.assertEqual(100, actual)

    def test_withdraw50fromAccount(self):
        self.account.deposit(100)
        self.account.withdraw(50)

        actual = self.account.get_balance()

        self.assertEqual(50, actual)

    def test_apply4percentInterest(self):
        self.account.deposit(1000)
        self.account.apply_interest(4.0)

        actual = self.account.get_balance()

        self.assertEqual(1040, actual)

    def test_withdrawTooMuchRaisesException(self):
        self.account.deposit(50)

        with self.assertRaises(Exception) as asserter:
            self.account.withdraw(100)

        self.assertEqual("Not enough balance.", str(asserter.exception))

    def tearDown(self):
        self.account = None
