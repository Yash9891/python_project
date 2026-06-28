# =============================================================================
#  PYTHON CONDITIONAL STATEMENTS — Complete Reference Guide
#  Author  : Yash
#  Purpose : Understand conditional statements in Python from scratch
#  Topics  : if / elif / else, comparison operators, logical operators,
#            membership operators, nested conditions, ternary expressions
# =============================================================================


# =============================================================================
# SECTION 1 — WHAT IS A CONDITIONAL STATEMENT?
# =============================================================================
# A conditional statement lets your program make decisions.
# Python evaluates a condition (True or False) and executes only the
# matching block of code.
#
# Syntax:
#   if <condition>:
#       <code block>          ← runs when condition is True
#   elif <another condition>:
#       <code block>          ← runs when the first is False, this is True
#   else:
#       <code block>          ← runs when ALL above conditions are False
#
# Rules:
#   • Indentation (4 spaces) defines the block — Python has no braces {}
#   • elif and else are optional
#   • You can chain as many elif blocks as you need


# =============================================================================
# SECTION 2 — COMPARISON OPERATORS (produce True / False)
# =============================================================================
# Operator  Meaning                    Example
# --------  -------------------------  ----------
#   ==      equal to                   5 == 5  → True
#   !=      not equal to               5 != 3  → True
#   >       greater than               7 > 4   → True
#   <       less than                  2 < 9   → True
#   >=      greater than or equal to   5 >= 5  → True
#   <=      less than or equal to      3 <= 6  → True


# =============================================================================
# SECTION 3 — BASIC if / elif / else
# =============================================================================

age = 25

if age < 13:
    print("Child (under 13)")
elif age < 18:
    print("Teenager (13–17)")
elif age < 60:
    print("Adult (18–59)")       # ← This block runs for age = 25
else:
    print("Senior (60+)")

# Output: Adult (18–59)


# =============================================================================
# SECTION 4 — LOGICAL OPERATORS: and / or / not
# =============================================================================
# Combine multiple conditions in one expression.
#
#   and  → BOTH conditions must be True
#   or   → AT LEAST ONE condition must be True
#   not  → INVERTS the condition (True becomes False, False becomes True)

temperature = 28
is_raining  = False

# Using 'and'
if temperature > 25 and not is_raining:
    print("Great day for a walk!")   # ← runs: both conditions are True

# Using 'or'
score = 45
if score < 40 or score > 100:
    print("Invalid score")
else:
    print("Score is valid")          # ← runs


# =============================================================================
# SECTION 5 — MEMBERSHIP OPERATOR: in / not in
# =============================================================================
# Check whether a value exists inside a list, tuple, string, or dictionary.

fruits = ["apple", "banana", "mango", "grape"]

search = "mango"

if search in fruits:
    print(f"'{search}' is in the list.")     # ← runs
else:
    print(f"'{search}' is NOT in the list.")

# Check absence
if "cherry" not in fruits:
    print("Cherry is not available.")        # ← runs


# =============================================================================
# SECTION 6 — NESTED CONDITIONALS
# =============================================================================
# An if block can contain another if block inside it.
# Use sparingly — deep nesting hurts readability.

username   = "yash"
is_logged_in = True
is_admin   = False

if is_logged_in:
    if is_admin:
        print("Welcome, Admin! Access to dashboard granted.")
    else:
        print(f"Welcome, {username}! You have standard access.")  # ← runs
else:
    print("Please log in to continue.")


# =============================================================================
# SECTION 7 — TERNARY (ONE-LINE) CONDITIONAL EXPRESSION
# =============================================================================
# Compact form for simple if/else assignments.
#
# Syntax:  value_if_true  if  condition  else  value_if_false

marks = 72

result = "Pass" if marks >= 50 else "Fail"
print(result)   # Pass

# Equivalent long form:
# if marks >= 50:
#     result = "Pass"
# else:
#     result = "Fail"


# =============================================================================
# SECTION 8 — REAL-WORLD EXAMPLE: ATM PIN VALIDATOR
# =============================================================================

def atm_check(balance: float, pin_entered: int, correct_pin: int) -> None:
    """Simulate a basic ATM access check."""

    if pin_entered != correct_pin:
        print("❌ Incorrect PIN. Access denied.")
    elif balance <= 0:
        print("⚠️  Your account balance is zero.")
    elif balance < 500:
        print(f"✅ Access granted. Low balance warning: ₹{balance:.2f}")
    else:
        print(f"✅ Access granted. Available balance: ₹{balance:.2f}")


