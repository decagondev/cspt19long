class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"<Person: {self.name}, {self.age}>"
    
dave = Person("Dave", 67)
dave2 = { "name": "Dave", "age": 67 }
ste = Person("Steve", 22)
bob = Person("Bob", 102)

people = [
    dave,
    ste,
    bob
]

# for person in people:
#     print(person.name)

a = [person for person in people if person.name[0] == 'D']
for thing in a:
    print(thing)
print(a)