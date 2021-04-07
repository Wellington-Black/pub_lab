import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub
from src.food import Food

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Bruce", 50, 30, 0)
        self.pub = Pub("The Prancing Pony", 100)
        self.drink = Drink("Beer", 5, 2)
        self.food_2 = Food("Pizza", 10, 5)
        self.pub.drinks = {
            "Beer": 20,
            "Ginandtonic": 10,
            "Rum": 40,
            "Vodka": 10
        }
        #self.customer_2 = Customer("Linda", 100, 17)

    def test_customer_has_name(self):
        self.assertEqual("Bruce", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(30, self.customer.age)

    def test_customer_has_drunkenness_level(self):
        self.assertEqual(0, self.customer.drunkenness_level)

    def test_buy_drink(self):
        self.customer.buy_drink(self.pub, self.drink)
        self.assertEqual(45, self.customer.wallet)
        self.assertEqual(105, self.pub.till)
        self.assertEqual(2, self.customer.drunkenness_level)
        self.assertEqual(19, self.pub.drinks["Beer"])

    def test_buy_food(self):
        self.customer.buy_food(self.pub, self.food_2)
        self.assertEqual(40, self.customer.wallet)
        self.assertEqual(110, self.pub.till)
        self.assertEqual(5, self.customer.rejuvenation_level)
        self.assertEqual(-5, self.customer.drunkenness_level)
    