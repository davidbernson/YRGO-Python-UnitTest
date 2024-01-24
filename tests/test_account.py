import unittest
from account import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account()

    def tearDown(self):
        self.account = None
