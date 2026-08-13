# 1. Create a Dictionary
students = {101: "Ali", 102: "Sara", 103: "Omar", 104: "Lina", 105: "Khaled"}

# 1.1 Add New Entries
students[106] = "Nora"

# 1.2 Update Existing Values
students[101] = "Ahmed"

# 1.3 Access Values
print(students[101])
for v in students.values():
    print(v)

# 1.4 Iterate Through Dictionary
for k, v in students.items():
    print(k, v)

# 1.5 Print Only Keys
for k in students.keys():
    print(k)

# 1.6 Print Only Values
for v in students.values():
    print(v)

# 1.7 Create a Nested Dictionary
nested = {
    101: {"name": "abc", "age": 22},
    102: {"name": "xyz", "age": 21}
}

# 1.8 Access Nested Values
print(nested[101]["name"])
print(nested[101]["age"])

# 1.9 Delete Elements
del students[101]
students.pop(102)
students.popitem()

# 2. Check Key Existence
print(103 in students)

# 3. Count Entries
print(len(students))

# 4. Merge Two Dictionaries
dict1 = {1: "A", 2: "B"}
dict2 = {3: "C", 4: "D"}
merged = {}
for k, v in dict1.items():
    merged[k] = v
for k, v in dict2.items():
    merged[k] = v
print(merged)

# 5. Dictionary Comprehension
squares = {x: x * x for x in range(1, 6)}
print(squares)

# 6. Reverse Dictionary
original = {1: "A", 2: "B", 3: "C"}
reversed_dict = {}
for k, v in original.items():
    reversed_dict[v] = k
print(reversed_dict)
