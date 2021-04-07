class Customer:

    def __init__(self, name, wallet, age, drunkenness_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness_level = drunkenness_level

    def buy_drink(self, pub, drink):
        self.wallet -= drink.price
        pub.till += drink.price
        self.drunkenness_level += drink.alcohol_level