class Department:
    def __init__(self, name, products):
        self.name = name
        self.products = products

    def __str__(self):
        output = f"{self.name}\n"
        if len(self.products) > 0:
            for product in self.products:
                output += f"  {product}\n"
        else:
            output += f"There are no products here\n"
        
        return output