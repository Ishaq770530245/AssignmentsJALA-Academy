"""Assignment 12: Constructors and Class Attributes in Python.

This module demonstrates various constructor patterns including default,
parameterized, parent class calling, access levels, and real-world examples.
"""


# 1. Default and Parameterized Constructors
class Demo:
    """Demonstrate default and parameterized constructors."""

    def __init__(self, first=None, second=None):
        if first is None and second is None:
            print("Default constructor")
        elif second is None:
            print("One argument:", first)
        else:
            print("Two arguments:", first, second)


d1 = Demo()
d2 = Demo(10)
d3 = Demo(10, 20)


# 2. Calling Parent Constructor
class Parent:
    """Parent class with constructor."""

    def __init__(self):
        print("Parent constructor")


class Child(Parent):
    """Child class calling parent constructor."""

    def __init__(self):
        super().__init__()
        print("Child constructor")


c = Child()


# 3. Simulating Access Levels
class Access:
    """Demonstrate public, protected, and private access levels."""

    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"


obj = Access()
print(obj.public)
print(obj._protected)
# pylint: disable=protected-access
print(obj._Access__private)
# pylint: enable=protected-access


# 4. Constructor Attributes Concept
class Car:
    """Car class demonstrating constructor attributes."""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car = Car("Toyota", "Corolla")
print(car.brand, car.model)


# 5. Using __str__() for Better Output
class Person:
    """Person class with string representation."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


p = Person("Ali", 25)
print(p)


# 6. Constructor with *args
class ArgsDemo:
    """Demonstrate constructor with variable arguments."""

    def __init__(self, *args):
        self.values = args
        print(self.values)


args_demo = ArgsDemo(1, 2, 3, 4)


# 7. Real-World Example
class Employee:
    """Employee class with constructor and string representation."""

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def __str__(self):
        return f"{self.name} | {self.emp_id} | {self.salary}"


e1 = Employee("Ali", 101, 5000)
e2 = Employee("Sara", 102, 6000)
print(e1)
print(e2)
