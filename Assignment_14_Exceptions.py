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
    if age < 18:
        raise Exception("Age must be 18 or above")
check_age(16)

# 5. Function That Raises Exception
def always_fail():
    raise Exception("Always fails")

try:
    always_fail()
except Exception as e:
    print("Handled:", e)

# 6. Create Your Own Exception
class InsufficientBalanceError(Exception):
    pass

balance = 100
try:
    withdraw = 200
    if withdraw > balance:
        raise InsufficientBalanceError("Not enough balance")
except InsufficientBalanceError as e:
    print(e)

# 7. Using finally
try:
    f = open("sample.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Cleanup done")

# 8. File Not Found
try:
    f = open("missing.txt", "r")
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
import logging
logging.basicConfig(filename="errors.log", level=logging.ERROR)
try:
    print(1 / 0)
except Exception as e:
    logging.error(str(e))

# 14. Input Validation System
while True:
    try:
        val = int(input("Enter a valid number: "))
        break
    except ValueError:
        print("Invalid, try again")
print("You entered:", val)
