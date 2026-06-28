# =============================================================================
#  PYTHON DATA STRUCTURES & LISTS — Complete Reference Guide
#  Author  : Yash
#  Purpose : Understand data structures and lists in Python from scratch
# =============================================================================


# -----------------------------------------------------------------------------
# WHAT IS A DATA STRUCTURE?
# -----------------------------------------------------------------------------
# A data structure is a way of organising and storing data in memory so that
# it can be accessed and modified efficiently.
#
# Python has 4 built-in data structures:
#
#  Structure   Syntax          Ordered   Mutable   Duplicates   Key feature
#  ─────────   ─────────────   ───────   ───────   ──────────   ─────────────────────
#  List        [1, 2, 3]       Yes       Yes       Yes          General-purpose sequence
#  Tuple       (1, 2, 3)       Yes       No        Yes          Fixed / read-only data
#  Set         {1, 2, 3}       No        Yes       No           Unique items, fast lookup
#  Dictionary  {"a": 1}        Yes*      Yes       Keys: No     Key-value pairs
#
#  * Dict preserves insertion order since Python 3.7
#
# There are also data structures in the 'collections' module:
#   deque, Counter, OrderedDict, defaultdict, namedtuple — covered at the end.


# =============================================================================
# LIST — Deep Dive
# =============================================================================
# A list is an ordered, mutable sequence that can hold items of any type.
# Items can be added, removed, or changed after creation.
# Lists allow duplicate values.
# Defined with square brackets [ ]


# =============================================================================
# 1. CREATING LISTS
# =============================================================================

empty_list  = []                          # empty list
l1          = [10, 2, 30, 4, 5]          # integers
names       = ["Yash", "Prashant", "Rohit is good", "Prashant"]  # strings
mixed       = [1, "hello", 3.14, True, None]   # mixed types
nested      = [[1, 2], [3, 4], [5, 6]]   # list of lists

print(l1)       # [10, 2, 30, 4, 5]
print(names)    # ['Yash', 'Prashant', 'Rohit is good', 'Prashant']
print(mixed)    # [1, 'hello', 3.14, True, None]

# Create a list using list()
from_range  = list(range(1, 6))     # [1, 2, 3, 4, 5]
from_string = list("Yash")          # ['Y', 'a', 's', 'h']
print(from_range)
print(from_string)

# List comprehension — concise way to create lists
squares  = [x ** 2 for x in range(1, 6)]   # [1, 4, 9, 16, 25]
evens    = [x for x in range(1, 11) if x % 2 == 0]   # [2, 4, 6, 8, 10]
print(squares)
print(evens)


# =============================================================================
# 2. INDEXING AND SLICING
# =============================================================================
# Lists use the same index rules as strings.
# Positive index starts at 0 (left), negative index starts at -1 (right).

names = ["Yash", "Prashant", "Rohit", "Aarav", "Meera"]
#         0         1          2        3         4
#        -5        -4         -3       -2        -1

print(names[0])      # Yash     — first item
print(names[2])      # Rohit
print(names[-1])     # Meera    — last item
print(names[-2])     # Aarav

# Slicing   [start : stop : step]  — stop is EXCLUSIVE
print(names[1:3])    # ['Prashant', 'Rohit']
print(names[:3])     # ['Yash', 'Prashant', 'Rohit']
print(names[2:])     # ['Rohit', 'Aarav', 'Meera']
print(names[::2])    # ['Yash', 'Rohit', 'Meera']  — every 2nd item
print(names[::-1])   # ['Meera', 'Aarav', 'Rohit', 'Prashant', 'Yash']  — reversed


# =============================================================================
# 3. MUTABILITY — changing items in place
# =============================================================================
# Lists ARE mutable — you can change any element directly using its index.
# (Unlike strings, which are immutable.)

l1 = [10, 2, 30, 4, 5]
print(l1)         # [10, 2, 30, 4, 5]

l1[0] = 100       # change first element
print(l1)         # [100, 2, 30, 4, 5]

l1[-1] = 999      # change last element
print(l1)         # [100, 2, 30, 4, 999]

# Change a slice of elements
l1[1:3] = [20, 300]
print(l1)         # [100, 20, 300, 4, 999]


# =============================================================================
# 4. ADDING ELEMENTS
# =============================================================================

