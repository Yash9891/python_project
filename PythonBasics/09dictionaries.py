# =============================================================================
#  PYTHON DICTIONARIES — Complete Reference Guide
#  Author  : Yash
#  Purpose : Understand dictionaries in Python from scratch
# =============================================================================


# -----------------------------------------------------------------------------
# WHAT IS A DICTIONARY?
# -----------------------------------------------------------------------------
# A dictionary stores data as KEY : VALUE pairs.
# Think of it like a real dictionary: you look up a WORD (key) to get its
# MEANING (value).
#
# Rules:
#   • Keys must be UNIQUE — duplicate keys overwrite the earlier value
#   • Keys must be IMMUTABLE — strings, numbers, tuples (NOT lists)
#   • Values can be ANYTHING — int, str, list, dict, function, etc.
#   • Dictionaries are ORDERED — insertion order preserved (Python 3.7+)
#   • Dictionaries are MUTABLE — you can add, change, remove pairs
#   • NO indexing — access values by KEY, not by position
#
#  Property        Dictionary
#  ─────────────   ──────────────────────────────────────────────────────────
#  Ordered         Yes (Python 3.7+)
#  Mutable         Yes
#  Duplicates      Keys: No  |  Values: Yes
#  Indexing        By KEY, not by position (no d[0])
#  Syntax          {"key": value}
#  Best for        Labelled data, fast key-based lookup


# =============================================================================
# 1. CREATING DICTIONARIES
# =============================================================================

# ── Empty dictionary ──────────────────────────────────────────────────────────
dec = {}
print(type(dec))    # <class 'dict'>
# ⚠️  {} gives dict, not set. Use set() for empty set.

# ── Basic dictionary ──────────────────────────────────────────────────────────
person = {
    "name"  : ["Prashant", "Yash"],   # value is a LIST
    "age"   : 23,
    "city"  : "Pune",
    "salary": 455657
}
print(person)
# {'name': ['Prashant', 'Yash'], 'age': 23, 'city': 'Pune', 'salary': 455657}

# ── Keys can be numbers too ───────────────────────────────────────────────────
numbers = {
    1: "Yash",
    2: "Two",
    3: ["Three", "Pop", "List", 45.6]   # value is a mixed list
}
print(numbers[1])       # Yash
print(numbers[3])       # ['Three', 'Pop', 'List', 45.6]
print(numbers[3][1:])   # ['Pop', 'List', 45.6]  — slice the list value

# ── Duplicate keys — LAST value wins ─────────────────────────────────────────
dup = {"name": "Yash", "name": "Prashant"}
print(dup)   # {'name': 'Prashant'}  ← first "name" is silently overwritten

# ── Create using dict() constructor ──────────────────────────────────────────
car = dict(brand="Toyota", price=345657, year=2026)
print(car)   # {'brand': 'Toyota', 'price': 345657, 'year': 2026}

# ── Create using zip() — pair two lists into a dict ──────────────────────────
names  = ["Yash", "Prashant", "Super", "Pop"]
salary = [23000, 45999, 67555, 79999]
dict1  = dict(zip(names, salary))
print(dict1)   # {'Yash': 23000, 'Prashant': 45999, 'Super': 67555, 'Pop': 79999}

# ── dict.fromkeys() — same default value for all keys ────────────────────────
keys    = ["name", "age", "city"]
default = dict.fromkeys(keys, "Unknown")
print(default)   # {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}


# =============================================================================
# 2. NESTED DICTIONARIES
# =============================================================================
# A dictionary whose VALUES are other dictionaries.
# Used for hierarchical / structured data (like JSON).

nestedPersons = {
    "name": {
        "Yash": {
            "age" : 23,
            "city": "Pune"
        },
        "Prashant": {
            "age" : 25,
            "city": "Mumbai"
        }
        # ⚠️  Duplicate key "Prashant" above — only the LAST one is kept
    }
}

