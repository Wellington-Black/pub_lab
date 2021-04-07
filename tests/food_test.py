import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food_1 = Food("Sandwich", 5, 1)
        self.food_2 = Food("Pizza", 10, 5)
    
    def test_food_has_name(self):
        self.assertEqual("Pizza", self.food_2.name)

    def test_food_has_price(self):
        self.assertEqual(10, self.food_2.price)

    def test_food_has_rejuvenation_level(self):
        self.assertEqual(5, self.food_2.rejuvenation_level)