# =============================================================================
#  PYTHON TUPLES — Complete Reference Guide
#  Author  : Yash
#  Purpose : Understand tuples in Python from scratch
# =============================================================================


# -----------------------------------------------------------------------------
# WHAT IS A TUPLE?
# -----------------------------------------------------------------------------
# A tuple is an ordered, immutable sequence that can hold items of any type.
# Once created, its elements CANNOT be changed, added, or removed.
# Tuples allow duplicate values.
# Defined with round brackets ( )
#
#  Property        Tuple       List
#  ─────────────   ─────────   ────────
#  Ordered         Yes         Yes
#  Mutable         No ✗        Yes ✓
#  Duplicates      Yes         Yes
#  Syntax          (1, 2, 3)   [1, 2, 3]
#  Speed           Faster      Slightly slower
#  Dict key        Yes ✓       No ✗


# =============================================================================
# 1. CREATING TUPLES
# =============================================================================

empty_tuple  = ()                          # empty tuple
single_item  = (42,)                       # ⚠️ trailing comma is REQUIRED
                                           #    (42) alone is just an integer
numbers      = (10, 23, 45)               # integers
names        = ("Yash", "Prashant", "Rohit", "Prashant")  # strings (duplicates OK)
mixed        = (1, "hello", 3.14, True, None)              # mixed types
nested       = ((1, 2), (3, 4), (5, 6))  # tuple of tuples

print(numbers)      # (10, 23, 45)
print(names)        # ('Yash', 'Prashant', 'Rohit', 'Prashant')
print(mixed)        # (1, 'hello', 3.14, True, None)
print(single_item)  # (42,)

# Create a tuple using tuple()
from_range  = tuple(range(1, 6))    # (1, 2, 3, 4, 5)
from_string = tuple("Yash")         # ('Y', 'a', 's', 'h')
from_list   = tuple([10, 20, 30])   # (10, 20, 30) — convert list to tuple
print(from_range)
print(from_string)
print(from_list)

# Tuple packing — no parentheses needed
packed = 1, 2, 3
print(packed)        # (1, 2, 3)
print(type(packed))  # <class 'tuple'>


# =============================================================================
# 2. INDEXING AND SLICING
# =============================================================================
# Same index rules as lists and strings.
# Positive index starts at 0 (left), negative index starts at -1 (right).

names = ("Yash", "Prashant", "Rohit", "Aarav", "Meera")
#          0         1          2        3         4
#         -5        -4         -3       -2        -1

print(names[0])      # Yash     — first item
print(names[2])      # Rohit
print(names[-1])     # Meera    — last item
print(names[-2])     # Aarav

# Slicing   [start : stop : step]  — stop is EXCLUSIVE
print(names[1:3])    # ('Prashant', 'Rohit')
print(names[:3])     # ('Yash', 'Prashant', 'Rohit')
print(names[2:])     # ('Rohit', 'Aarav', 'Meera')
print(names[::2])    # ('Yash', 'Rohit', 'Meera')  — every 2nd item
print(names[::-1])   # ('Meera', 'Aarav', 'Rohit', 'Prashant', 'Yash')  — reversed

# ⚠️  Indexing works on tuples. It does NOT work on sets and dictionaries.


# =============================================================================
# 3. IMMUTABILITY — The Core Rule
# =============================================================================
# Tuples are IMMUTABLE — you CANNOT change, add, or remove elements.
# Any attempt will raise a TypeError.

t = (10, 23, 45)
print(t)           # (10, 23, 45)

# t[0] = 100       # ❌ TypeError: 'tuple' object does not support item assignment
# t.append(99)     # ❌ AttributeError: 'tuple' object has no attribute 'append'
# t.remove(10)     # ❌ AttributeError: 'tuple' object has no attribute 'remove'

# ── Workaround — convert to list, modify, convert back ───────────────────────
temp      = list(t)    # (10, 23, 45) → [10, 23, 45]
temp[0]   = 100
t_updated = tuple(temp)
print("Updated:", t_updated)   # (100, 23, 45)
print("Original unchanged:", t)  # (10, 23, 45)

# ── Mutable objects INSIDE a tuple CAN be changed ────────────────────────────
mutable_inside = ([1, 2], [3, 4])
mutable_inside[0].append(99)     # modifying the list inside — this works!
print(mutable_inside)            # ([1, 2, 99], [3, 4])


# =============================================================================
# 4. BUILT-IN TUPLE METHODS
# =============================================================================
# Tuples have only 2 built-in methods (because they're immutable).

b = (5, 3, 8, 3, 9, 3, 1)

# ── count() — number of times a value appears ─────────────────────────────────
print(b.count(3))    # 3  — 3 appears three times
print(b.count(5))    # 1
print(b.count(99))   # 0  — no error if not found (unlike index)