# Access nested value — chain keys one by one
print(nestedPersons["name"]["Prashant"]["city"])   # Mumbai

# Safe nested access using .get() — no crash if key is missing
print(nestedPersons["name"].get("Rohit", "Not found"))   # Not found

# Real-world style nested dict — student records
students = {
    "Yash"    : {"age": 20, "grade": "A", "city": "Delhi",  "marks": [95, 88, 91]},
    "Prashant": {"age": 22, "grade": "B", "city": "Mumbai", "marks": [78, 82, 80]},
    "Rohit"   : {"age": 21, "grade": "A", "city": "Pune",   "marks": [91, 94, 89]},
}

print(students["Yash"]["grade"])            # A
print(students["Rohit"]["marks"][0])        # 91  — first mark of Rohit
print(sum(students["Yash"]["marks"]))       # 274 — total marks of Yash


# =============================================================================
# 3. ACCESSING VALUES
# =============================================================================

person = {
    "name"  : "Yash",
    "age"   : 23,
    "city"  : "Pune",
    "salary": 455657
}

# ── Direct key access — raises KeyError if key is missing ─────────────────────
print(person["name"])    # Yash
print(person["age"])     # 23
# print(person["phone"]) # ❌ KeyError: 'phone'

# ── get() — SAFE access, returns None or custom default if key missing ─────────
print(person.get("age"))              # 23
print(person.get("phone"))            # None    — no crash
print(person.get("phone", "N/A"))     # N/A     — custom default

# ── Looping to access all keys and values ─────────────────────────────────────
for key in person:
    print(key, "→", person[key])

# With .items() — cleanest way
for key, value in person.items():
    print(f"  {key:10} : {value}")


# =============================================================================
# 4. CHECKING IF A KEY EXISTS
# =============================================================================

person = {"name": "Yash", "age": 23, "city": "Pune", "salary": 455657}

# ── in — checks KEYS only ─────────────────────────────────────────────────────
print("name"   in person)    # True
print("phone"  in person)    # False
print("Yash"   in person)    # False — "Yash" is a VALUE, not a key

# Check then act — safe pattern
if "name" in person:
    print("Name found:", person["name"])   # Name found: Yash

# Check in nested dict
nestedPersons = {"name": {"Yash": {"age": 23, "city": "Pune"}}}
if "name" in nestedPersons:
    print("Present:", nestedPersons["name"])

# Check if value exists
print("Yash" in person.values())    # True
print(23     in person.values())    # True

# ── not in ────────────────────────────────────────────────────────────────────
if "phone" not in person:
    print("Phone number not on record")


# =============================================================================
# 5. ADDING AND UPDATING VALUES
# =============================================================================

person = {"name": "Yash", "age": 23, "city": "Pune"}

# ── Add new key-value pair ────────────────────────────────────────────────────
person["salary"] = 455657
person["email"]  = "yash@example.com"
print(person)

# ── Update existing value ─────────────────────────────────────────────────────
person["name"] = "Yash Sharma"     # overwrites old value
print(person["name"])              # Yash Sharma

# ── update() — add/modify MULTIPLE keys at once ───────────────────────────────
person.update({"age": 24, "city": "Delhi", "phone": "9999999999"})
print(person)

# ── Update nested dict ────────────────────────────────────────────────────────
nestedPersons = {
    "name": {
        "Prashant": {"age": 25, "city": "Mumbai"}
    }
}
nestedPersons["name"]["Prashant"]["city"] = "Delhi"
print(nestedPersons["name"]["Prashant"])   # {'age': 25, 'city': 'Delhi'}

# ── setdefault() — add key ONLY if it doesn't exist ──────────────────────────
person.setdefault("phone", "Not provided")   # phone exists — no change
person.setdefault("score", 95)               # score missing — adds it
print(person.get("score"))   # 95


# =============================================================================
# 6. REMOVING KEY-VALUE PAIRS
# =============================================================================

