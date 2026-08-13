"""Assignment 14: Exception Handling Examples.

This module demonstrates various exception handling techniques in Python
including custom exceptions, multiple except blocks, logging, and file operations.
"""

import logging

logging.basicConfig(filename="errors.log", level=logging.ERROR)


# 1. Generate an Exception
# print(10 / 0)

# 2. Handle the Exception
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# 3. Multiple Except Blocks
try:
    a = int(input("Enter a number: "))
    print(10 / a)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

# 4. Raise an Exception Manually
def check_age(age):
    """Check if age is 18 or above, raise ValueError if not."""
    if age < 18:
        raise ValueError("Age must be 18 or above")


try:
    check_age(16)
except ValueError as err:
    print("Handled:", err)

# 5. Function That Raises Exception
def always_fail():
    """Always raise a RuntimeError for demonstration."""
    raise RuntimeError("Always fails")


try:
    always_fail()
except RuntimeError as err:
    print("Handled:", err)

# 6. Create Your Own Exception
class InsufficientBalanceError(Exception):
    """Custom exception for insufficient balance scenarios."""
    pass


BALANCE = 100
WITHDRAW = 200
try:
    if WITHDRAW > BALANCE:
        raise InsufficientBalanceError("Not enough balance")
except InsufficientBalanceError as err:
    print(err)

# 7. Using finally
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Cleanup done")

# 8. File Not Found
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")

# 9. Type Error
try:
    print("5" + 5)
except TypeError:
    print("Type error occurred")

# 10. Attribute Error
try:
    x = 5
    x.append(1)
except AttributeError:
    print("Attribute error")

# 11. Index Error
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index out of range")

# 12. Use else Block
try:
    x = 5 / 1
except ZeroDivisionError:
    print("Error")
else:
    print("No error, result:", x)

# 13. Logging Errors
try:
    print(1 / 0)
except ZeroDivisionError as err:
    logging.error(str(err))

# 14. Input Validation System
while True:
    try:
        val = int(input("Enter a valid number: "))
        break
    except ValueError:
        print("Invalid, try again")
print("You entered:", val)
