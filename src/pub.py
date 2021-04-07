class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def check_age_and_drunkenness(self, customer):
        if customer.age >= 18 and customer.drunkenness_level < 10:
            customer.buy_drink
        else:
            return "Go home, we can't serve you"

