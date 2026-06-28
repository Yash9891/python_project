# =============================================================================
#  PYTHON BUILT-IN FUNCTIONS — Complete Reference Guide
#  Author  : Yash
#  Purpose : Understand Python's most important built-in functions from scratch
# =============================================================================


# -----------------------------------------------------------------------------
# WHAT IS A BUILT-IN FUNCTION?
# -----------------------------------------------------------------------------
# Built-in functions are ready-to-use functions that come with Python.
# You do NOT need to import anything — they are always available.
#
# Python has 68+ built-in functions. This file covers the most essential ones
# grouped by category:
#
#   1. Type Checking     → type(), isinstance()
#   2. Type Conversion   → int(), float(), str(), bool(), list(), tuple(),
#                          set(), dict(), complex()
#   3. Input / Output    → input(), print()
#   4. Numeric           → abs(), round(), pow(), divmod(), max(), min(), sum()
#   5. Sequence          → len(), range(), sorted(), reversed(), enumerate(),
#                          zip(), map(), filter()
#   6. Object Info       → id(), dir(), help(), vars(), callable()
#   7. Iteration / Logic → all(), any()
#   8. String / Format   → repr(), format(), chr(), ord()
#   9. Math Utilities    → bin(), oct(), hex()


# =============================================================================
# 1. TYPE CHECKING
# =============================================================================

# ── type() ───────────────────────────────────────────────────────────────────
# Returns the data type (class) of a variable or value.

a         = 90
name      = "Yash"
float_12  = 23.4
flag      = True
nothing   = None

print(type(a))         # <class 'int'>
print(type(name))      # <class 'str'>
print(type(float_12))  # <class 'float'>
print(type(flag))      # <class 'bool'>
print(type(nothing))   # <class 'NoneType'>
print(type([1, 2]))    # <class 'list'>
print(type({"k": 1}))  # <class 'dict'>

# Get just the type name as a string (useful for printing)
print(type(a).__name__)      # int
print(type(name).__name__)   # str


# ── isinstance() ─────────────────────────────────────────────────────────────
# Returns True if a variable is an instance of the given type (or types).
# Preferred over type() for type checking because it respects inheritance.

print(isinstance(a, int))           # True
print(isinstance(name, str))        # True
print(isinstance(float_12, float))  # True
print(isinstance(flag, bool))       # True  — bool is a subclass of int
print(isinstance(flag, int))        # True  — so this is also True!

# Check against multiple types at once using a tuple
value = 3.14
print(isinstance(value, (int, float)))   # True — matches float


# =============================================================================
# 2. TYPE CONVERSION  (Type Casting)
# =============================================================================
# Convert a value from one data type to another.

# ── int() ─────────────────────────────────────────────────────────────────────
# Converts to integer. Truncates floats (does NOT round). Parses numeric strings.

num = "23"
num = int(num)
print(type(num))    # <class 'int'>
print(num)          # 23

print(int(9.9))     # 9    ← truncated, NOT rounded
print(int(9.1))     # 9
print(int(True))    # 1
print(int(False))   # 0
print(int("0b1010", 2))   # 10  — convert binary string to int
print(int("0xFF",  16))   # 255 — convert hex string to int

# print(int("hello"))   # ❌ ValueError — "hello" is not a number


# ── float() ──────────────────────────────────────────────────────────────────
# Converts to floating-point number.

a = 34
a = float(a)
print(type(a))    # <class 'float'>
print(a)          # 34.0

print(float("3.14"))    # 3.14
print(float(True))      # 1.0
print(float("inf"))     # inf
print(float("-inf"))    # -inf


# ── str() ────────────────────────────────────────────────────────────────────
# Converts to string.

num = 20
string23 = str(num)
print(type(string23))   # <class 'str'>
print(string23)         # "20"

print(str(3.14))    # "3.14"
print(str(True))    # "True"
print(str(None))    # "None"
print(str([1,2,3])) # "[1, 2, 3]"


# ── bool() ───────────────────────────────────────────────────────────────────
# Converts to boolean. Remember: 0, "", [], {}, None, False → False. Everything
# else → True.

