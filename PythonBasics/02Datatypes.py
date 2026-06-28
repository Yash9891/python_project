# =============================================================================
#  PYTHON DATA TYPES — Complete Reference Guide
#  Author  : Yash
#  Purpose : Understand all built-in data types in Python from scratch
# =============================================================================


# -----------------------------------------------------------------------------
# WHAT IS A DATA TYPE?
# -----------------------------------------------------------------------------
# A data type tells Python what kind of value a variable holds and what
# operations are allowed on it.
# Python is dynamically typed — types are assigned automatically at runtime.
#
# Built-in types at a glance:
#   Numeric   → int, float, complex
#   Text      → str
#   Boolean   → bool
#   None      → NoneType
#   Sequence  → list, tuple, range
#   Mapping   → dict
#   Set       → set, frozenset

#What are the built-in data structures in Python?
# List
# Tuple
# Dictionary
# Set

# =============================================================================
# 1. INTEGER  (int)
# =============================================================================
# Whole numbers — positive, negative, or zero. No size limit in Python.

age        =  23
score      = -10
population =  1_000_000   # underscores allowed for readability

print(age)          # 23
print(type(age))    # <class 'int'>

# Common operations
print(10 + 3)   # 13  — addition
print(10 - 3)   # 7   — subtraction
print(10 * 3)   # 30  — multiplication
print(10 ** 3)  # 1000 — exponentiation (10 to the power 3)
print(10 // 3)  # 3   — floor division (drops the decimal)
print(10 %  3)  # 1   — modulus (remainder)

# Different number bases
binary  = 0b1010   # base-2  → 10
octal   = 0o12     # base-8  → 10
hexa    = 0xA      # base-16 → 10
print(binary, octal, hexa)   # 10 10 10


# =============================================================================
# 2. FLOAT  (float)
# =============================================================================
# Numbers with a decimal point. Stored in 64-bit IEEE 754 format.

pi      = 3.14159
temp    = -98.6
sci     = 1.5e3    # scientific notation → 1500.0

print(pi)           # 3.14159
print(type(pi))     # <class 'float'>
print(sci)          # 1500.0

# Floating-point precision quirk (important to know!)
print(0.1 + 0.2)            # 0.30000000000000004  ← not exactly 0.3
print(round(0.1 + 0.2, 2))  # 0.3  ← use round() to fix display

# Useful float constants
import math
print(math.inf)    #  infinity
print(-math.inf)   # -infinity
print(math.nan)    #  Not a Number (result of undefined operations)


# =============================================================================
# 3. COMPLEX  (complex)
# =============================================================================
# Numbers with a real and imaginary part. Written as  a + bj

z1 = 3 + 4j
z2 = complex(2, -5)   # same as 2 - 5j

print(z1)             # (3+4j)
print(type(z1))       # <class 'complex'>
print(z1.real)        # 3.0  — real part
print(z1.imag)        # 4.0  — imaginary part
print(z1 + z2)        # (5-1j) — addition works naturally


# =============================================================================
# 4. STRING  (str)
# =============================================================================
# An ordered, immutable sequence of Unicode characters.
# Defined with single quotes, double quotes, or triple quotes.

name     = "Yash"
greeting = 'Hello, World!'
bio      = """This is a
multi-line string."""

print(name)           # Yash
print(type(name))     # <class 'str'>

# ── Common string operations ──────────────────────────────────────────────────
s = "python programming"

print(len(s))           # 18       — number of characters
print(s.upper())        # PYTHON PROGRAMMING
print(s.lower())        # python programming
print(s.title())        # Python Programming
print(s.capitalize())   # Python programming
print(s.replace("python", "java"))   # java programming
print(s.split())        # ['python', 'programming']
print(s.strip())        # removes leading/trailing whitespace
print(s.startswith("py"))  # True
print(s.endswith("ing"))   # True
print("gram" in s)         # True  — membership check

# ── Indexing and slicing ──────────────────────────────────────────────────────
word = "Python"
#        P  y  t  h  o  n
# index  0  1  2  3  4  5
# neg   -6 -5 -4 -3 -2 -1

print(word[0])       # P    — first character
print(word[-1])      # n    — last character
print(word[0:3])     # Pyt  — slice [start:stop] (stop is excluded)
print(word[::2])     # Pto  — every second character
print(word[::-1])    # nohtyP — reversed

# ── String formatting ─────────────────────────────────────────────────────────
student = "Yash"
marks   = 95

# f-string (recommended — Python 3.6+)
print(f"Name: {student}, Marks: {marks}")

# .format()
print("Name: {}, Marks: {}".format(student, marks))

# % formatting (older style)
print("Name: %s, Marks: %d" % (student, marks))

# Strings are IMMUTABLE — you cannot change a character in place
# name[0] = "y"   # ❌ TypeError: 'str' object does not support item assignment


# =============================================================================
# 5. BOOLEAN  (bool)
# =============================================================================
# Has exactly two values: True or False.
# Internally, True == 1 and False == 0.

is_student = True
has_passed = False

print(is_student)         # True
print(type(is_student))   # <class 'bool'>

# Boolean arithmetic
print(True  + True)    # 2
print(True  + False)   # 1
print(False + False)   # 0
print(True  * 10)      # 10

# Logical operators
print(True  and False)  # False
print(True  or  False)  # True
print(not  True)        # False

# Comparison operators return booleans
print(10 > 5)    # True
print(10 == 5)   # False
print(10 != 5)   # True

# Truthy and falsy values — every object has a boolean interpretation
print(bool(0))        # False  — zero is falsy
print(bool(1))        # True   — any non-zero number is truthy
print(bool(""))       # False  — empty string is falsy
print(bool("Yash"))   # True
print(bool([]))       # False  — empty list is falsy
print(bool([1, 2]))   # True
print(bool(None))     # False


# =============================================================================
# 6. NONETYPE  (None)
# =============================================================================
# Represents the absence of a value. Python's equivalent of null.
# There is only ONE None object in all of Python.

result = None

print(result)          # None
print(type(result))    # <class 'NoneType'>

# Use 'is' (not ==) to check for None
if result is None:
    print("No value assigned yet")

# Functions that don't return anything implicitly return None
def greet():
    print("Hello!")

output = greet()
print(output)    # None


# =============================================================================
# 7. LIST  (list)
# =============================================================================
# Ordered, mutable collection. Can hold mixed types. Allows duplicates.

fruits = ["apple", "banana", "cherry"]
mixed  = [1, "hello", 3.14, True, None]

print(fruits)          # ['apple', 'banana', 'cherry']
print(type(fruits))    # <class 'list'>
print(len(fruits))     # 3

# Indexing and slicing work the same as strings
print(fruits[0])       # apple
print(fruits[-1])      # cherry
print(fruits[0:2])     # ['apple', 'banana']

# ── Modifying lists ───────────────────────────────────────────────────────────
fruits.append("mango")         # add to end
fruits.insert(1, "grape")      # insert at index 1
fruits.remove("banana")        # remove by value
popped = fruits.pop()          # remove and return last item
fruits.sort()                  # sort in place
fruits.reverse()               # reverse in place
print(fruits)

# ── Other useful methods ──────────────────────────────────────────────────────
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(min(nums))        # 1
print(max(nums))        # 9
print(sum(nums))        # 31
print(nums.count(1))    # 2   — how many times 1 appears
print(nums.index(5))    # 4   — index of value 5


# =============================================================================
# 8. TUPLE  (tuple)
# =============================================================================
# Ordered, IMMUTABLE collection. Faster than list. Good for fixed data.

coordinates = (10.5, 20.3)
rgb         = (255, 128, 0)
single      = (42,)          # ← trailing comma is required for a 1-item tuple

print(coordinates)         # (10.5, 20.3)
print(type(coordinates))   # <class 'tuple'>

# Access exactly like a list
print(rgb[0])   # 255

# Tuples support unpacking
r, g, b = rgb
print(r, g, b)   # 255 128 0

# Tuples are immutable
# rgb[0] = 100   # ❌ TypeError: 'tuple' object does not support item assignment


# =============================================================================
# 9. RANGE  (range)
# =============================================================================
# Represents an immutable sequence of numbers. Memory-efficient — stores
# only start, stop, and step — not all values.

r1 = range(5)          # 0, 1, 2, 3, 4
r2 = range(1, 10)      # 1 … 9
r3 = range(0, 20, 5)   # 0, 5, 10, 15

print(list(r1))   # [0, 1, 2, 3, 4]
print(list(r2))   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(r3))   # [0, 5, 10, 15]

