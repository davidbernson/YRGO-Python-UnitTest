import unittest
from account import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account()

    def test_newlyCreatedAccountHas0Balance(self):
        assert self.account.get_balance() == 0

    def test_deposit100ToAccount(self):
        self.account.deposit(100)

        assert self.account.get_balance() == 100

    def test_withdraw50FromAccountWith100(self):
        self.account.deposit(100)
        self.account.withdraw(50)

        assert self.account.get_balance() == 50

    def test_withdraw100FromAccountWith50ShouldThrowException(self):
        self.account.deposit(50)

        with self.assertRaises(Exception) as cm:
            self.account.withdraw(100)

        self.assertEqual(str(cm.exception), "Not enough balance.")

    def test_apply4PercentInterestToAccountWith1000(self):
        self.account.deposit(1000)
        self.account.apply_interest(4.0)

        assert self.account.get_balance() == 1040

    def tearDown(self):
        self.account = None