print(bool(0))       # False
print(bool(1))       # True
print(bool(-99))     # True  — any non-zero number
print(bool(""))      # False — empty string
print(bool("Yash"))  # True
print(bool([]))      # False — empty list
print(bool([0]))     # True  — list with one item (even if item is 0)
print(bool(None))    # False


# ── list(), tuple(), set(), dict() ───────────────────────────────────────────
# Convert iterables to list / tuple / set / dict.

print(list("abc"))           # ['a', 'b', 'c']
print(list((1, 2, 3)))       # [1, 2, 3]
print(list({1, 2, 3}))       # [1, 2, 3]  (order may vary)
print(list(range(5)))        # [0, 1, 2, 3, 4]

print(tuple([10, 20, 30]))   # (10, 20, 30)

print(set([1, 2, 2, 3, 3]))  # {1, 2, 3}  — removes duplicates

# dict from a list of key-value pairs
print(dict([("a", 1), ("b", 2)]))   # {'a': 1, 'b': 2}


# ── complex() ────────────────────────────────────────────────────────────────
print(complex(3, 4))    # (3+4j)
print(complex("2+3j"))  # (2+3j)


# =============================================================================
# 3. INPUT / OUTPUT
# =============================================================================

# ── print() ──────────────────────────────────────────────────────────────────
# Outputs values to the console.
# Signature: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print("Hello", "Yash")               # Hello Yash          — default sep is space
print("Hello", "Yash", sep=", ")     # Hello, Yash
print("Hello", "Yash", sep=" | ")    # Hello | Yash

print("Loading", end="")             # no newline at end
print("...", end="\n")               # Loading...

# Print multiple values with f-string
name  = "Yash"
score = 95
print(f"Student: {name}, Score: {score}")

# Print with formatting
print(f"Pi is approximately {3.14159:.2f}")   # Pi is approximately 3.14
print(f"{'Left':<10} | {'Right':>10}")        # Left       |      Right


# ── input() ──────────────────────────────────────────────────────────────────
# Reads a line of text from the user. ALWAYS returns a STRING.

# Uncomment to test interactively:
# name = input("Type your name: ")
# print("Hello " + name)

# ⚠️  input() returns str — convert when you need numbers
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(num1 + num2)    # now adds numbers, not concatenates strings

# Common mistake
# num1 = input("Enter number 1: ")   # returns "10" (string)
# num2 = input("Enter number 2: ")   # returns "20" (string)
# print(num1 + num2)    # "1020"  ← string concatenation, NOT 30!
# Fix:
# print(int(num1) + int(num2))   # 30  ✅


# =============================================================================
# 4. NUMERIC FUNCTIONS
# =============================================================================

# ── abs() — absolute value ───────────────────────────────────────────────────
print(abs(-42))     # 42
print(abs(3.7))     # 3.7
print(abs(-3.7))    # 3.7
print(abs(3 + 4j))  # 5.0  — magnitude of complex number

# ── round() — round to n decimal places ──────────────────────────────────────
print(round(3.14159))      # 3     — rounds to nearest integer
print(round(3.14159, 2))   # 3.14
print(round(3.14159, 4))   # 3.1416
print(round(2.5))          # 2     — Python uses "banker's rounding"
print(round(3.5))          # 4

# ── pow() — exponentiation (optional modulus) ────────────────────────────────
print(pow(2, 10))        # 1024   — same as 2 ** 10
print(pow(2, 10, 1000))  # 24    — (2**10) % 1000  — efficient for large nums

# ── divmod() — quotient AND remainder in one call ─────────────────────────────
quotient, remainder = divmod(17, 5)
print(quotient)    # 3
print(remainder)   # 2

# ── max() and min() ──────────────────────────────────────────────────────────
print(max(3, 7, 1, 9, 2))        # 9
print(min(3, 7, 1, 9, 2))        # 1
print(max([10, 50, 30, 20]))      # 50
print(min("apple", "banana"))     # apple  — alphabetical comparison
print(max("Yash", "Prashant", key=len))   # Prashant — longest string

