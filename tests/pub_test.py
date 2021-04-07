import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100)
        self.customer = Customer("Bruce", 50, 30, 0)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_check_age_and_drunkenness(self):
        self.pub.check_age_and_drunkenness(self.customer)
        # self.customer.age >= 18
        self.assertEqual(30, self.customer.age)  
        self.assertEqual(0, self.customer.drunkenness_level)  

    def test_drunkenness_level(self):
        self.assertEqual(0, self.customer.drunkenness_level)

        # def test_buy_drink(self):
        # customer = Customer("Bruce", 50, 30)
        # drink = Drink("beer", 5)
        # customer.buy_drink(self.pub,drink)
        # self.assertEqual(45,customer.wallet)
        # self.assertEqual(105, self.pub.till)