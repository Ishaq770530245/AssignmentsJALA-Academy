"""Assignment 13: Functions Examples in Python.

This module demonstrates various function concepts including parameters,
default values, *args, **kwargs, lambda, map, and filter.
"""


# 1. Function with Parameters
def add(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2


print(add(5, 3))


# 2. Default Parameters
def greet(name, greeting="Hello"):
    """Greet a person with optional custom greeting."""
    print(greeting, name)


greet("Ali")
greet("Ali", "Hi")


# 3. Keyword Arguments Usage
def info(name, age, city):
    """Print person information using keyword arguments."""
    print(name, age, city)


info(age=25, city="Riyadh", name="Ali")


# 4. Using *args
def sum_all(*args):
    """Return the sum of all provided arguments."""
    total = 0
    for x in args:
        total += x
    return total


print(sum_all(1, 2, 3, 4))


# 5. Using **kwargs
def print_info(**kwargs):
    """Print key-value pairs from keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Ali", age=25)


# 6. Flexible Function
def flexible(val):
    """Handle different input types flexibly."""
    if isinstance(val, (int, float)):
        print(val * val)
    elif isinstance(val, str):
        print(val.upper())


flexible(5)
flexible("hello")


# 7. Advanced Function
def total_price(base, *items, discount=0, **details):
    """Calculate total price with items, discount, and extra details."""
    price = base
    for item in items:
        price += item
    price -= discount
    print("Details:", details)
    return price


print(total_price(100, 20, 30, discount=10, note="VIP"))


# 8. Lambda Functions
def add_lambda(num1, num2):
    """Add two numbers."""
    return num1 + num2


def square_lambda(x):
    """Return the square of a number."""
    return x * x


print(add_lambda(2, 3))
print(square_lambda(4))


# 9. Map Function
nums = [1, 2, 3, 4]
sq = list(map(lambda x: x * x, nums))
print(sq)


# 10. Filter Function
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
