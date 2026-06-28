# =============================================================================
#  PYTHON STRINGS — Complete Reference Guide
#  Author  : Yash
#  Purpose : Understand strings in Python from scratch
# =============================================================================


# -----------------------------------------------------------------------------
# WHAT IS A STRING?
# -----------------------------------------------------------------------------
# A string is an ordered, immutable sequence of Unicode characters.
# Defined using single quotes, double quotes, or triple quotes.
# Each character has an index starting from 0 (left) or -1 (right).
#
# Index layout for  "Python"
#
#   Character :  P   y   t   h   o   n
#   +ve index :  0   1   2   3   4   5
#   -ve index : -6  -5  -4  -3  -2  -1


# =============================================================================
# 1. CREATING STRINGS
# =============================================================================

single    = 'Hello'
double    = "Hello"
triple    = """This is a
multi-line string."""
raw       = r"C:\Users\Yash\Desktop"   # raw string — backslash treated literally
escaped   = "She said \"Hello!\""      # escape double quotes inside string

print(single)    # Hello
print(double)    # Hello
print(triple)
print(raw)       # C:\Users\Yash\Desktop
print(escaped)   # She said "Hello!"

# Common escape sequences
print("Line1\nLine2")    # \n — newline
print("Tab\there")       # \t — tab
print("Back\\slash")     # \\ — literal backslash


# =============================================================================
# 2. INDEXING — accessing one character
# =============================================================================

sentence = "Harry Potter is Good"

print(sentence[0])    # H  — first character
print(sentence[6])    # P
print(sentence[-1])   # d  — last character
print(sentence[-4])   # G

# Trying to access an out-of-range index causes IndexError
# print(sentence[100])   # ❌ IndexError


# =============================================================================
# 3. SLICING — accessing a range of characters
# =============================================================================
# Syntax: string[start : stop : step]
#   start — index to begin (inclusive, default 0)
#   stop  — index to end   (exclusive, default end of string)
#   step  — jump size      (default 1)

sentence = "Harry Potter is Good"

print(sentence[0:5])     # Harry   — index 0 to 4
print(sentence[6:12])    # Potter
print(sentence[:5])      # Harry   — start defaults to 0
print(sentence[16:])     # Good    — stop defaults to end
print(sentence[-4:])     # Good    — last 4 characters
print(sentence[-4:-1])   # Goo     — stop is exclusive
print(sentence[::2])     # Hry otrI od — every 2nd character
print(sentence[::-1])    # dooG si rettoP yrraH — reversed string


# =============================================================================
# 4. STRING PROPERTIES
# =============================================================================

sentence = "Harry Potter good Harry Harry is Good"

# ── len() — total number of characters (including spaces) ────────────────────
print(len(sentence))    # 37

# ── Immutability — strings CANNOT be changed in place ────────────────────────
name = "Yash"
# name[0] = "P"   # ❌ TypeError: 'str' object does not support item assignment

# Workaround: slice and concatenate to "modify"
name1 = name[1:]         # "ash"
new_name = "P" + name1   # "Pash"
print(new_name)          # Pash

# Another workaround: use replace()
name = "Yash"
name = name.replace("Y", "P")
print(name)   # Pash


# =============================================================================
# 5. STRING METHODS — Case
# =============================================================================

sentence = "harry potter good harry harry is good"

print(sentence.upper())        # HARRY POTTER GOOD HARRY HARRY IS GOOD
print(sentence.lower())        # harry potter good harry harry is good
print(sentence.capitalize())   # Harry potter good harry harry is good
print(sentence.title())        # Harry Potter Good Harry Harry Is Good
print(sentence.swapcase())     # HARRY POTTER GOOD HARRY HARRY IS GOOD → swaps each


# =============================================================================
# 6. STRING METHODS — Search and Check
# =============================================================================

sentence = "Harry Potter good Harry Harry is Good"

# ── count() — number of times a substring appears ─────────────────────────────
print(sentence.count("Harry"))    # 3
print(sentence.count("good"))     # 1  — case-sensitive
print(sentence.count("Good"))     # 1

# ── find() — index of FIRST occurrence (-1 if not found) ────────────────────
print(sentence.find("Potter"))    # 6
print(sentence.find("Good"))      # 33
print(sentence.find("Java"))      # -1  — not found

# ── index() — same as find() but raises ValueError if not found ──────────────
print(sentence.index("Harry"))    # 0
# print(sentence.index("Java"))   # ❌ ValueError

# ── rfind() / rindex() — search from the RIGHT side ──────────────────────────
print(sentence.rfind("Harry"))    # 21  — last occurrence
print(sentence.rindex("Harry"))   # 21

# ── startswith() / endswith() ────────────────────────────────────────────────
print(sentence.startswith("Harry"))    # True
print(sentence.startswith("Potter"))   # False
print(sentence.endswith("Good"))       # True
print(sentence.endswith("is good"))    # False  — case-sensitive

