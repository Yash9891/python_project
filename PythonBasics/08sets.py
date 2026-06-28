# =============================================================================
#  PYTHON SETS — Complete Reference Guide
#  Author  : Yash
#  Purpose : Understand sets in Python from scratch
# =============================================================================


# -----------------------------------------------------------------------------
# WHAT IS A SET?
# -----------------------------------------------------------------------------
# A set is an UNORDERED collection of UNIQUE elements.
# Duplicate values are automatically removed.
# Sets are MUTABLE — you can add/remove elements after creation.
# But the ELEMENTS themselves must be immutable (no lists inside sets).
# Defined with curly braces { }
#
#  Property        Set
#  ─────────────   ────────────────────────────────────────────────
#  Ordered         No  — no guaranteed order, no indexing
#  Mutable         Yes — can add/remove elements
#  Duplicates      No  — automatically eliminated
#  Indexing        No  — cannot use set[0]
#  Syntax          {1, 2, 3}
#  Best for        Uniqueness checks, membership tests, math ops


# =============================================================================
# 1. CREATING SETS
# =============================================================================

# ── Using set() — the only way to create an EMPTY set ────────────────────────
s = set()
print(type(s))    # <class 'set'>

# ⚠️  Common mistake: {} creates a DICT, not a set!
d = {}
print(type(d))    # <class 'dict'>   ← NOT a set

# ── Using curly braces { } with values ───────────────────────────────────────
s = {23, 45, 67, 89, 23, 45}   # duplicates are silently removed
print(type(s))   # <class 'set'>
print(s)         # {67, 89, 23, 45}  — order may vary, no duplicates

nums = {1, 2, 3, 5, 5, 6, 6, 90, 1}
print(nums)      # {1, 2, 3, 5, 6, 90}

# ── Converting a list to a set — removes duplicates ───────────────────────────
my_list = [45, 56, 78, 89, 78, 89]
s       = set(my_list)
print(s)         # {45, 56, 78, 89}

# ── Other conversions ─────────────────────────────────────────────────────────
from_string = set("hello")          # {'h', 'e', 'l', 'o'}  — unique chars
from_range  = set(range(1, 6))      # {1, 2, 3, 4, 5}
from_tuple  = set((10, 20, 10, 30)) # {10, 20, 30}

print(from_string)
print(from_range)
print(from_tuple)


# =============================================================================
# 2. ADDING AND REMOVING ELEMENTS
# =============================================================================

s = {23, 45, 67, 89}

# ── add() — add ONE element ───────────────────────────────────────────────────
s.add(900)
print(s)      # {67, 900, 23, 45, 89}  — 900 added

s.add(45)     # duplicate — silently ignored
print(s)      # no change

# ── update() — add MULTIPLE elements from any iterable ───────────────────────
s.update([100, 200, 300])
print(s)      # 100, 200, 300 added

s.update({400, 500}, (600,))   # multiple iterables at once
print(s)

# ── discard() — remove if present, NO error if missing ────────────────────────
s = {23, 45, 67, 89}
s.discard(45)     # removes 45
print(s)          # {67, 89, 23}

s.discard(4775)   # 4775 not in set — silently ignored, no crash
print(s)          # unchanged

# ── remove() — remove element, RAISES KeyError if not found ──────────────────
s.remove(67)      # removes 67
print(s)          # {89, 23}

# s.remove(9999)  # ❌ KeyError: 9999  ← use discard() if unsure

# Safe remove with remove()
value = 9999
if value in s:
    s.remove(value)
else:
    print(f"{value} not found — nothing removed")

# ── pop() — remove and return an ARBITRARY element ────────────────────────────
s = {10, 20, 30, 40}
removed = s.pop()       # random element removed
print("Removed:", removed)
print("Remaining:", s)

# ── clear() — remove ALL elements ─────────────────────────────────────────────
s = {1, 2, 3}
s.clear()
print(s)   # set()


# =============================================================================
# 3. MEMBERSHIP — Checking if an Element Exists
# =============================================================================
# 'in' is very fast for sets — much faster than searching a list.

s = {23, 45, 67, 89}

find = 456 in s
print(find)   # False — 456 is not in the set

find = 45 in s
print(find)   # True  — 45 is in the set

print(89 not in s)    # False — 89 IS in the set

# Practical use
if 45 in s:
    print("45 found in set")
else:
    print("45 not found")


# =============================================================================
# 4. SET OPERATIONS — The Real Power of Sets
# =============================================================================

s1 = {1, 2, 3, 4, 5, 8, 9}
s2 = {4, 5, 6, 7, 8}