person = {"name": "Yash", "age": 23, "city": "Pune", "grade": "A"}

# ── pop() — remove key and RETURN its value ───────────────────────────────────
removed = person.pop("grade")
print("Removed:", removed)    # A
print(person)                 # grade is gone

person.pop("phone", "Key not found")    # safe — no KeyError
print(person)                           # unchanged

# ── popitem() — remove LAST inserted pair and return it ───────────────────────
last = person.popitem()
print("Last item:", last)    # ('city', 'Pune')
print(person)

# ── del — delete by key ───────────────────────────────────────────────────────
person = {"name": "Yash", "age": 23, "city": "Pune"}
del person["city"]
print(person)   # {'name': 'Yash', 'age': 23}
# del person["phone"]  # ❌ KeyError

# ── clear() — remove ALL pairs ────────────────────────────────────────────────
person.clear()
print(person)   # {}


# =============================================================================
# 7. DICTIONARY VIEWS — keys(), values(), items()
# =============================================================================

person = {"name": "Yash", "age": 23, "city": "Pune", "salary": 455657}

print(person.keys())     # dict_keys(['name', 'age', 'city', 'salary'])
print(person.values())   # dict_values(['Yash', 23, 'Pune', 455657])
print(person.items())    # dict_items([('name', 'Yash'), ('age', 23), ...])

# Convert to list
print(list(person.keys()))     # ['name', 'age', 'city', 'salary']
print(list(person.values()))   # ['Yash', 23, 'Pune', 455657]

# Views are LIVE — they reflect changes to the dict
keys_view = person.keys()
person["email"] = "yash@example.com"
print(keys_view)   # dict_keys([..., 'email'])  — automatically updated!


# =============================================================================
# 8. MERGING DICTIONARIES
# =============================================================================

num1 = {"a": 1, "b": 34}
num2 = {"b": 38, "c": 455}

# ── | operator (Python 3.9+) — creates a NEW merged dict ─────────────────────
merged = num1 | num2     # right side wins on duplicate keys
print(merged)   # {'a': 1, 'b': 38, 'c': 455}

merged = num2 | num1     # now num1 wins on "b"
print(merged)   # {'b': 34, 'a': 1, 'c': 455}

# ── update() — merge IN PLACE ────────────────────────────────────────────────
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
d1.update(d2)    # d2 values overwrite d1 on clash
print(d1)        # {'a': 1, 'b': 99, 'c': 3}

# ── ** unpacking — works in all Python 3.x versions ──────────────────────────
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
merged = {**d1, **d2}   # right side wins
print(merged)           # {'a': 1, 'b': 99, 'c': 3}


# =============================================================================
# 9. DICTIONARY COMPREHENSION
# =============================================================================
# Syntax: {key_expr: value_expr  for  item  in  iterable  if  condition}

# ── Squares — u is key, u**2 is value ────────────────────────────────────────
squares = {u: u**2 for u in range(1, 11)}   # range(1,11) → 1 to 10
print(squares)
# {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, 10:100}

# ── Cubes of odd numbers ──────────────────────────────────────────────────────
cubes = {x: x**3 for x in range(1, 6) if x % 2 != 0}
print(cubes)   # {1: 1, 3: 27, 5: 125}

# ── Build grade book from two lists ──────────────────────────────────────────
names_list  = ["Yash", "Prashant", "Rohit"]
scores_list = [95, 88, 76]
grade_book  = {name: score for name, score in zip(names_list, scores_list)}
print(grade_book)   # {'Yash': 95, 'Prashant': 88, 'Rohit': 76}

# ── Filter: only students who scored >= 90 ────────────────────────────────────
toppers = {k: v for k, v in grade_book.items() if v >= 90}
print(toppers)   # {'Yash': 95}

# ── Swap keys and values ──────────────────────────────────────────────────────
original = {"name": "Yash", "city": "Delhi"}
swapped  = {v: k for k, v in original.items()}
print(swapped)   # {'Yash': 'name', 'Delhi': 'city'}

