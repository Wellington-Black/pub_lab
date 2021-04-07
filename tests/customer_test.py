import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("Bruce", 50)
        self.customer_2 = Customer("Linda", 100)

    def test_buy_drink(self):

        customer = Customer("Bruce", 50)
        drink = Drink("beer", 5)
        self.assertEqual(45,customer.wallet)
        self.assertEqual(105, pub.till)
        



        #  def buy_drink(self, drink):
        # self.wallet -= drink.price
        # pub.till += drink.price