for i in range(3):
    print(i, end=" ")   # 0 1 2
print()


# =============================================================================
# 10. DICTIONARY  (dict)
# =============================================================================
# Unordered (insertion-ordered since Python 3.7) collection of key-value pairs.
# Keys must be unique and immutable; values can be anything.

student = {
    "name"  : "Yash",
    "age"   : 20,
    "marks" : 95.5,
    "passed": True
}

print(student)              # full dictionary
print(type(student))        # <class 'dict'>
print(student["name"])      # Yash        — access by key
print(student.get("age"))   # 20          — safe access (no KeyError if missing)

# ── Modifying dictionaries ────────────────────────────────────────────────────
student["grade"] = "A"      # add new key
student["age"]   = 21       # update existing key
del student["passed"]       # delete a key

# ── Useful methods ────────────────────────────────────────────────────────────
print(student.keys())       # all keys
print(student.values())     # all values
print(student.items())      # all key-value pairs as tuples

for key, value in student.items():
    print(f"  {key}: {value}")


# =============================================================================
# 11. SET  (set)
# =============================================================================
# Unordered collection of UNIQUE items. No indexing. Great for deduplication.

colors = {"red", "green", "blue", "red"}   # duplicate "red" is removed
print(colors)         # {'red', 'green', 'blue'}  (order may vary)
print(type(colors))   # <class 'set'>

