"""Assignment 11: File Handling Operations in Python.

This module demonstrates various file handling operations including
reading, writing, copying, and appending files.
"""

import os
import datetime


# 1. Read a Text File
with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read())

# 2. Write to a Text File
data = input("Enter text: ")
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(data)

# 3. Read File Using File Object (Stream)
with open("sample.txt", "r", encoding="utf-8") as file:
    print("read():", file.read())

with open("sample.txt", "r", encoding="utf-8") as file:
    print("readline():", file.readline())

with open("sample.txt", "r", encoding="utf-8") as file:
    print("readlines():", file.readlines())

# 4. Random Access File Reading
with open("sample.txt", "r", encoding="utf-8") as file:
    file.seek(5)
    print(file.read())

# 5. Read from a Specific Index
with open("sample.txt", "r", encoding="utf-8") as file:
    file.seek(10)
    print(file.read(20))

# 6. Check File Permissions
print("Read:", os.access("sample.txt", os.R_OK))
print("Write:", os.access("sample.txt", os.W_OK))

# 7. Count Words, Lines, and Characters
with open("sample.txt", "r", encoding="utf-8") as file:
    lines = 0
    words = 0
    chars = 0
    for line in file:
        lines += 1
        words += len(line.split())
        chars += len(line)
    print("Lines:", lines, "Words:", words, "Chars:", chars)

# 8. Copy File Content
with open("sample.txt", "r", encoding="utf-8") as src:
    with open("copy.txt", "w", encoding="utf-8") as dst:
        dst.write(src.read())

# 9. Append Data with Timestamp
with open("log.txt", "a", encoding="utf-8") as file:
    file.write(str(datetime.datetime.now()) + " - New entry\n")
