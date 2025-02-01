class Product:
    def __init__(self,name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f'Product name: {self.name}, Price: {self.price}, Stock: {self.stock}')
    def update_price(self, new_price):
        self.price=new_price
        print(f'Updating price to {new_price}...')
        print(f'New Price : {new_price}...')
    def update_stock(self, new_stock):
        self.stock= new_stock
        print(f'Updating price to {new_stock}...')
        print(f'New Stock : {new_stock}...')

product = Product('Laptop', 1000.0, 50)
product.display_info()
product.update_price(120.50)
product.update_stock(20)