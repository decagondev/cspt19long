class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def purchase(self):
        pass
    
    def __str__(self):
        return f"{self.name} costs ${self.price}"