# Can also check a tuple of options
print(sentence.endswith(("Good", "great", "nice")))   # True

# ── in / not in — membership check ───────────────────────────────────────────
print("Harry"  in sentence)      # True
print("Hermione" in sentence)    # False
print("Hermione" not in sentence) # True


# =============================================================================
# 7. STRING METHODS — Validation
# =============================================================================

print("Python3".isalnum())    # True  — only letters and digits
print("Python!".isalnum())    # False — '!' is not alphanumeric
print("Python".isalpha())     # True  — only letters
print("123".isdigit())        # True  — only digits
print("  ".isspace())         # True  — only whitespace
print("hello world".islower()) # True
print("HELLO".isupper())       # True
print("Hello World".istitle()) # True  — each word starts with uppercase


# =============================================================================
# 8. STRING METHODS — Replace and Remove
# =============================================================================

sentence = "Harry Potter good Harry Harry is Good"

# ── replace() — replaces ALL occurrences by default ──────────────────────────
string2 = "Yash"
replaced_string = sentence.replace("Harry", string2)
print(replaced_string)   # Yash Potter good Yash Yash is Good

# Replace only the first N occurrences
print(sentence.replace("Harry", "Yash", 2))   # Yash Potter good Yash Harry is Good

# ── strip() — removes whitespace (or characters) from BOTH ends ───────────────
messy = "   Hello, World!   "
print(messy.strip())     # "Hello, World!"
print(messy.lstrip())    # "Hello, World!   "
print(messy.rstrip())    # "   Hello, World!"

# Remove specific characters
print("***Hello***".strip("*"))    # Hello
print("xxYashxx".strip("x"))       # Yash

# ── removeprefix() / removesuffix()  (Python 3.9+) ───────────────────────────
print("Mr. Yash".removeprefix("Mr. "))    # Yash
print("Yash.py".removesuffix(".py"))      # Yash


# =============================================================================
# 9. STRING METHODS — Split and Join
# =============================================================================

sentence = "Harry Potter good Harry Harry is Good"

# ── split() — splits string into a LIST ──────────────────────────────────────
words = sentence.split()          # split on whitespace by default
print(words)
# ['Harry', 'Potter', 'good', 'Harry', 'Harry', 'is', 'Good']

csv_data = "Yash,20,Delhi,Python"
parts    = csv_data.split(",")
print(parts)   # ['Yash', '20', 'Delhi', 'Python']

# Split with a limit
print(sentence.split(" ", 2))    # ['Harry', 'Potter', 'good Harry Harry is Good']

# ── rsplit() — split from the RIGHT ──────────────────────────────────────────
print("a,b,c,d".rsplit(",", 2))   # ['a,b', 'c', 'd']

# ── splitlines() — split on newline characters ────────────────────────────────
text = "Line1\nLine2\nLine3"
print(text.splitlines())    # ['Line1', 'Line2', 'Line3']

# ── join() — joins a list of strings into one string ─────────────────────────
words = ["Harry", "Potter", "is", "Good"]
print(" ".join(words))     # Harry Potter is Good
print("-".join(words))     # Harry-Potter-is-Good
print("".join(words))      # HarryPotterisGood

# Practical: clean and rejoin
raw      = "  Harry   Potter  "
cleaned  = " ".join(raw.split())    # removes extra spaces
print(cleaned)    # Harry Potter


# =============================================================================
# 10. STRING METHODS — Align and Pad
# =============================================================================

name = "Yash"

print(name.center(10))          # "   Yash   "
print(name.center(10, "-"))     # "---Yash---"
print(name.ljust(10))           # "Yash      "
print(name.ljust(10, "."))      # "Yash......"
print(name.rjust(10))           # "      Yash"
print(name.zfill(8))            # "0000Yash"  — pad with zeros (used for numbers)

# Practical: formatted table
students = [("Yash", 95), ("Prashant", 88), ("Aarav", 76)]
print(f"{'Name':<12} {'Score':>6}")
print("-" * 20)
for n, s in students:
    print(f"{n:<12} {s:>6}")


# =============================================================================
# 11. STRING FORMATTING
# =============================================================================

name  = "Yash"
score = 95.678
pi    = 3.14159

# ── f-string (recommended — Python 3.6+) ─────────────────────────────────────
print(f"Name: {name}, Score: {score}")
print(f"Score rounded: {score:.2f}")       # 2 decimal places
print(f"Pi: {pi:.4f}")                     # 4 decimal places
print(f"Score as int: {int(score)}")
print(f"{'Padded':^20}")                   # centered in 20 chars
print(f"{1000000:,}")                      # 1,000,000 — comma separator

# ── .format() ────────────────────────────────────────────────────────────────
print("Name: {}, Score: {}".format(name, score))
print("Name: {0}, Score: {1}, Name again: {0}".format(name, score))
print("Name: {n}, Score: {s}".format(n=name, s=score))