# ── sum() ────────────────────────────────────────────────────────────────────
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))          # 15
print(sum(numbers, 100))     # 115  — 100 is the starting value (offset)


# =============================================================================
# 5. SEQUENCE FUNCTIONS
# =============================================================================

# ── len() — length / count of items ──────────────────────────────────────────
print(len("Python"))         # 6
print(len([1, 2, 3, 4]))     # 4
print(len((10, 20, 30)))     # 3
print(len({"a": 1, "b": 2})) # 2  — counts keys
print(len({1, 2, 3}))        # 3

# ── range() — generates a number sequence ────────────────────────────────────
print(list(range(5)))          # [0, 1, 2, 3, 4]
print(list(range(2, 8)))       # [2, 3, 4, 5, 6, 7]
print(list(range(0, 20, 5)))   # [0, 5, 10, 15]
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]  — countdown

# ── sorted() — returns a NEW sorted list ─────────────────────────────────────
nums   = [5, 2, 8, 1, 9, 3]
names  = ["Prashant", "Yash", "Aarav"]

print(sorted(nums))                       # [1, 2, 3, 5, 8, 9]
print(sorted(nums, reverse=True))         # [9, 8, 5, 3, 2, 1]
print(sorted(names))                      # ['Aarav', 'Prashant', 'Yash']
print(sorted(names, key=len))             # ['Yash', 'Aarav', 'Prashant'] — by length
print(sorted(names, key=str.lower))       # case-insensitive sort

# Note: list.sort() modifies IN PLACE; sorted() returns a new list
original = [3, 1, 2]
new_list = sorted(original)   # original unchanged
print(original)   # [3, 1, 2]
print(new_list)   # [1, 2, 3]

# ── reversed() — returns an iterator in reverse order ────────────────────────
items = [1, 2, 3, 4, 5]
print(list(reversed(items)))   # [5, 4, 3, 2, 1]
print(list(reversed("hello"))) # ['o', 'l', 'l', 'e', 'h']

# ── enumerate() — adds an index counter to any iterable ──────────────────────
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# 0 apple
# 1 banana
# 2 cherry

for index, fruit in enumerate(fruits, start=1):    # start from 1
    print(f"{index}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry

# ── zip() — pairs up items from multiple iterables ───────────────────────────
names  = ["Yash", "Prashant", "Aarav"]
scores = [95, 88, 76]
grades = ["A", "B", "C"]

for n, s, g in zip(names, scores, grades):
    print(f"{n}: {s} ({g})")
# Yash: 95 (A)
# Prashant: 88 (B)
# Aarav: 76 (C)

# zip stops at the shortest iterable
print(list(zip([1, 2, 3], ["a", "b"])))   # [(1, 'a'), (2, 'b')]

# ── map() — applies a function to every item ─────────────────────────────────
numbers = [1, 2, 3, 4, 5]

# Square every number
squares = list(map(lambda x: x ** 2, numbers))
print(squares)   # [1, 4, 9, 16, 25]

# Convert list of strings to integers
str_nums = ["10", "20", "30"]
int_nums = list(map(int, str_nums))
print(int_nums)   # [10, 20, 30]

# ── filter() — keeps only items where function returns True ──────────────────
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6, 8, 10]

words = ["", "Yash", "", "Python", ""]
non_empty = list(filter(None, words))   # None keeps truthy values
print(non_empty)   # ['Yash', 'Python']


# =============================================================================
# 6. OBJECT INFO FUNCTIONS
# =============================================================================

# ── id() — returns memory address of an object ───────────────────────────────
a = 10
b = 10
c = [1, 2]
d = [1, 2]

print(id(a))        # same as id(b) — Python caches small ints
print(id(b))
print(id(a) == id(b))   # True  — same object (cached)
print(id(c) == id(d))   # False — different list objects

# ── dir() — lists all attributes and methods of an object ────────────────────
print(dir("hello"))   # shows all string methods: upper, lower, split, ...
print(dir([]))        # shows all list methods: append, pop, sort, ...
# print(dir())        # shows names in current scope