# ── index() — returns index of FIRST occurrence ───────────────────────────────
print(b.index(8))    # 2  — position of 8
print(b.index(3))    # 1  — position of FIRST 3 (not all)
# print(b.index(99)) # ❌ ValueError: tuple.index(x): x not in tuple

# Safe index search
if 99 in b:
    print(b.index(99))
else:
    print("Value not found")


# =============================================================================
# 5. USEFUL BUILT-IN FUNCTIONS WITH TUPLES
# =============================================================================

nums = (4, 1, 9, 2, 7)

print(len(nums))      # 5   — number of elements
print(min(nums))      # 1   — smallest value
print(max(nums))      # 9   — largest value
print(sum(nums))      # 23  — total (numeric tuples only)
print(sorted(nums))   # [1, 2, 4, 7, 9] — returns a NEW sorted LIST (tuple unchanged)
print(list(nums))     # [4, 1, 9, 2, 7] — convert to list

# reversed() — returns an iterator (wrap in tuple to see result)
print(tuple(reversed(nums)))   # (7, 2, 9, 1, 4)

# any() and all()
flags = (True, False, True)
print(any(flags))    # True  — at least one is True
print(all(flags))    # False — not all are True


# =============================================================================
# 6. TUPLE OPERATIONS
# =============================================================================

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# ── Concatenation (+) — creates a NEW tuple ───────────────────────────────────
print(t1 + t2)       # (1, 2, 3, 4, 5, 6)

# ── Repetition (*) — repeats the tuple ───────────────────────────────────────
print(t1 * 3)        # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# ── Membership (in / not in) ──────────────────────────────────────────────────
print(2 in t1)       # True
print(9 in t1)       # False
print(9 not in t1)   # True

# ── Comparison ────────────────────────────────────────────────────────────────
print((1, 2, 3) == (1, 2, 3))   # True  — element-by-element comparison
print((1, 2, 3) <  (1, 2, 4))   # True  — compared lexicographically


# =============================================================================
# 7. TUPLE UNPACKING
# =============================================================================
# Assign each element of a tuple to individual variables in one line.

print("\n--- Basic Unpacking ---")
coordinates = (28.7041, 77.1025)
latitude, longitude = coordinates
print(f"Latitude: {latitude}, Longitude: {longitude}")

# Number of variables must exactly match number of elements
# a, b = (1, 2, 3)   # ❌ ValueError: too many values to unpack

# ── Extended unpacking with * (star) ──────────────────────────────────────────
first, *middle, last = (1, 2, 3, 4, 5)
print(f"first={first}, middle={middle}, last={last}")
# first=1, middle=[2, 3, 4], last=5

*start, second_last, last = (10, 20, 30, 40, 50)
print(f"start={start}, second_last={second_last}, last={last}")

# ── Swap variables — no temp variable needed ──────────────────────────────────
x, y = 10, 20
x, y = y, x          # Python creates a tuple (y, x) on the right, then unpacks
print(f"After swap: x={x}, y={y}")   # x=20, y=10

# ── Unpacking in loops ────────────────────────────────────────────────────────
students = [("Yash", 95), ("Prashant", 88), ("Rohit", 76)]
for name, score in students:
    print(f"{name}: {score}")


# =============================================================================
# 8. ITERATING OVER A TUPLE
# =============================================================================

fruits = ("apple", "banana", "cherry")

# Basic for loop
for fruit in fruits:
    print(fruit)

# With index using enumerate()
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Loop over two tuples together using zip()
scores = (95, 88, 76)
for name, score in zip(("Yash", "Prashant", "Rohit"), scores):
    print(f"{name}: {score}")

# While loop with tuple
t = (10, 20, 30)
i = 0
while i < len(t):
    print(t[i])
    i += 1


# =============================================================================
# 9. NESTED TUPLES
# =============================================================================
# A tuple that contains other tuples. Useful for fixed tables/records.

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matrix[0])       # (1, 2, 3)  — first row
print(matrix[1][2])    # 6          — row 1, column 2
print(matrix[-1][-1])  # 9          — last row, last column

# Iterate over nested tuple
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
# 1 2 3
# 4 5 6
# 7 8 9


# =============================================================================
# 10. TUPLES AS DICTIONARY KEYS
# =============================================================================
# Because tuples are immutable (hashable), they can be used as dict keys.
# Lists CANNOT be used as dict keys.

# GPS coordinate → location name
locations = {
    (28.7041, 77.1025): "Delhi",
    (19.0760, 72.8777): "Mumbai",
    (13.0827, 80.2707): "Chennai",
}
print(locations[(28.7041, 77.1025)])   # Delhi

