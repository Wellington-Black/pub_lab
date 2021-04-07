class Customer:

    def __init__(self, name, wallet, age, drunkenness_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness_level = drunkenness_level
        self.rejuvenation_level = 0

    def buy_drink(self, pub, drink):
        self.wallet -= drink.price
        pub.till += drink.price
        self.drunkenness_level += drink.alcohol_level
        for drink_name in pub.drinks:
            if drink_name == drink.name:
                pub.drinks[drink_name] -= 1


    def buy_food(self, pub, food):
        self.wallet -= food.price
        pub.till += food.price
        self.drunkenness_level -= food.rejuvenation_level
        self.rejuvenation_level += food.rejuvenation_level