# ── union() / | — ALL elements from both sets ────────────────────────────────
print(s1.union(s2))        # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1 | s2)             # same result — shorthand

# ── intersection() / & — only elements present in BOTH sets ──────────────────
print(s1.intersection(s2)) # {4, 5, 8}
print(s1 & s2)             # same result

# ── difference() / - — elements in s1 but NOT in s2 ─────────────────────────
print(s1.difference(s2))   # {1, 2, 3, 9}  — in s1 only
print(s1 - s2)             # same result

print(s2 - s1)             # {6, 7}        — in s2 only

# ── symmetric_difference() / ^ — elements in EITHER but NOT BOTH ─────────────
print(s1 ^ s2)             # {1, 2, 3, 6, 7, 9}
print(s1.symmetric_difference(s2))   # same result

# ── Visual summary:
#    s1 = {1,2,3,4,5,8,9}    s2 = {4,5,6,7,8}
#    ┌──────────────────────────────────────────┐
#    │  s1 only        │  both   │  s2 only    │
#    │  {1,2,3,9}      │ {4,5,8} │  {6,7}      │
#    └──────────────────────────────────────────┘
#    union            = all three zones
#    intersection     = middle only
#    s1 - s2          = left only
#    s2 - s1          = right only
#    symmetric diff   = left + right (no middle)


# =============================================================================
# 5. SET COMPARISON METHODS
# =============================================================================

s1 = {1, 2, 3, 4, 5, 8, 9}
c1 = {1, 2, 8, 9}
c2 = {10, 11}

# ── issubset() — is c1 entirely inside s1? ───────────────────────────────────
print(c1.issubset(s1))    # True  — every element of c1 is in s1
print(c1 <= s1)           # True  — shorthand

# ── issuperset() — does s1 contain ALL of c1? ────────────────────────────────
print(s1.issuperset(c1))  # True  — s1 has all elements of c1
print(s1 >= c1)           # True  — shorthand

# ── isdisjoint() — do the sets share NO common elements? ─────────────────────
print(s1.isdisjoint(c2))  # True  — s1 and c2 have nothing in common
print(s1.isdisjoint(c1))  # False — they share 1, 2, 8, 9


# =============================================================================
# 6. IN-PLACE / UPDATE VERSIONS OF SET OPERATIONS
# =============================================================================
# These modify the set DIRECTLY instead of returning a new one.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.intersection_update(b)    # a = a & b  — keep only common elements
print(a)   # {3, 4}

a = {1, 2, 3, 4}
a.difference_update(b)      # a = a - b  — remove elements that are in b
print(a)   # {1, 2}

a = {1, 2, 3, 4}
a.symmetric_difference_update(b)   # a = a ^ b
print(a)   # {1, 2, 5, 6}


# =============================================================================
# 7. FROZENSET — Immutable Set
# =============================================================================
# frozenset is a set that CANNOT be changed after creation.
# Can be used as a dictionary key (regular sets cannot).

fs = frozenset({1, 2, 3, 4})
print(fs)          # frozenset({1, 2, 3, 4})

# fs.add(5)        # ❌ AttributeError — frozensets are immutable

# Use case — frozenset as a dictionary key
permissions = {
    frozenset({"admin", "editor"}): "Full Access",
    frozenset({"viewer"}):          "Read Only",
}
print(permissions[frozenset({"admin", "editor"})])   # Full Access


# =============================================================================
# 8. ITERATING OVER A SET
# =============================================================================

fruits = {"apple", "banana", "cherry"}

# Basic loop — order is NOT guaranteed
for fruit in fruits:
    print(fruit)

# Sort for consistent, predictable output
for fruit in sorted(fruits):
    print(fruit)

# Set comprehension — like list comprehension but returns a set
squares = {x**2 for x in range(1, 6)}
print(squares)   # {1, 4, 9, 16, 25}

evens = {x for x in range(1, 11) if x % 2 == 0}
print(evens)     # {2, 4, 6, 8, 10}


# =============================================================================
# 9. USEFUL BUILT-IN FUNCTIONS WITH SETS
# =============================================================================

s = {4, 1, 9, 2, 7}

print(len(s))      # 5   — number of elements
print(min(s))      # 1   — smallest
print(max(s))      # 9   — largest
print(sum(s))      # 23  — total
print(sorted(s))   # [1, 2, 4, 7, 9]  — returns a sorted LIST

print(9 in s)      # True  — fast membership test
print(99 in s)     # False


# =============================================================================
# 10. REAL-WORLD USE CASES
# =============================================================================

# ── Remove duplicates from a list ─────────────────────────────────────────────
names_with_dupes = ["Yash", "Prashant", "Yash", "Rohit", "Prashant"]
unique_names     = list(set(names_with_dupes))
print(sorted(unique_names))   # ['Prashant', 'Rohit', 'Yash']

