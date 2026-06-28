# =============================================================================
#  PYTHON VARIABLES — Complete Reference Guide
#  Author  : Yash
#  Purpose : Understand variables in Python from scratch
# =============================================================================


# -----------------------------------------------------------------------------
# 1. WHAT IS A VARIABLE?
# -----------------------------------------------------------------------------
# A variable is a named container that stores a value in memory.
# Think of it as a labelled box — you put something inside it and refer to it
# later using the label (the variable name).
#
# Syntax:
#   variable_name = value
#
# Python is dynamically typed, which means you do NOT declare the type
# explicitly — Python figures it out automatically.

age = 23                  # integer
name = "Yash"             # string
height = 5.9              # float
is_student = True         # boolean

print(age)                # Output: 23
print(name)               # Output: Yash
print(height)             # Output: 5.9
print(is_student)         # Output: True


# -----------------------------------------------------------------------------
# 2. VARIABLE NAMING RULES  (must follow — or Python raises a SyntaxError)
# -----------------------------------------------------------------------------

# RULE 1 — Use letters, digits, and underscores ONLY
valid_name   = "Yash"     # ✅ correct
_private_var = 42         # ✅ underscore prefix is allowed
var5777      = "hello"    # ✅ digits are fine — but NOT at the start

# RULE 2 — Must NOT start with a digit
# 9var = "error"          # ❌ SyntaxError: invalid syntax

# RULE 3 — No special characters anywhere in the name
# $name   = "Yash"        # ❌ SyntaxError
# my-var  = 10            # ❌ SyntaxError (hyphen is subtraction)
# var@end = "hello"       # ❌ SyntaxError
# user#id = 1             # ❌ SyntaxError

# RULE 4 — Cannot be a Python keyword
# for = 5                 # ❌ SyntaxError — 'for' is a reserved keyword
# if  = 10                # ❌ SyntaxError

# View all keywords:
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
#  'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
#  'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
#  'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
#  'while', 'with', 'yield']


# -----------------------------------------------------------------------------
# 3. NAMING CONVENTIONS  (best practices — not enforced by Python, but expected)
# -----------------------------------------------------------------------------

# snake_case  — recommended for variables and functions (PEP 8 standard)
first_name   = "Yash"
total_marks  = 95

# UPPER_SNAKE_CASE — for constants (values that should not change)
MAX_SPEED    = 120
PI           = 3.14159

# CamelCase / PascalCase — for class names (covered later)
# class StudentRecord: ...

# Avoid single letters except as loop counters
x = 10          # ok for maths or quick tests
i = 0           # ok inside loops

# Avoid names that shadow built-ins
# list = [1, 2, 3]    # ⚠️  shadows the built-in 'list' — use my_list instead


# -----------------------------------------------------------------------------
# 4. DYNAMIC TYPING — same variable, different types
# -----------------------------------------------------------------------------
# Python allows you to reassign a variable to a completely different type.

data = 100          # data is an int
print(type(data))   # <class 'int'>

data = "hello"      # now data is a str
print(type(data))   # <class 'str'>

data = [1, 2, 3]    # now data is a list
print(type(data))   # <class 'list'>


# -----------------------------------------------------------------------------
# 5. MULTIPLE ASSIGNMENT
# -----------------------------------------------------------------------------

# Assign the same value to multiple variables in one line
a = b = c = 0
print(a, b, c)      # 0 0 0

# Assign different values in one line (tuple unpacking)
x, y, z = 10, 20, 30
print(x, y, z)      # 10 20 30

# Swap two variables — Python makes this elegant
x, y = y, x
print(x, y)         # 20 10


# -----------------------------------------------------------------------------
# 6. TYPE CHECKING AND CONVERSION
# -----------------------------------------------------------------------------

num   = 42
text  = "100"
price = 9.99

# Check type
print(type(num))    # <class 'int'>
print(type(text))   # <class 'str'>
print(type(price))  # <class 'float'>

# Convert types (type casting)
print(int(text))    # 100  — string "100" → integer 100
print(float(num))   # 42.0 — integer 42  → float 42.0
print(str(num))     # "42" — integer 42  → string "42"
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False — empty string is falsy


