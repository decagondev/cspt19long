from Department import Department

class Store:
    def __init__(self, name, departments):
        # attributes
        self.name = name
        self.departments = departments

    def __str__(self):
        output = f"{self.name}\n"

        for i, dept in enumerate(self.departments):
            output += f"  [{i + 1}]  {dept.name}\n"
        
        output += f"  [{len(self.departments) + 1}]  Exit"
        output += "\n"
        return output



my_store = Store("Bobs Emporium", [Department("Clothes"), Department("Weapons"), Department("Electronics")])

choice = 0
while choice != len(my_store.departments) + 1:
    print(my_store)
    choice = int(input("Please Choose a Floor: "))

    if choice == len(my_store.departments) + 1:
        print("Thanks for shopping!")
    elif choice > 0 and choice <= len(my_store.departments):
        print(f"{my_store.departments[choice - 1]}")
    else:
        print("Select a Valid Floor")

    