# ── Find students common to two classes ───────────────────────────────────────
class_a = {"Yash", "Prashant", "Rohit"}
class_b = {"Rohit", "Aarav", "Meera"}
print(class_a & class_b)   # {'Rohit'}

# ── Students only in class A ──────────────────────────────────────────────────
print(class_a - class_b)   # {'Yash', 'Prashant'}

# ── Fast access control check ─────────────────────────────────────────────────
allowed_users = {"Yash", "Prashant", "Rohit"}
user = "Yash"
if user in allowed_users:
    print(f"{user} has access")   # Yash has access


# =============================================================================
# QUICK REFERENCE TABLE
# =============================================================================
#
#  Method / Operation              What it does
#  ─────────────────────────────   ────────────────────────────────────────────
#  set()                           Create an empty set (NOT {})
#  s.add(x)                        Add single element x
#  s.update(iter)                  Add all items from iterable
#  s.remove(x)                     Remove x — KeyError if not found
#  s.discard(x)                    Remove x — no error if not found
#  s.pop()                         Remove and return an arbitrary element
#  s.clear()                       Remove all elements
#  s.copy()                        Shallow copy
#  a | b  / a.union(b)             All elements from both sets
#  a & b  / a.intersection(b)      Elements in both sets
#  a - b  / a.difference(b)        Elements in a but not b
#  a ^ b  / a.symmetric_difference(b)  Elements in either, not both
#  a <= b / a.issubset(b)          True if all of a is in b
#  a >= b / a.issuperset(b)        True if a contains all of b
#  a.isdisjoint(b)                 True if a and b share no elements
#  len(s)                          Number of elements
#  x in s                          True if x is in the set
#  sorted(s)                       Return new sorted list from set
#  frozenset(s)                    Create immutable version of set


# =============================================================================
# PRACTICE QUESTIONS
# =============================================================================

# Q1. Create a set from the list [1,2,2,3,4,4,5] and print unique values.
# ------ Solution ------
lst_q1 = [1, 2, 2, 3, 4, 4, 5]
print(set(lst_q1))   # {1, 2, 3, 4, 5}


# Q2. Given s = {23,45,67,89}, add 900 and remove 45. Print the result.
# ------ Solution ------
s_q2 = {23, 45, 67, 89}
s_q2.add(900)
s_q2.discard(45)
print(s_q2)   # {67, 89, 23, 900}


# Q3. Check if 456 is present in {23, 45, 67, 89}.
# ------ Solution ------
print(456 in {23, 45, 67, 89})   # False


# Q4. Given s1={1,2,3,4,5,8,9} and s2={4,5,6,7,8}, find:
#     a) Union   b) Intersection   c) s1 - s2
# ------ Solution ------
s1_q4 = {1, 2, 3, 4, 5, 8, 9}
s2_q4 = {4, 5, 6, 7, 8}
print("Union       :", s1_q4 | s2_q4)          # {1,2,3,4,5,6,7,8,9}
print("Intersection:", s1_q4 & s2_q4)          # {4, 5, 8}
print("Difference  :", s1_q4 - s2_q4)          # {1, 2, 3, 9}


# Q5. Check if {1,2,8,9} is a subset of {1,2,3,4,5,8,9}.
# ------ Solution ------
print({1, 2, 8, 9}.issubset({1, 2, 3, 4, 5, 8, 9}))   # True


# Q6. Check if {1,2,3,4,5,8,9} is a superset of {1,2,8,9}.
# ------ Solution ------
print({1, 2, 3, 4, 5, 8, 9}.issuperset({1, 2, 8, 9}))   # True


# Q7. Use set comprehension to get unique squares of [1,1,2,2,3,3,4,4].
# ------ Solution ------
nums_q7 = [1, 1, 2, 2, 3, 3, 4, 4]
print({x**2 for x in nums_q7})   # {1, 4, 9, 16}


# Q8. (Challenge) Two students list their favourite languages.
#     Find: common, only Yash's, only Prashant's, and all combined.
# ------ Solution ------
yash_langs     = {"Python", "Java", "C++", "JavaScript"}
prashant_langs = {"Python", "JavaScript", "Go", "Rust"}

print("Common        :", yash_langs & prashant_langs)   # {'Python', 'JavaScript'}
print("Only Yash     :", yash_langs - prashant_langs)   # {'Java', 'C++'}
print("Only Prashant :", prashant_langs - yash_langs)   # {'Go', 'Rust'}
print("All combined  :", yash_langs | prashant_langs)   # all 6 languages