l1    = [10, 2, 30, 4, 5]
names = ["Yash", "Prashant", "Rohit"]

# ── append() — add ONE item to the END ───────────────────────────────────────
l1.append(100)
print(l1)      # [10, 2, 30, 4, 5, 100]

names.append("Aarav")
print(names)   # ['Yash', 'Prashant', 'Rohit', 'Aarav']

# ── insert() — add ONE item at a SPECIFIC INDEX ───────────────────────────────
l1.insert(0, 2000)     # insert 2000 at index 0 (pushes rest right)
print(l1)              # [2000, 10, 2, 30, 4, 5, 100]

l1.insert(3, 999)      # insert 999 at index 3
print(l1)              # [2000, 10, 2, 999, 30, 4, 5, 100]

# ── extend() — add MULTIPLE items to the END ──────────────────────────────────
l1 = [1, 2, 3]
l1.extend([4, 5, 6])
print(l1)    # [1, 2, 3, 4, 5, 6]

# extend vs append
a = [1, 2, 3]
b = [1, 2, 3]
a.append([4, 5])    # adds the list AS ONE item → [1, 2, 3, [4, 5]]
b.extend([4, 5])    # adds items individually  → [1, 2, 3, 4, 5]
print(a)
print(b)

# ── + operator — creates a NEW list ──────────────────────────────────────────
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)   # [1, 2, 3, 4, 5, 6]
# list1 and list2 are unchanged


# =============================================================================
# 5. REMOVING ELEMENTS
# =============================================================================

l1    = [10, 2, 30, 4, 5]
names = ["Yash", "Prashant", "Rohit", "Prashant"]

# ── remove() — removes FIRST occurrence of a VALUE ────────────────────────────
l1.remove(30)
print(l1)      # [10, 2, 4, 5]

names.remove("Prashant")    # removes only the FIRST "Prashant"
print(names)                # ['Yash', 'Rohit', 'Prashant']

# ⚠️  remove() raises ValueError if the value is not in the list
# l1.remove(999)   # ❌ ValueError: list.remove(x): x not in list

# Safe remove
if 999 in l1:
    l1.remove(999)
else:
    print("Value not found")

# ── pop() — removes item at a GIVEN INDEX and RETURNS it ──────────────────────
l1 = [10, 2, 30, 4, 5]

removed = l1.pop(2)     # remove item at index 2
print(removed)          # 30
print(l1)               # [10, 2, 4, 5]

last = l1.pop()         # no index = removes and returns LAST item
print(last)             # 5
print(l1)               # [10, 2, 4]

# ── del — delete by index or slice ────────────────────────────────────────────
l1 = [10, 2, 30, 4, 5]
del l1[0]         # delete first item
print(l1)         # [2, 30, 4, 5]

del l1[1:3]       # delete a slice
print(l1)         # [2, 5]

# del can also delete the entire variable
# del l1
# print(l1)   # ❌ NameError — l1 no longer exists

# ── clear() — remove ALL items, keep the list object ─────────────────────────
l1 = [10, 2, 30, 4, 5]
l1.clear()
print(l1)    # []


# =============================================================================
# 6. SORTING AND ORDERING
# =============================================================================

l1    = [10, 2, 30, 4, 5]
names = ["Prashant", "Yash", "Rohit", "Aarav"]

# ── sort() — sorts the list IN PLACE (modifies original) ─────────────────────
l1.sort()
print(l1)        # [2, 4, 5, 10, 30]

l1.sort(reverse=True)
print(l1)        # [30, 10, 5, 4, 2]

names.sort()
print(names)     # ['Aarav', 'Prashant', 'Rohit', 'Yash']

names.sort(key=len)   # sort by string length
print(names)          # ['Yash', 'Rohit', 'Aarav', 'Prashant']

# ── sorted() — returns a NEW sorted list (original unchanged) ─────────────────
l1       = [10, 2, 30, 4, 5]
new_list = sorted(l1)
print(l1)        # [10, 2, 30, 4, 5]  — original unchanged
print(new_list)  # [2, 4, 5, 10, 30]

# ── reverse() — reverse the list IN PLACE ────────────────────────────────────
l1 = [10, 2, 30, 4, 5]
l1.reverse()
print(l1)        # [5, 4, 30, 2, 10]