# ── Convert list of tuples to dict ───────────────────────────────────────────
pairs   = [("a", 1), ("b", 2), ("c", 3)]
from_pairs = {k: v for k, v in pairs}
print(from_pairs)   # {'a': 1, 'b': 2, 'c': 3}


# =============================================================================
# 10. USEFUL BUILT-IN FUNCTIONS WITH DICTS
# =============================================================================

grades = {"Yash": 95, "Prashant": 88, "Rohit": 76, "Aarav": 91}

print(len(grades))              # 4   — number of key-value pairs
print(max(grades.values()))     # 95  — highest score
print(min(grades.values()))     # 76  — lowest score
print(sum(grades.values()))     # 350 — total of all scores

# Who scored highest?
top_student = max(grades, key=grades.get)
print(top_student)   # Yash

# Sort by value (descending)
sorted_grades = dict(sorted(grades.items(), key=lambda x: x[1], reverse=True))
print(sorted_grades)   # {'Yash': 95, 'Aarav': 91, 'Prashant': 88, 'Rohit': 76}

# Sort by key (alphabetical)
sorted_by_name = dict(sorted(grades.items()))
print(sorted_by_name)   # {'Aarav': 91, 'Prashant': 88, 'Rohit': 76, 'Yash': 95}

# ── copy() — shallow copy ─────────────────────────────────────────────────────
original = {"a": 1, "b": 2}
copy     = original.copy()
copy["c"] = 3
print(original)   # {'a': 1, 'b': 2}  — unaffected
print(copy)       # {'a': 1, 'b': 2, 'c': 3}


# =============================================================================
# 11. REAL-WORLD USE CASES
# =============================================================================

# ── Word frequency counter ────────────────────────────────────────────────────
sentence = "yash is good yash is smart prashant is good"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
# {'yash': 2, 'is': 3, 'good': 2, 'smart': 1, 'prashant': 1}

# ── Student report card ───────────────────────────────────────────────────────
report = {
    "Yash": {"Maths": 95, "Science": 88, "English": 91},
    "Prashant": {"Maths": 78, "Science": 82, "English": 80},
}
for student, subjects in report.items():
    total   = sum(subjects.values())
    average = total / len(subjects)
    print(f"{student}: Total={total}, Average={average:.1f}")

# ── Phone book ────────────────────────────────────────────────────────────────
phonebook = {"Yash": "9876543210", "Prashant": "9123456789"}
search    = "Yash"
if search in phonebook:
    print(f"{search}'s number: {phonebook[search]}")

# ── Config / settings store ───────────────────────────────────────────────────
config = {
    "theme"     : "dark",
    "font_size" : 14,
    "language"  : "Python",
    "autosave"  : True,
}
print(f"Theme: {config['theme']}, Font: {config['font_size']}px")

# ── Inventory tracker ─────────────────────────────────────────────────────────
inventory = {"apple": 50, "banana": 30, "mango": 0}
for item, qty in inventory.items():
    status = "In stock" if qty > 0 else "Out of stock"
    print(f"  {item:10} : {qty:3} units — {status}")