# ── % formatting (old style) ──────────────────────────────────────────────────
print("Name: %s, Score: %.2f" % (name, score))


# =============================================================================
# 12. STRING OPERATIONS
# =============================================================================

# ── Concatenation ( + ) ───────────────────────────────────────────────────────
first = "Harry"
last  = "Potter"
full  = first + " " + last
print(full)    # Harry Potter

# ── Repetition ( * ) ──────────────────────────────────────────────────────────
print("Ha" * 3)        # HaHaHa
print("-" * 30)        # ------------------------------ (separator line)

# ── Iteration ─────────────────────────────────────────────────────────────────
for char in "Yash":
    print(char, end=" ")    # Y a s h
print()

# ── Comparison ────────────────────────────────────────────────────────────────
print("apple" == "apple")    # True
print("apple" <  "banana")   # True  — alphabetical
print("Yash"  == "yash")     # False — case-sensitive


# =============================================================================
# QUICK REFERENCE TABLE
# =============================================================================
#
#  Method                   What it does
#  ───────────────────────  ──────────────────────────────────────────────────
#  s.upper()                All uppercase
#  s.lower()                All lowercase
#  s.capitalize()           First letter uppercase, rest lowercase
#  s.title()                First letter of each word uppercase
#  s.swapcase()             Swap upper↔lower for each character
#  s.strip(chars)           Remove leading/trailing whitespace or chars
#  s.lstrip(chars)          Remove from left only
#  s.rstrip(chars)          Remove from right only
#  s.replace(old, new, n)   Replace old with new (n times, default all)
#  s.split(sep, n)          Split into list (n times, default all)
#  s.rsplit(sep, n)         Split from right
#  s.splitlines()           Split on newline characters
#  sep.join(list)           Join list items into one string
#  s.find(sub)              Index of first match (-1 if not found)
#  s.rfind(sub)             Index of last match (-1 if not found)
#  s.index(sub)             Index of first match (ValueError if not found)
#  s.count(sub)             Number of non-overlapping occurrences
#  s.startswith(prefix)     True if string starts with prefix
#  s.endswith(suffix)       True if string ends with suffix
#  s.isalpha()              True if all characters are letters
#  s.isdigit()              True if all characters are digits
#  s.isalnum()              True if all characters are letters or digits
#  s.isspace()              True if all characters are whitespace
#  s.isupper()              True if all cased characters are uppercase
#  s.islower()              True if all cased characters are lowercase
#  s.istitle()              True if string is titlecased
#  s.center(w, char)        Center in width w, padded with char
#  s.ljust(w, char)         Left-justify in width w
#  s.rjust(w, char)         Right-justify in width w
#  s.zfill(w)               Pad with leading zeros to width w
#  s.encode(encoding)       Encode string to bytes


# =============================================================================
# PRACTICE QUESTIONS
# =============================================================================

sentence = "Harry Potter good Harry Harry is Good"

# Q1. Print the first 5 and last 4 characters of the sentence.
# ------ Solution ------
print(sentence[:5])     # Harry
print(sentence[-4:])    # Good


# Q2. Count how many times "Harry" appears. Then count "good" (case-insensitive).
# ------ Solution ------
print(sentence.count("Harry"))            # 3
print(sentence.lower().count("good"))     # 2  — finds both "good" and "Good"


# Q3. Replace all occurrences of "Harry" with your name and print.
# ------ Solution ------
print(sentence.replace("Harry", "Yash"))


# Q4. Reverse the sentence using slicing.
# ------ Solution ------
print(sentence[::-1])


# Q5. Check if the sentence starts with "Harry" and ends with "Good".
# ------ Solution ------
print(sentence.startswith("Harry"))   # True
print(sentence.endswith("Good"))      # True


# Q6. Split the sentence into a list of words. Print the 3rd word.
# ------ Solution ------
words = sentence.split()
print(words[2])   # good


# Q7. Given name = "  yash sharma  ", clean it and convert to title case.
# ------ Solution ------
name = "  yash sharma  "
print(name.strip().title())   # Yash Sharma


# Q8. Given csv = "Yash,20,Delhi,Python", extract each value separately.
# ------ Solution ------
csv = "Yash,20,Delhi,Python"
name, age, city, lang = csv.split(",")
print(f"Name: {name}, Age: {age}, City: {city}, Language: {lang}")


# Q9. Check if "Potter" is in the sentence and print its starting index.
# ------ Solution ------
word = "Potter"
if word in sentence:
    print(f"'{word}' found at index {sentence.find(word)}")


# Q10. Print a formatted table:
#      Name         Language     Score
#      Yash         Python         95
#      Prashant     JavaScript     88
# ------ Solution ------
data = [("Yash", "Python", 95), ("Prashant", "JavaScript", 88)]
print(f"{'Name':<12} {'Language':<14} {'Score':>5}")
print("-" * 35)
for n, lang, sc in data:
    print(f"{n:<12} {lang:<14} {sc:>5}")


