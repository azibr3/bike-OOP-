class Bike:
    def __init__(self, description, cost, sale_price, condition):
        self.__description = description
        self.__cost = cost
        self.__sale_price = sale_price
        self.__condition = condition
        self.__sold = False

    def get_description(self):
        return self.__description
    def get_cost(self):
        return self.__cost
    def get_sale_price(self):
        return self.__sale_price
    def get_condition(self):
        return self.__condition
    def get_sold(self):
        return self.__sold

    def update_sale_price(self, sale_price):
        if self.__sold == True:
            print('Action not allowed, Bike has already been sold')
        else:
            self.__sale_price = sale_price

    def sell(self):
            self.__sold = True

bike1= Bike ('Univega Alpina, orange', cost=100, sale_price=500, condition=0.5)

bike1.update_sale_price(350)

bike1.sell()

print(f"The final sale price of the bike is: {bike1.get_sale_price()}")