# =============================================================================
# QUICK REFERENCE TABLE
# =============================================================================
#
#  Method / Operation           What it does
#  ────────────────────────────  ──────────────────────────────────────────────
#  d[key]                        Access value — KeyError if missing
#  d.get(key, default)           Safe access — returns default if missing
#  d[key] = value                Add or update a key
#  d.update({k:v})               Add/update multiple keys at once
#  d.setdefault(key, default)    Add key only if it doesn't already exist
#  d.pop(key, default)           Remove & return value (safe with default)
#  d.popitem()                   Remove & return last inserted (key, value)
#  del d[key]                    Delete key — KeyError if missing
#  d.clear()                     Remove all items
#  d.keys()                      Live view of all keys
#  d.values()                    Live view of all values
#  d.items()                     Live view of all (key, value) pairs
#  d.copy()                      Shallow copy
#  dict(zip(k, v))               Build dict from two lists
#  dict.fromkeys(keys, val)      New dict with same value for all keys
#  key in d                      True if key exists (checks KEYS only)
#  len(d)                        Number of key-value pairs
#  d1 | d2                       Merge dicts — new dict (Python 3.9+)
#  d1.update(d2)                 Merge in place
#  {**d1, **d2}                  Merge using unpacking (all Python 3.x)
#  max(d, key=d.get)             Key with the highest value
#  sorted(d.items(), key=...)    Sort entries by key or value


# =============================================================================
# PRACTICE QUESTIONS
# =============================================================================

# Q1. Create a person dict with name, age, city. Print each key and value.
# ------ Solution ------
p_q1 = {"name": "Yash", "age": 23, "city": "Pune"}
for k, v in p_q1.items():
    print(f"{k}: {v}")


# Q2. Use zip() to create a salary dict from two lists.
# ------ Solution ------
names_q2  = ["Yash", "Prashant", "Rohit"]
salary_q2 = [45000, 55000, 40000]
print(dict(zip(names_q2, salary_q2)))


# Q3. Safely access a "phone" key that doesn't exist. Print "Not available".
# ------ Solution ------
p_q3 = {"name": "Yash", "age": 23}
print(p_q3.get("phone", "Not available"))   # Not available


# Q4. Access Prashant's city from this nested dict.
# ------ Solution ------
nested_q4 = {"name": {"Prashant": {"age": 25, "city": "Mumbai"}}}
print(nested_q4["name"]["Prashant"]["city"])   # Mumbai


# Q5. Update the nested dict — change Prashant's city to "Delhi".
# ------ Solution ------
nested_q4["name"]["Prashant"]["city"] = "Delhi"
print(nested_q4["name"]["Prashant"])   # {'age': 25, 'city': 'Delhi'}


# Q6. Build a squares dict {1:1, 2:4, ..., 10:100} using comprehension.
# ------ Solution ------
squares_q6 = {u: u**2 for u in range(1, 11)}
print(squares_q6)


# Q7. Merge {"a":1,"b":34} and {"b":38,"c":455}. The second dict should win.
# ------ Solution ------
n1_q7  = {"a": 1,  "b": 34}
n2_q7  = {"b": 38, "c": 455}
merged = n1_q7 | n2_q7
print(merged)   # {'a': 1, 'b': 38, 'c': 455}


# Q8. Count word frequency in: "the cat sat on the mat the cat".
# ------ Solution ------
words_q8 = "the cat sat on the mat the cat".split()
freq_q8  = {}
for w in words_q8:
    freq_q8[w] = freq_q8.get(w, 0) + 1
print(freq_q8)   # {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}


# Q9. From the grade_book, find the top scorer using max().
# ------ Solution ------
grade_book_q9 = {"Yash": 95, "Prashant": 88, "Rohit": 76, "Aarav": 91}
top = max(grade_book_q9, key=grade_book_q9.get)
print(f"Top scorer: {top} with {grade_book_q9[top]}")   # Yash with 95


# Q10. (Challenge) Given the student report below, calculate and print
#      each student's average score, then print the overall class average.
# ------ Solution ------
report_q10 = {
    "Yash"    : {"Maths": 95, "Science": 88, "English": 91},
    "Prashant": {"Maths": 78, "Science": 82, "English": 80},
    "Rohit"   : {"Maths": 91, "Science": 94, "English": 89},
}
all_avgs = []
for name, marks in report_q10.items():
    avg = sum(marks.values()) / len(marks)
    all_avgs.append(avg)
    print(f"{name}: Average = {avg:.1f}")

print(f"Class Average = {sum(all_avgs)/len(all_avgs):.1f}")