# ── Set operations ────────────────────────────────────────────────────────────
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # {1,2,3,4,5,6}  — union
print(a & b)   # {3,4}          — intersection
print(a - b)   # {1,2}          — difference (in a but not b)
print(a ^ b)   # {1,2,5,6}      — symmetric difference

# Add / remove
colors.add("yellow")
colors.discard("green")   # safe remove (no error if not found)
print(colors)

# frozenset — immutable version of set
fs = frozenset([1, 2, 3])
# fs.add(4)   # ❌ AttributeError — frozenset is immutable


# =============================================================================
# 12. TYPE CONVERSION CHEAT SHEET
# =============================================================================

# To int
print(int(3.9))       # 3       — truncates, does NOT round
print(int("42"))      # 42
print(int(True))      # 1

# To float
print(float(5))       # 5.0
print(float("3.14"))  # 3.14

# To string
print(str(100))       # "100"
print(str(True))      # "True"

# To bool
print(bool(0))        # False
print(bool(""))       # False
print(bool(None))     # False
print(bool(-1))       # True  — any non-zero is truthy

# To list
print(list("abc"))         # ['a', 'b', 'c']
print(list((1, 2, 3)))     # [1, 2, 3]
print(list({1, 2, 3}))     # [1, 2, 3]

# To tuple
print(tuple([1, 2, 3]))    # (1, 2, 3)

# To set
print(set([1, 2, 2, 3]))   # {1, 2, 3}  — duplicates removed


# =============================================================================
# QUICK REFERENCE TABLE
# =============================================================================
#
#  Type       Example                  Mutable   Ordered   Duplicates
#  ─────────  ───────────────────────  ────────  ────────  ──────────
#  int        42                       No        —         —
#  float      3.14                     No        —         —
#  complex    3+4j                     No        —         —
#  str        "hello"                  No        Yes       Yes
#  bool       True / False             No        —         —
#  NoneType   None                     No        —         —
#  list       [1, 2, 3]                Yes       Yes       Yes
#  tuple      (1, 2, 3)                No        Yes       Yes
#  range      range(0, 10)             No        Yes       Yes
#  dict       {"a": 1, "b": 2}        Yes       Yes*      Keys: No
#  set        {1, 2, 3}               Yes       No        No
#  frozenset  frozenset({1, 2})        No        No        No
#
#  * dict preserves insertion order since Python 3.7


# =============================================================================
# PRACTICE QUESTIONS
# =============================================================================

# Q1. Create one variable for each type: int, float, str, bool, None.
#     Print the value and type of each.
# ------ Solution ------
samples = [42, 3.14, "Yash", True, None]
for s in samples:
    print(f"Value: {repr(s):10}  Type: {type(s).__name__}")


# Q2. Given price = "499.99", convert it to a float and apply a 10% discount.
# ------ Solution ------
price    = "499.99"
price    = float(price)
discount = price * 0.10
print(f"Discounted price: {price - discount:.2f}")   # 449.99


# Q3. Create a list of 5 fruits. Sort it, reverse it, and print the result.
# ------ Solution ------
fruits = ["banana", "apple", "mango", "cherry", "grape"]
fruits.sort()
fruits.reverse()
print(fruits)


# Q4. Create a dictionary for a student with keys: name, age, grade.
#     Add a new key 'city' and update the age. Print all key-value pairs.
# ------ Solution ------
student = {"name": "Yash", "age": 20, "grade": "A"}
student["city"] = "Delhi"
student["age"]  = 21
for k, v in student.items():
    print(f"  {k}: {v}")


# Q5. Given two sets A = {1,2,3,4} and B = {3,4,5,6}, find:
#     union, intersection, and difference (A - B).
# ------ Solution ------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union       :", A | B)
print("Intersection:", A & B)
print("Difference  :", A - B)


# Q6. Use a tuple to store (latitude, longitude) of a city. Unpack and print.
# ------ Solution ------
location = (28.6139, 77.2090)   # New Delhi
latitude, longitude = location
print(f"Lat: {latitude}, Long: {longitude}")


# Q7. Remove duplicates from the list [1,2,2,3,3,3,4] using a set.
# ------ Solution ------
nums   = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))
unique.sort()
print(unique)   # [1, 2, 3, 4]


# Q8. Write a function that returns None if a number is negative,
#     otherwise returns the square of that number.
# ------ Solution ------
def safe_square(n):
    if n < 0:
        return None
    return n ** 2

print(safe_square(5))    # 25
print(safe_square(-3))   # None


