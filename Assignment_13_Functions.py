# 1. Function with Parameters
def add(a, b):
    return a + b
print(add(5, 3))

# 2. Default Parameters
def greet(name, greeting="Hello"):
    print(greeting, name)
greet("Ali")
greet("Ali", "Hi")

# 3. Keyword Arguments Usage
def info(name, age, city):
    print(name, age, city)
info(age=25, city="Riyadh", name="Ali")

# 4. Using *args
def sum_all(*args):
    total = 0
    for x in args:
        total += x
    return total
print(sum_all(1, 2, 3, 4))

# 5. Using **kwargs
def print_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
print_info(name="Ali", age=25)

# 6. Flexible Function
def flexible(val):
    if isinstance(val, (int, float)):
        print(val * val)
    elif isinstance(val, str):
        print(val.upper())

flexible(5)
flexible("hello")

# 7. Advanced Function
def total_price(base, *items, discount=0, **details):
    price = base
    for item in items:
        price += item
    price -= discount
    print("Details:", details)
    return price
print(total_price(100, 20, 30, discount=10, note="VIP"))

# 8. Lambda Functions
add = lambda a, b: a + b
square = lambda x: x * x
print(add(2, 3))
print(square(4))

# 9. Map Function
nums = [1, 2, 3, 4]
sq = list(map(lambda x: x * x, nums))
print(sq)

# 10. Filter Function
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