# -----------------------------------------------------------------------------
# 7. SCOPE — where a variable lives
# -----------------------------------------------------------------------------

global_var = "I am global"   # accessible everywhere in this file

def my_function():
    local_var = "I am local"  # only accessible inside this function
    print(global_var)         # ✅ can read the global variable
    print(local_var)          # ✅ local variable is visible here

my_function()
# print(local_var)            # ❌ NameError — local_var doesn't exist outside


# Using 'global' keyword to modify a global variable inside a function
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)   # 2


# -----------------------------------------------------------------------------
# 8. CONSTANTS (convention only — Python has no true const keyword)
# -----------------------------------------------------------------------------
# By convention, write constants in ALL_CAPS to signal "don't change this."

GRAVITY       = 9.8        # m/s²
SPEED_OF_LIGHT = 3e8       # metres per second
APP_NAME      = "MyApp"

# Python won't stop you from reassigning them, but teammates (and your future
# self) will understand they are meant to be fixed values.


# -----------------------------------------------------------------------------
# 9. DELETING A VARIABLE
# -----------------------------------------------------------------------------

temp = "temporary value"
print(temp)   # temporary value

del temp
# print(temp) # ❌ NameError: name 'temp' is not defined


# -----------------------------------------------------------------------------
# 10. QUICK REFERENCE SUMMARY
# -----------------------------------------------------------------------------
#
#  ✅ Valid names        ❌ Invalid names
#  ─────────────────     ─────────────────────────────────
#  name                  9name   (starts with digit)
#  _name                 my-name (hyphen = minus operator)
#  name9                 my name (space not allowed)
#  my_name               $name   ($ not allowed)
#  MY_CONSTANT           for     (reserved keyword)
#
#  Conventions (PEP 8):
#  • Variables  → snake_case        (my_variable)
#  • Constants  → UPPER_SNAKE_CASE  (MAX_SIZE)
#  • Classes    → PascalCase        (MyClass)
#
#  Key functions:
#  • type(x)    → returns the data type of x
#  • id(x)      → returns the memory address of x
#  • del x      → removes the variable from memory
#  • isinstance(x, int) → True/False type check


# =============================================================================
# PRACTICE QUESTIONS
# =============================================================================

# Q1. Create variables to store your name, age, and GPA. Print all three.
# ------ Solution ------
student_name = "Yash"
student_age  = 20
student_gpa  = 8.7
print(student_name, student_age, student_gpa)


# Q2. What is wrong with the following? Fix it.
#     1name = "Alice"
#     my-score = 99
#     for = 10
# ------ Solution ------
name_1   = "Alice"   # moved digit to the end
my_score = 99        # replaced hyphen with underscore
score    = 10        # renamed — 'for' is a keyword


# Q3. Swap the values of x and y without using a third variable.
# ------ Solution ------
x = 5
y = 10
x, y = y, x
print("x =", x, "| y =", y)   # x = 10 | y = 5


# Q4. Assign the value 50 to variables p, q, and r in a single line.
# ------ Solution ------
p = q = r = 50
print(p, q, r)   # 50 50 50


# Q5. Convert the string "3.14" to a float and multiply it by 2. Print the result.
# ------ Solution ------
pi_str    = "3.14"
pi_float  = float(pi_str)
print(pi_float * 2)   # 6.28


# Q6. Check the type of each: 42, 3.14, "hello", True, [1, 2, 3]
# ------ Solution ------
values = [42, 3.14, "hello", True, [1, 2, 3]]
for v in values:
    print(f"{repr(v):15} → {type(v).__name__}")


# Q7. Create a constant for the value of gravity (9.8) and use it to
#     calculate the weight of a 70 kg object. (weight = mass × gravity)
# ------ Solution ------
GRAVITY = 9.8
mass    = 70
weight  = mass * GRAVITY
print(f"Weight = {weight} N")   # Weight = 686.0 N


# Q8. Write a function that increments a global variable 'score' by 10
#     each time it is called. Call it 3 times and print the final score.
# ------ Solution ------
score = 0

def add_points():
    global score
    score += 10

add_points()
add_points()
add_points()
print("Final score:", score)   # Final score: 30

