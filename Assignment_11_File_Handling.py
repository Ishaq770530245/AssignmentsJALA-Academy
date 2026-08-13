# 1. Read a Text File
f = open("sample.txt", "r")
print(f.read())
f.close()

# 2. Write to a Text File
data = input("Enter text: ")
f = open("output.txt", "w")
f.write(data)
f.close()

# 3. Read File Using File Object (Stream)
f = open("sample.txt", "r")
print("read():", f.read())
f.close()

f = open("sample.txt", "r")
print("readline():", f.readline())
f.close()

f = open("sample.txt", "r")
print("readlines():", f.readlines())
f.close()

# 4. Random Access File Reading
f = open("sample.txt", "r")
f.seek(5)
print(f.read())
f.close()

# 5. Read from a Specific Index
f = open("sample.txt", "r")
f.seek(10)
print(f.read(20))
f.close()

# 6. Check File Permissions
import os
print("Read:", os.access("sample.txt", os.R_OK))
print("Write:", os.access("sample.txt", os.W_OK))

# 7. Count Words, Lines, and Characters
f = open("sample.txt", "r")
lines = 0
words = 0
chars = 0
for line in f:
    lines += 1
    words += len(line.split())
    chars += len(line)
f.close()
print("Lines:", lines, "Words:", words, "Chars:", chars)

# 8. Copy File Content
src = open("sample.txt", "r")
dst = open("copy.txt", "w")
dst.write(src.read())
src.close()
dst.close()

# 9. Append Data with Timestamp
import datetime
f = open("log.txt", "a")
f.write(str(datetime.datetime.now()) + " - New entry\n")
f.close()
