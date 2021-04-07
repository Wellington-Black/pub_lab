import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("beer", 5, 2)
        self.drink_2 = Drink("Ginandtonic", 10, 5)

    def test_drink_has_name(self):
        self.assertEqual("beer", self.drink_1.name)

    def test_drink_has_price(self):
        self.assertEqual(5, self.drink_1.price)

    def test_drink_has_alcohol_level(self):
        self.assertEqual(2, self.drink_1.alcohol_level)    