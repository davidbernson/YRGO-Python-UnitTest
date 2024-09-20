import unittest
import dicegame


class TestDiceGame(unittest.TestCase):

    def setUp(self):
        self.player = dicegame.Player("Tester McTesterson")

    def test_create_player(self):
        self.assertEqual("Tester McTesterson", self.player.name)

    def test_add_three_dice_to_player(self):
        self.player.add_die(6)
        self.player.add_die(6)
        self.player.add_die(6)

        self.assertEqual(3, self.player.get_number_of_dice())

    def test_roll_single_six_sided_die_25_times(self):
        die = dicegame.Die(6)

        for i in range(25):
            die.roll()

            with self.subTest(i=i):
                self.assertTrue(1 <= die.get_value() <= 6)

    def test_roll_three_dice_for_player(self):
        self.player.add_die(6)
        self.player.add_die(6)
        self.player.add_die(6)

        print("dice: " + str(self.player.get_number_of_dice()))

        for i in range(25):
            self.player.roll_dice()

            with self.subTest(i=i):
                self.assertTrue(3 <= self.player.get_dice_value() <= 18)

    def tearDown(self):
        self.player = None