# ── help() — shows documentation for any object or function ──────────────────
# Uncomment to test in terminal:
# help(str)
# help(print)
# help(list.append)

# ── callable() — checks if an object can be called like a function ─────────────
def greet():
    return "Hello"

print(callable(greet))   # True  — it's a function
print(callable(42))      # False — it's an integer

# ── vars() — returns the __dict__ of an object or current scope ───────────────
class Dog:
    def __init__(self):
        self.name  = "Bruno"
        self.breed = "Labrador"

dog = Dog()
print(vars(dog))   # {'name': 'Bruno', 'breed': 'Labrador'}


# =============================================================================
# 7. ITERATION / LOGIC FUNCTIONS
# =============================================================================

# ── all() — returns True if ALL items are truthy ─────────────────────────────
print(all([True, True, True]))    # True
print(all([True, False, True]))   # False
print(all([1, 2, 3]))             # True  — all non-zero
print(all([1, 0, 3]))             # False — 0 is falsy
print(all([]))                    # True  — vacuous truth (empty = all pass)

# Use case: validate all fields are filled
fields = ["Yash", "yash@email.com", "Delhi"]
print(all(fields))   # True — none are empty strings

# ── any() — returns True if AT LEAST ONE item is truthy ──────────────────────
print(any([False, False, True]))  # True
print(any([False, False, False])) # False
print(any([0, "", None]))         # False — all falsy
print(any([0, "", "Yash"]))       # True

# Use case: check if at least one permission is granted
permissions = [False, False, True, False]
print(any(permissions))   # True — at least one granted


# =============================================================================
# 8. STRING / CHARACTER FUNCTIONS
# =============================================================================

# ── repr() — returns a string with quotes and escape characters shown ─────────
print(repr("hello"))          # 'hello'    — with quotes
print(repr("line1\nline2"))   # 'line1\nline2'  — shows \n literally
print(repr(3.14))             # 3.14
print(repr([1, 2, 3]))        # [1, 2, 3]

# ── format() — formats a value as a string ───────────────────────────────────
print(format(3.14159, ".2f"))    # 3.14
print(format(1000000, ","))      # 1,000,000
print(format(255, "b"))          # 11111111  — binary
print(format(255, "x"))          # ff        — hexadecimal
print(format(255, "o"))          # 377       — octal
print(format("left", "<10"))     # "left      "  — left aligned in 10 chars
print(format("right", ">10"))    # "     right"  — right aligned

# ── chr() and ord() — convert between character and Unicode number ─────────────
print(chr(65))    # A
print(chr(97))    # a
print(chr(8364))  # €

print(ord("A"))   # 65
print(ord("a"))   # 97
print(ord("€"))   # 8364

# Practical: shift letters (simple cipher)
letter    = "A"
shifted   = chr(ord(letter) + 3)
print(shifted)    # D


# =============================================================================
# 9. MATH UTILITY FUNCTIONS
# =============================================================================

# ── bin(), oct(), hex() — convert integer to string in another base ─────────
print(bin(10))    # 0b1010   — binary
print(oct(10))    # 0o12     — octal
print(hex(255))   # 0xff     — hexadecimal
print(hex(255).upper())   # 0XFF

# Strip the prefix if you only want the digits
print(bin(10)[2:])    # 1010
print(hex(255)[2:])   # ff


