# class NameOfClass:

# class (Blueprint)
class Animal:
    def __init__(self, name, colors):
        self.name = name
        self.age = 1
        self.fav_colors = colors

    def __str__(self):
        output = f"My name is {self.name} and I am {self.age} years old.\n"
        output += "My Favorite Colors Are:"
        for col in self.fav_colors:
            output += f" {col} "
        output += "\n"

        return output

my_colors = ["Red", "Yellow", "Cyan"]
dog = Animal("Dave", my_colors)
cat = Animal("Sue", ["Orange", "Blue"])
print(dog)
print(cat)