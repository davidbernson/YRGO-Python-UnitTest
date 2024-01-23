import unittest
import dicegame

class TestDiceGame(unittest.TestCase):

    def setUp(self):
        self.player = dicegame.Player("Tester McTesterson")

    def test_create_player(self):
        self.assertEqual("Tester McTesterson", self.player.name)

    def test_addThreeDiceToPlayer(self):      
        self.player.add_die(6)
        self.player.add_die(6)
        self.player.add_die(6)

        self.assertEqual(3, self.player.get_number_of_dice())

    def test_rollSingleSixSidedDie25Times(self):
        self.die = dicegame.Die(6)
        
        for i in range(25):
            self.die.roll()

            with self.subTest(i=i):
                self.assertTrue(1 <= self.die.get_value() <= 6)

    def test_rollThreeDiceForPlayer(self):
        self.player.add_die(6)
        self.player.add_die(6)
        self.player.add_die(6)

        print("dice: " + str(self.player.get_number_of_dice()))

        for i in range(25):
            self.player.roll_dice()

            with self.subTest(i=i):
                print(self.player.get_dice_value())
                self.assertTrue(3 <= self.player.get_dice_value() <= 18)

    def tearDown(self):
        self.player = None