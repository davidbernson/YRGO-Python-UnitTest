import unittest
import dicegame


class TestDiceGame(unittest.TestCase):

    def setUp(self):
        self.player = dicegame.Player("Tester McTesterson")

    def test_create_player(self):
        pass

    def test_addThreeDiceToPlayer_AssertPlayerHas3Dice(self):      
        pass

    def test_rollSingleSixSidedDie25Times_AssertResultBetween1And6(self):
        pass

    def test_rollThreeDiceForPlayer_AssertResultBetween3And18(self):
        pass

    def tearDown(self):
        self.player = None