atm_check(balance=1500.0, pin_entered=1234, correct_pin=1234)
# Output: ✅ Access granted. Available balance: ₹1500.00

atm_check(balance=200.0, pin_entered=9999, correct_pin=1234)
# Output: ❌ Incorrect PIN. Access denied.


# =============================================================================
# SECTION 9 — ORIGINAL CODE (CORRECTED & EXPLAINED)
# =============================================================================

age = 10

# Corrected: age 10 is NOT an adult — fixed the print message
if age < 12:
    print(f"Person is a child. Age: {age}")        # ← runs (age = 10)
elif age > 80:
    print(f"Person is a senior. Age: {age}")
else:
    print(f"Person is an adult. Age: {age}")


# Membership check on a list
numbers = [34, 56, 68, 234, 23]

if 348 in numbers:
    print("348 is present in the list.")
else:
    print("348 is NOT in the list.")               # ← runs


# Logical 'or' condition (corrected label)
age = 10
if age > 18 or age < 5:                           # True adult OR very young child
    print("Special category.")
else:
    print("Regular child/pre-adult range.")        # ← runs (age = 10)


# =============================================================================
# SECTION 10 — PRACTICE QUESTIONS
# =============================================================================
#
# ── Beginner ──────────────────────────────────────────────────────────────────
#
# Q1. Write a program that accepts a number and prints whether it is
#     Positive, Negative, or Zero.
#
# Q2. A shop gives discounts based on purchase amount:
#       < ₹500   → No discount
#       ₹500–999 → 10% discount
#       ≥ ₹1000  → 20% discount
#     Print the final amount after discount.
#
# Q3. Check if a given year is a leap year.
#     (Hint: divisible by 4, but not 100 — unless also divisible by 400)
#
# ── Intermediate ──────────────────────────────────────────────────────────────
#
# Q4. Take three numbers and print the largest without using max().
#
# Q5. A traffic light system:
#       "red"    → "Stop"
#       "yellow" → "Slow down"
#       "green"  → "Go"
#       anything else → "Invalid signal"
#
# Q6. A student's grade calculator:
#       90–100 → "A"   |   80–89 → "B"   |   70–79 → "C"
#       60–69  → "D"   |   below 60 → "F"
#
# ── Advanced ──────────────────────────────────────────────────────────────────
#
# Q7. Build a simple login system:
#     - Stored username: "admin", password: "python123"
#     - Accept input and check credentials
#     - Allow 3 attempts before locking out
#
# Q8. Given a list of integers, print only those that are:
#     - Greater than 10   AND
#     - Even numbers      AND
#     - Present in a second "allowed" list


# =============================================================================
# SECTION 11 — SOLUTIONS TO SELECTED QUESTIONS
# =============================================================================

# ── Solution: Q1 — Positive / Negative / Zero ─────────────────────────────────
number = -7

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")    # ← runs
else:
    print("Zero")


# ── Solution: Q3 — Leap Year ──────────────────────────────────────────────────
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")    # ← runs
else:
    print(f"{year} is NOT a Leap Year.")


# ── Solution: Q5 — Traffic Light ──────────────────────────────────────────────
signal = "green"

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Slow down")
elif signal == "green":
    print("Go")           # ← runs
else:
    print("Invalid signal")


# ── Solution: Q6 — Grade Calculator ──────────────────────────────────────────
marks = 85

if 90 <= marks <= 100:
    grade = "A"
elif 80 <= marks < 90:
    grade = "B"           # ← runs
elif 70 <= marks < 80:
    grade = "C"
elif 60 <= marks < 70:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")  # Grade: B


# ── Solution: Q8 — Filtered List ──────────────────────────────────────────────
values  = [5, 14, 22, 7, 30, 11, 18, 3, 40]
allowed = [14, 22, 30, 40, 99]

for val in values:
    if val > 10 and val % 2 == 0 and val in allowed:
        print(val)        # Prints: 14, 22, 30, 40


# =============================================================================
# QUICK RECAP
# =============================================================================
# ✅  if / elif / else     → decision making
# ✅  ==, !=, >, <, >=, <= → comparison operators
# ✅  and / or / not       → logical operators
# ✅  in / not in          → membership operators
# ✅  Nested if            → conditions inside conditions
# ✅  Ternary expression   → one-line if/else for simple cases
# =============================================================================