names = ["Prashant", "Yash", "Rohit", "Aarav"]
names.reverse()
print(names)     # ['Aarav', 'Rohit', 'Yash', 'Prashant']


# =============================================================================
# 7. SEARCHING AND COUNTING
# =============================================================================

names = ["Yash", "Prashant", "Rohit", "Prashant", "Aarav"]

# ── index() — returns INDEX of first occurrence ───────────────────────────────
print(names.index("Prashant"))    # 1  — first occurrence
# print(names.index("Meera"))     # ❌ ValueError if not found

# Safe index search
if "Meera" in names:
    print(names.index("Meera"))
else:
    print("Not found")

# ── count() — number of times a value appears ─────────────────────────────────
print(names.count("Prashant"))    # 2
print(names.count("Yash"))        # 1
print(names.count("Meera"))       # 0  — no error, just 0

# ── in / not in — membership check ───────────────────────────────────────────
print("Yash"  in names)      # True
print("Meera" in names)      # False
print("Meera" not in names)  # True


# =============================================================================
# 8. USEFUL LIST FUNCTIONS
# =============================================================================

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print(len(numbers))     # 10   — number of items
print(min(numbers))     # 1    — smallest value
print(max(numbers))     # 9    — largest value
print(sum(numbers))     # 39   — total of all values

# ── copy() — shallow copy of the list ────────────────────────────────────────
original = [1, 2, 3]
copy1    = original.copy()     # ✅ independent copy
copy2    = original            # ⚠️  this is NOT a copy — same object!

copy1.append(99)
copy2.append(88)

print(original)   # [1, 2, 3, 88]  — copy2 changed original too!
print(copy1)      # [1, 2, 3, 99]  — copy1 is independent

# ── * operator — repeat a list ────────────────────────────────────────────────
print([0] * 5)           # [0, 0, 0, 0, 0]
print(["hi"] * 3)        # ['hi', 'hi', 'hi']


# =============================================================================
# 9. ITERATING OVER A LIST
# =============================================================================

fruits = ["apple", "banana", "cherry"]

# Basic loop
for fruit in fruits:
    print(fruit)

# Loop with index using enumerate
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# Loop over two lists together using zip
scores = [95, 88, 76]
for name, score in zip(["Yash", "Prashant", "Aarav"], scores):
    print(f"{name}: {score}")

# While loop with list
items = [10, 20, 30]
i = 0
while i < len(items):
    print(items[i])
    i += 1


# =============================================================================
# 10. NESTED LISTS
# =============================================================================
# A list that contains other lists. Used to represent matrices or tables.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])       # [1, 2, 3]   — first row
print(matrix[1][2])    # 6           — row 1, column 2
print(matrix[-1][-1])  # 9           — last row, last column

# Iterate over a matrix
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
# 1 2 3
# 4 5 6
# 7 8 9


# =============================================================================
# 11. LIST COMPREHENSION (advanced creation)
# =============================================================================
# Shorter and faster alternative to for loops for creating lists.
# Syntax:  [expression  for  item  in  iterable  if  condition]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares      = [x**2 for x in numbers]
evens        = [x    for x in numbers if x % 2 == 0]
even_squares = [x**2 for x in numbers if x % 2 == 0]
upper_names  = [n.upper() for n in ["yash", "prashant", "rohit"]]

print(squares)        # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(evens)          # [2, 4, 6, 8, 10]
print(even_squares)   # [4, 16, 36, 64, 100]
print(upper_names)    # ['YASH', 'PRASHANT', 'ROHIT']


# =============================================================================
# 12. collections MODULE — Extended Data Structures
# =============================================================================
from collections import Counter, deque, defaultdict, namedtuple, OrderedDict

# ── Counter — count occurrences of each item ──────────────────────────────────
names_list = ["Yash", "Prashant", "Yash", "Rohit", "Yash", "Prashant"]
count      = Counter(names_list)
print(count)                    # Counter({'Yash': 3, 'Prashant': 2, 'Rohit': 1})
print(count["Yash"])            # 3
print(count.most_common(2))     # [('Yash', 3), ('Prashant', 2)]

# ── deque — double-ended queue (fast append/pop from both ends) ───────────────
dq = deque([1, 2, 3])
dq.appendleft(0)    # add to left
dq.append(4)        # add to right
print(dq)           # deque([0, 1, 2, 3, 4])
dq.popleft()        # remove from left
dq.pop()            # remove from right
print(dq)           # deque([1, 2, 3])

