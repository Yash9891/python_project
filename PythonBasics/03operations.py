# =============================================================================
#  PYTHON OPERATORS — Complete Reference Guide
#  Author  : Yash
#  Purpose : Understand all types of operators in Python from scratch
# =============================================================================


# -----------------------------------------------------------------------------
# WHAT IS AN OPERATOR?
# -----------------------------------------------------------------------------
# An operator is a symbol that performs an operation on one or more values
# (called operands).
#
# Python has 7 categories of operators:
#   1. Arithmetic      →  +  -  *  /  //  %  **
#   2. Assignment      →  =  +=  -=  *=  /=  //=  %=  **=  &=  |=  ^=
#   3. Comparison      →  ==  !=  >  <  >=  <=
#   4. Logical         →  and  or  not
#   5. Bitwise         →  &  |  ^  ~  <<  >>
#   6. Identity        →  is  is not
#   7. Membership      →  in  not in


# =============================================================================
# 1. ARITHMETIC OPERATORS
# =============================================================================
# Used to perform basic mathematical operations.

num1 = 10
num2 = 3

print(num1 +  num2)   # 13   — Addition
print(num1 -  num2)   # 7    — Subtraction
print(num1 *  num2)   # 30   — Multiplication
print(num1 /  num2)   # 3.333...  — Division (always returns float)
print(num1 // num2)   # 3    — Floor Division (drops the decimal)
print(num1 %  num2)   # 1    — Modulus (remainder after division)
print(num1 ** num2)   # 1000 — Exponentiation (10 to the power 3)

# ── Practical examples ────────────────────────────────────────────────────────

# Check if a number is even or odd using modulus
number = 17
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")    # 17 is Odd

# Floor division use case — split items equally
total_chocolates = 25
children         = 4
each_gets        = total_chocolates // children    # 6
leftover         = total_chocolates %  children    # 1
print(f"Each child gets {each_gets}, leftover: {leftover}")

# Important: / always gives float, // gives int (when both operands are int)
print(10 / 2)    # 5.0  ← float
print(10 // 2)   # 5    ← int

# Operator precedence (BODMAS / PEMDAS applies)
result = 2 + 3 * 4 ** 2 - 1
#             ↑ first: 4**2 = 16
#         ↑ second: 3*16 = 48
#     ↑ third: 2+48 = 50
# ↑ last: 50-1 = 49
print(result)    # 49
print(2 + (3 * (4 ** 2)) - 1)   # same — use parentheses for clarity


# =============================================================================
# 2. ASSIGNMENT OPERATORS
# =============================================================================
# Used to assign values to variables.
# Compound assignment operators are shorthand: a += b  means  a = a + b

a = 10   # simple assignment

# Compound assignment
a += 5    # a = a + 5  → 15
print(a)  # 15

a -= 3    # a = a - 3  → 12
print(a)  # 12

a *= 2    # a = a * 2  → 24
print(a)  # 24

a /= 4    # a = a / 4  → 6.0  (note: becomes float)
print(a)  # 6.0

a //= 2   # a = a // 2 → 3.0
print(a)  # 3.0

a **= 3   # a = a ** 3 → 27.0
print(a)  # 27.0

a %= 5    # a = a % 5  → 2.0
print(a)  # 2.0

# ── String and list assignment ────────────────────────────────────────────────
name  = "Yash"
name += " Sharma"    # string concatenation via +=
print(name)          # Yash Sharma

items  = [1, 2, 3]
items += [4, 5]      # list extension via +=
print(items)         # [1, 2, 3, 4, 5]

# ── Walrus operator  :=  (Python 3.8+) ───────────────────────────────────────
# Assigns AND returns a value inside an expression (the "assignment expression")
import random
numbers = [random.randint(1, 100) for _ in range(10)]

if (n := len(numbers)) > 5:
    print(f"List is long: {n} items")   # List is long: 10 items


# =============================================================================
# 3. COMPARISON (RELATIONAL) OPERATORS
# =============================================================================
# Compare two values and always return True or False.

num1 = 10
num2 = 20

print(num1 == num2)   # False — Equal to
print(num1 != num2)   # True  — Not equal to
print(num1 >  num2)   # False — Greater than
print(num1 <  num2)   # True  — Less than
print(num1 >= num2)   # False — Greater than or equal to
print(num1 <= num2)   # True  — Less than or equal to

# Works on strings too (compares alphabetically by Unicode value)
name1 = "Yash"
name2 = "Yash"
name3 = "Prashant"

print(name1 == name2)   # True
print(name1 == name3)   # False
print("apple" < "banana")   # True — 'a' comes before 'b'

# Chained comparisons — Pythonic and readable
age = 25
print(18 <= age <= 60)   # True — checks both conditions at once

marks = 75
grade = "A" if marks >= 90 else "B" if marks >= 75 else "C"
print(grade)   # B


# =============================================================================
# 4. LOGICAL OPERATORS
# =============================================================================
# Combine multiple conditions. Operate on boolean values (or truthy/falsy).
#
# TRUTHY  → any non-zero number, non-empty string/list/dict/set, True
# FALSY   → 0, 0.0, "", [], {}, set(), None, False

# ── and — returns True only when BOTH sides are truthy ───────────────────────
print(True  and True)    # True
print(True  and False)   # False
print(False and True)    # False
print(False and False)   # False

# 'and' returns the first falsy value, or the last value if all are truthy
print("Yash" and 100)    # 100       ← both truthy → returns last
print(""     and 100)    # ""        ← "" is falsy → returns first falsy
print(0      and "hi")   # 0         ← 0 is falsy  → returns first falsy

# ── or — returns True when AT LEAST ONE side is truthy ───────────────────────
print(True  or False)    # True
print(False or True)     # True
print(False or False)    # False

# 'or' returns the first truthy value, or the last value if all are falsy
print("Yash" or "Guest")   # "Yash"   ← first truthy
print(""     or "Guest")   # "Guest"  ← "" is falsy, so returns next
print(0      or False)     # False    ← all falsy → returns last

# ── not — reverses the boolean value ─────────────────────────────────────────
print(not True)      # False
print(not False)     # True
print(not "Yash")    # False — "Yash" is truthy, not makes it False
print(not "")        # True  — "" is falsy, not makes it True
print(not 0)         # True
print(not 42)        # False

# ── Real-world logical operator examples ─────────────────────────────────────
name     = "Yash"
is_admin = True
age      = 20

# Login check
if name == "Yash" and is_admin:
    print("Welcome, Admin Yash!")

# Default value using 'or'
username = ""
display  = username or "Guest"
print(f"Hello, {display}!")   # Hello, Guest!

# Toggle a boolean using 'not'
is_dark_mode = False
is_dark_mode = not is_dark_mode
print(is_dark_mode)   # True


# =============================================================================
# 5. BITWISE OPERATORS
# =============================================================================
# Operate on integers at the binary (bit) level.
#   &   AND       →  1 only if both bits are 1
#   |   OR        →  1 if at least one bit is 1
#   ^   XOR       →  1 if bits are different
#   ~   NOT       →  flips all bits  (~n = -(n+1))
#   <<  Left shift  →  multiply by 2 for each shift
#   >>  Right shift →  divide by 2 for each shift

a = 10   # binary: 1010
b = 6    # binary: 0110

print(a &  b)   # 2   → 0010
print(a |  b)   # 14  → 1110
print(a ^  b)   # 12  → 1100
print(~a)       # -11 → -(10+1)
print(a << 1)   # 20  → 10 * 2
print(a >> 1)   # 5   → 10 / 2

# Practical: check if a number is even using bitwise AND
num = 14
if num & 1 == 0:
    print(f"{num} is Even")   # 14 is Even


# =============================================================================
# 6. IDENTITY OPERATORS  (is / is not)
# =============================================================================
# Check whether two variables point to the SAME object in memory.
# Different from == which checks VALUE equality.

a = [1, 2, 3]
b = [1, 2, 3]
c = a             # c points to the SAME list as a

print(a == b)     # True  — same values
print(a is b)     # False — different objects in memory
print(a is c)     # True  — c IS the same object as a

print(id(a))      # memory address of a
print(id(b))      # different address
print(id(c))      # same address as a

# Python caches small integers (-5 to 256) and short strings
x = 100
y = 100
print(x is y)    # True — cached, same object

p = 1000
q = 1000
print(p is q)    # False — not cached, different objects

# RULE: use 'is' only to check for None, True, False
result = None
if result is None:
    print("No result yet")         # ✅ correct
if result == None:
    print("Also works but bad practice")   # ⚠️ use 'is' instead


# =============================================================================
# 7. MEMBERSHIP OPERATORS  (in / not in)
# =============================================================================
# Check whether a value exists inside a sequence (string, list, tuple,
# set, dict keys).

fruits = ["apple", "banana", "mango"]

print("apple"  in     fruits)   # True
print("cherry" in     fruits)   # False
print("cherry" not in fruits)   # True

# Works on strings
sentence = "Python is awesome"
print("Python"  in sentence)    # True
print("Java"    in sentence)    # False
print("is" not in sentence)     # False

# Works on dictionaries (checks KEYS by default)
student = {"name": "Yash", "age": 20}
print("name"  in student)       # True
print("Yash"  in student)       # False — checks keys, not values
print("Yash"  in student.values())   # True — explicitly check values

# Works on sets (fastest lookup — O(1))
allowed_users = {"Yash", "Prashant", "Aarav"}
user = "Yash"
if user in allowed_users:
    print(f"{user} is allowed")


# =============================================================================
# OPERATOR PRECEDENCE  (highest to lowest)
# =============================================================================
# When multiple operators appear in one expression, Python follows this order:
#
#  Priority   Operator(s)              Description
#  ────────   ──────────────────────   ──────────────────────────
#  1 (high)   ()                       Parentheses
#  2          **                       Exponentiation
#  3          ~  +x  -x                Bitwise NOT, Unary +/-
#  4          *  /  //  %              Multiply, Divide, Floor, Mod
#  5          +  -                     Addition, Subtraction
#  6          <<  >>                   Bitwise Shift
#  7          &                        Bitwise AND
#  8          ^                        Bitwise XOR
#  9          |                        Bitwise OR
#  10         ==  !=  >  <  >=  <=    Comparison
#             is  is not  in  not in
#  11         not                      Logical NOT
#  12         and                      Logical AND
#  13 (low)   or                       Logical OR

# Example — what does this evaluate to?
result = 3 + 2 ** 3 * 2 - 1 and not False or 5 > 3
# Step 1: 2**3 = 8
# Step 2: 8*2  = 16
# Step 3: 3+16 = 19
# Step 4: 19-1 = 18  → truthy
# Step 5: not False  = True
# Step 6: 18 and True = True
# Step 7: 5 > 3 = True
# Step 8: True or True = True
print(result)   # True

# TIP: when in doubt, use parentheses — it costs nothing and saves bugs.


# =============================================================================
# QUICK REFERENCE TABLE
# =============================================================================
#
#  Category    Operators                      Returns
#  ──────────  ─────────────────────────────  ─────────────────────────
#  Arithmetic  + - * / // % **                Number
#  Assignment  = += -= *= /= //= %= **=       (modifies variable)
#  Comparison  == != > < >= <=                True / False
#  Logical     and  or  not                   Truthy/falsy value
#  Bitwise     & | ^ ~ << >>                  Integer
#  Identity    is  is not                     True / False
#  Membership  in  not in                     True / False


# =============================================================================
# PRACTICE QUESTIONS
# =============================================================================

# Q1. Given a = 15 and b = 4, print the result of all 7 arithmetic operators.
# ------ Solution ------
a, b = 15, 4
print(f"Add: {a+b}, Sub: {a-b}, Mul: {a*b}, Div: {a/b:.2f}")
print(f"FloorDiv: {a//b}, Mod: {a%b}, Power: {a**b}")


# Q2. Start with x = 100. Apply -= 25, then *= 2, then //= 3. Print after each step.
# ------ Solution ------
x  = 100
x -= 25;  print(x)    # 75
x *= 2;   print(x)    # 150
x //= 3;  print(x)    # 50


# Q3. Without running the code, predict the output. Then verify.
#     print(5 > 3 and 10 != 10)
#     print(5 > 3 or  10 != 10)
#     print(not (5 > 3))
# ------ Solution ------
print(5 > 3 and 10 != 10)   # False  (True and False → False)
print(5 > 3 or  10 != 10)   # True   (True or  False → True)
print(not (5 > 3))           # False  (not True → False)


# Q4. Check whether a user-entered year is a leap year.
#     A year is a leap year if divisible by 4, except centuries
#     unless also divisible by 400.
# ------ Solution ------
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"{year} is {'a leap' if is_leap else 'not a leap'} year")


# Q5. Use membership operators to validate an email domain.
#     Given email = "yash@gmail.com", check if it contains "@" and ends with ".com"
# ------ Solution ------
email = "yash@gmail.com"
if "@" in email and email.endswith(".com"):
    print("Valid email format")
else:
    print("Invalid email format")


# Q6. Use identity operators to check if two variables point to the same object.
#     a = [10, 20]   b = a   c = [10, 20]
# ------ Solution ------
a = [10, 20]
b = a
c = [10, 20]
print(a is b)    # True  — same object
print(a is c)    # False — equal values but different objects
print(a == c)    # True  — same values


# Q7. Use bitwise operators to:
#     (a) check if 28 is even
#     (b) multiply 7 by 8 using left shift only
# ------ Solution ------
print(28 & 1 == 0)   # True — even
print(7 << 3)        # 56   — 7 * (2**3) = 7 * 8


# Q8. Write a program that takes a marks value and prints the grade using
#     comparison + logical operators (no if-elif chain — use a dict or ternary).
# ------ Solution ------
marks = 82
grade = (
    "A+" if marks >= 95 else
    "A"  if marks >= 85 else
    "B"  if marks >= 75 else
    "C"  if marks >= 60 else
    "D"  if marks >= 40 else
    "F"
)
print(f"Marks: {marks} → Grade: {grade}")   # Marks: 82 → Grade: B


