def update_sale_price(bike, sale_price):
    if bike['sold'] == True:
        print('Action not allowed, Bike has already been sold')
    else:
        bike['sale_price'] = sale_price

def sell(bike):
    bike['sold'] = True

def create_bike(description, cost, sale_price, condition):
    return {
        'description': description,
        'cost': cost,
        'sale_price': sale_price,
        'condition': condition,
        'sold': False
    }

bike1 = create_bike('Univega Alpina, orange', cost=100, sale_price=500, condition=0.5)
update_sale_price(bike1, 350)
sell(bike1)