# ── defaultdict — dict with a default value for missing keys ──────────────────
dd = defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")
dd["veggies"].append("carrot")
print(dict(dd))   # {'fruits': ['apple', 'banana'], 'veggies': ['carrot']}

# ── namedtuple — tuple with named fields ──────────────────────────────────────
Student = namedtuple("Student", ["name", "age", "grade"])
s1 = Student("Yash", 20, "A")
print(s1.name)    # Yash
print(s1.age)     # 20
print(s1.grade)   # A


# =============================================================================
# QUICK REFERENCE TABLE
# =============================================================================
#
#  Method / Function     What it does
#  ──────────────────    ──────────────────────────────────────────────────────
#  list.append(x)        Add x to the end
#  list.insert(i, x)     Insert x at index i
#  list.extend(iter)     Add all items from iterable to the end
#  list.remove(x)        Remove first occurrence of x (ValueError if missing)
#  list.pop(i)           Remove and return item at index i (default: last)
#  list.clear()          Remove all items
#  list.sort()           Sort in place (ascending by default)
#  list.reverse()        Reverse in place
#  list.index(x)         Index of first occurrence of x
#  list.count(x)         Number of times x appears
#  list.copy()           Return a shallow copy
#  len(list)             Number of items
#  min(list)             Smallest item
#  max(list)             Largest item
#  sum(list)             Sum of all numeric items
#  sorted(list)          Return new sorted list (original unchanged)
#  reversed(list)        Return reverse iterator (original unchanged)
#  enumerate(list)       Return (index, value) pairs
#  zip(list1, list2)     Pair up items from two lists
#  x in list             True if x is in the list
#  x not in list         True if x is NOT in the list
#  del list[i]           Delete item at index i
#  del list[i:j]         Delete slice from i to j


# =============================================================================
# PRACTICE QUESTIONS
# =============================================================================

# Q1. Create a list of 5 numbers. Print the first, last, and middle item.
# ------ Solution ------
nums = [10, 20, 30, 40, 50]
print(nums[0])           # 10
print(nums[-1])          # 50
print(nums[len(nums)//2])  # 30


# Q2. Given l1 = [10, 2, 30, 4, 5], sort it ascending then descending.
# ------ Solution ------
l1 = [10, 2, 30, 4, 5]
l1.sort()
print(l1)                # [2, 4, 5, 10, 30]
l1.sort(reverse=True)
print(l1)                # [30, 10, 5, 4, 2]


# Q3. Add "Aarav" at index 1 and "Meera" at the end of names list.
# ------ Solution ------
names = ["Yash", "Prashant", "Rohit"]
names.insert(1, "Aarav")
names.append("Meera")
print(names)   # ['Yash', 'Aarav', 'Prashant', 'Rohit', 'Meera']


# Q4. Remove the second occurrence of "Prashant" from the list.
# ------ Solution ------
names = ["Yash", "Prashant", "Rohit", "Prashant"]
names.remove("Prashant")   # removes first
names.remove("Prashant")   # removes second
print(names)               # ['Yash', 'Rohit']


# Q5. Use list comprehension to create a list of cubes of odd numbers from 1–10.
# ------ Solution ------
cubes = [x**3 for x in range(1, 11) if x % 2 != 0]
print(cubes)   # [1, 27, 125, 343, 729]


# Q6. Flatten a nested list [[1,2],[3,4],[5,6]] into [1,2,3,4,5,6].
# ------ Solution ------
nested  = [[1, 2], [3, 4], [5, 6]]
flat    = [item for sublist in nested for item in sublist]
print(flat)   # [1, 2, 3, 4, 5, 6]


# Q7. Count occurrences of each name using Counter.
# ------ Solution ------
from collections import Counter
roster = ["Yash", "Prashant", "Yash", "Rohit", "Prashant", "Yash"]
print(Counter(roster))   # Counter({'Yash': 3, 'Prashant': 2, 'Rohit': 1})


# Q8. Given two lists [1,2,3] and [4,5,6], combine without using +.
#     Then find sum, min, max, and length of the combined list.
# ------ Solution ------
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
print(f"Sum: {sum(a)}, Min: {min(a)}, Max: {max(a)}, Len: {len(a)}")

