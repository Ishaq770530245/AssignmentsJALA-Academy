# 1. Default and Parameterized Constructors
class Demo:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Default constructor")
        elif b is None:
            print("One argument:", a)
        else:
            print("Two arguments:", a, b)

d1 = Demo()
d2 = Demo(10)
d3 = Demo(10, 20)

# 2. Calling Parent Constructor
class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")

c = Child()

# 3. Simulating Access Levels
class Access:
    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"

obj = Access()
print(obj.public)
print(obj._protected)
print(obj._Access__private)

# 4. Constructor Attributes Concept
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

c = Car("Toyota", "Corolla")
print(c.brand, c.model)

# 5. Using __str__() for Better Output
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

p = Person("Ali", 25)
print(p)

# 6. Constructor with *args
class ArgsDemo:
    def __init__(self, *args):
        self.values = args
        print(self.values)

a = ArgsDemo(1, 2, 3, 4)

# 7. Real-World Example
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.id = emp_id
        self.salary = salary
    def __str__(self):
        return f"{self.name} | {self.id} | {self.salary}"

e1 = Employee("Ali", 101, 5000)
e2 = Employee("Sara", 102, 6000)
print(e1)
print(e2)