# RGB color → color name
color_map = {
    (255, 0, 0)  : "Red",
    (0, 255, 0)  : "Green",
    (0, 0, 255)  : "Blue",
}
print(color_map[(0, 255, 0)])   # Green


# =============================================================================
# 11. TUPLE vs LIST — When to Use Which
# =============================================================================
#
#   Use a TUPLE when:
#     • Data must not change — coordinates, DB rows, RGB colors, config values
#     • You want faster performance (tuples are ~10–15% faster than lists)
#     • You need to use it as a dictionary key
#     • Returning multiple values from a function
#
#   Use a LIST when:
#     • Data needs to grow, shrink, or be modified
#     • You need sorting, appending, or removing items

# Tuples are commonly used to return multiple values from a function
def min_max(nums):
    return min(nums), max(nums)    # returns a tuple

low, high = min_max([3, 1, 9, 2, 7])
print(f"Min: {low}, Max: {high}")   # Min: 1, Max: 9


# =============================================================================
# QUICK REFERENCE TABLE
# =============================================================================
#
#  Method / Function     What it does
#  ──────────────────    ──────────────────────────────────────────────────────
#  tuple.count(x)        Number of times x appears (no error if missing)
#  tuple.index(x)        Index of first occurrence of x (ValueError if missing)
#  len(t)                Number of elements
#  min(t)                Smallest element
#  max(t)                Largest element
#  sum(t)                Sum of all numeric elements
#  sorted(t)             Return new sorted LIST (tuple unchanged)
#  tuple(reversed(t))    Reversed tuple
#  any(t)                True if at least one element is truthy
#  all(t)                True if ALL elements are truthy
#  x in t                True if x is in the tuple
#  x not in t            True if x is NOT in the tuple
#  t1 + t2               Concatenate — creates new tuple
#  t * n                 Repeat tuple n times
#  list(t)               Convert tuple to list (to allow mutation)
#  tuple(lst)            Convert list to tuple (to freeze it)


# =============================================================================
# PRACTICE QUESTIONS
# =============================================================================

# Q1. Create a tuple of 5 cities and print the first and last city.
# ------ Solution ------
cities = ("Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore")
print(cities[0])    # Delhi
print(cities[-1])   # Bangalore


# Q2. Count how many times the number 7 appears in the tuple below.
# ------ Solution ------
nums_q2 = (7, 3, 7, 8, 7, 2, 1, 7)
print(nums_q2.count(7))   # 4


# Q3. Find the index of "banana" in the tuple below.
# ------ Solution ------
fruits_q3 = ("mango", "apple", "banana", "grape")
print(fruits_q3.index("banana"))   # 2


# Q4. Convert the tuple (1, 2, 3, 4, 5) to a list, append 6, convert back.
# ------ Solution ------
t_q4     = (1, 2, 3, 4, 5)
lst_q4   = list(t_q4)
lst_q4.append(6)
t_q4     = tuple(lst_q4)
print(t_q4)   # (1, 2, 3, 4, 5, 6)


# Q5. Unpack the tuple (10, 20, 30) into three variables and print their sum.
# ------ Solution ------
a_q5, b_q5, c_q5 = (10, 20, 30)
print(a_q5 + b_q5 + c_q5)   # 60


# Q6. Slice the tuple (0,1,2,3,4,5,6,7,8,9) to get only even-indexed values.
# ------ Solution ------
t_q6 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t_q6[::2])   # (0, 2, 4, 6, 8)


# Q7. Write a function that takes a tuple of numbers and returns
#     a new tuple containing only the even numbers.
# ------ Solution ------
def filter_even(t):
    return tuple(x for x in t if x % 2 == 0)

print(filter_even((1, 2, 3, 4, 5, 6, 7, 8)))   # (2, 4, 6, 8)


# Q8. Merge two tuples and sort them in descending order.
# ------ Solution ------
t_a    = (5, 1, 8)
t_b    = (3, 9, 2)
merged = tuple(sorted(t_a + t_b, reverse=True))
print(merged)   # (9, 8, 5, 3, 2, 1)


# Q9. Given a list of student records as tuples, print only those with score >= 90.
# ------ Solution ------
students = [("Yash", 95), ("Prashant", 82), ("Rohit", 91), ("Aarav", 78)]
toppers  = [s for s in students if s[1] >= 90]
print(toppers)   # [('Yash', 95), ('Rohit', 91)]


# Q10. (Challenge) Use a tuple as a dictionary key to map (row, col) → value.
# ------ Solution ------
grid = {(0, 0): "X", (0, 1): "O", (1, 0): "O", (1, 1): "X"}
print(grid[(0, 1)])   # O
print(grid[(1, 1)])   # X