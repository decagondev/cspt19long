class Department:
    def __init__(self, name): # , products):
        self.name = name

    def __str__(self):
        return f"No products in {self.name}"