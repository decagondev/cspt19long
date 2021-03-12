from Product import Product

class Clothing(Product):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color

    def __str__(self):
        return f"{super().__str__()} comes in {self.color}"