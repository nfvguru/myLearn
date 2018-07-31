#!/usr/bin/env python3

class Person():
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"

p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())

# bowl has-a scoop
# employee is-a person

class Employee(Person):
    def __init__(self, name, id_number):
        # Person.__init__(self, name)
        super().__init__(name)
        self.id_number = id_number

e1 = Employee('emp1', 1)
e2 = Employee('emp2', 2)

print(e1.greet())
print(e2.greet())