# =============================================================================
# QUICK REFERENCE TABLE
# =============================================================================
#
#  Function        Category         What it does
#  ─────────────   ──────────────   ──────────────────────────────────────────
#  type(x)         Type Check       Returns the type of x
#  isinstance(x,T) Type Check       True if x is an instance of type T
#  int(x)          Conversion       Convert to integer
#  float(x)        Conversion       Convert to float
#  str(x)          Conversion       Convert to string
#  bool(x)         Conversion       Convert to boolean
#  list(x)         Conversion       Convert to list
#  tuple(x)        Conversion       Convert to tuple
#  set(x)          Conversion       Convert to set (removes duplicates)
#  dict(x)         Conversion       Convert to dictionary
#  input(prompt)   I/O              Read string from user
#  print(*args)    I/O              Print to console
#  abs(x)          Numeric          Absolute value
#  round(x, n)     Numeric          Round to n decimal places
#  pow(x, y)       Numeric          x to the power y
#  divmod(x, y)    Numeric          (quotient, remainder)
#  max(...)        Numeric          Largest value
#  min(...)        Numeric          Smallest value
#  sum(iterable)   Numeric          Sum of all items
#  len(x)          Sequence         Number of items
#  range(...)      Sequence         Generate number sequence
#  sorted(x)       Sequence         Return new sorted list
#  reversed(x)     Sequence         Return reverse iterator
#  enumerate(x)    Sequence         Add index counter to iterable
#  zip(...)        Sequence         Pair up items from iterables
#  map(fn, x)      Sequence         Apply function to each item
#  filter(fn, x)   Sequence         Keep items where fn returns True
#  id(x)           Object Info      Memory address of object
#  dir(x)          Object Info      List all attributes/methods
#  help(x)         Object Info      Show documentation
#  callable(x)     Object Info      True if x can be called
#  all(iterable)   Logic            True if all items are truthy
#  any(iterable)   Logic            True if any item is truthy
#  repr(x)         String           Unambiguous string representation
#  format(x, spec) String           Format value as string
#  chr(n)          String           Unicode number → character
#  ord(c)          String           Character → Unicode number
#  bin(n)          Math Utility     Integer → binary string
#  oct(n)          Math Utility     Integer → octal string
#  hex(n)          Math Utility     Integer → hexadecimal string


# =============================================================================
# PRACTICE QUESTIONS
# =============================================================================

# Q1. Ask the user for two numbers (as input), convert them to float,
#     and print their sum, difference, product, and quotient.
# ------ Solution ------
# num1 = float(input("Enter first number:  "))
# num2 = float(input("Enter second number: "))
# print(f"Sum: {num1+num2}, Diff: {num1-num2}, Prod: {num1*num2}, Div: {num1/num2:.2f}")

# (Static version for running without input prompt)
num1, num2 = 10.0, 4.0
print(f"Sum: {num1+num2}, Diff: {num1-num2}, Prod: {num1*num2}, Div: {num1/num2:.2f}")


# Q2. Use isinstance() to check if a value is int OR float.
#     Test with: 42, 3.14, "hello", True
# ------ Solution ------
test_vals = [42, 3.14, "hello", True]
for v in test_vals:
    result = isinstance(v, (int, float))
    print(f"{repr(v):10} is numeric: {result}")


# Q3. Given names = ["Prashant","Yash","Aarav","Meera"], use enumerate to
#     print a numbered list starting from 1.
# ------ Solution ------
names = ["Prashant", "Yash", "Aarav", "Meera"]
for i, n in enumerate(names, start=1):
    print(f"{i}. {n}")


# Q4. Use zip to combine two lists and create a dictionary.
#     keys = ["name","age","city"]   values = ["Yash", 20, "Delhi"]
# ------ Solution ------
keys   = ["name", "age", "city"]
values = ["Yash", 20, "Delhi"]
result = dict(zip(keys, values))
print(result)   # {'name': 'Yash', 'age': 20, 'city': 'Delhi'}


# Q5. Use map() to convert all strings in ["1","2","3","4"] to integers
#     and sum them.
# ------ Solution ------
str_list = ["1", "2", "3", "4"]
total    = sum(map(int, str_list))
print(total)   # 10


# Q6. Use filter() to keep only even numbers from 1 to 20.
# ------ Solution ------
evens = list(filter(lambda x: x % 2 == 0, range(1, 21)))
print(evens)   # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# Q7. Use all() to check if every element in a list is positive.
# ------ Solution ------
nums = [3, 7, 12, -1, 5]
print(all(n > 0 for n in nums))   # False — -1 is not positive


# Q8. Use chr() and ord() to print the alphabet A–Z.
# ------ Solution ------
alphabet = "".join(chr(i) for i in range(ord("A"), ord("Z") + 1))
print(alphabet)   # ABCDEFGHIJKLMNOPQRSTUVWXYZ

