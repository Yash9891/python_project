# =============================================================================
#  PYTHON LOOPS — Complete Reference Guide
#  Author  : Yash
#  Purpose : Understand for loops and while loops in Python from scratch
#  Topics  : for loop, while loop, range(), break, continue, else,
#            nested loops, enumerate(), zip(), list comprehension
# =============================================================================


# =============================================================================
# SECTION 1 — WHAT IS A LOOP?
# =============================================================================
# A loop repeats a block of code multiple times, avoiding manual repetition.
#
# Python has 2 main loops:
#   1. for loop   → used when you know HOW MANY times to repeat
#                   (iterating over a list, string, range, etc.)
#   2. while loop → used when you repeat UNTIL a condition becomes False


# =============================================================================
# SECTION 2 — FOR LOOP: Iterating Over a List
# =============================================================================

fruits = ["apple", "mango", "banana"]

print("── Each fruit on a new line ──")
for fruit in fruits:
    print(fruit)
# Output:
# apple
# mango
# banana

print("── All fruits on one line (end parameter) ──")
for fruit in fruits:
    print(fruit, end=" ")   # end=" " replaces the default newline with a space
print()                     # move to next line after the loop


# =============================================================================
# SECTION 3 — FOR LOOP: Iterating Over a String
# =============================================================================
# A string is just a sequence of characters — you can loop over it directly.

name = "Prashant"

print("── Characters with comma separator ──")
for char in name:
    print(char, end=", ")
print()

# Practical use: count vowels in a name
vowels = "aeiouAEIOU"
vowel_count = 0

for char in name:
    if char in vowels:
        vowel_count += 1

print(f"Vowels in '{name}': {vowel_count}")   # Vowels in 'Prashant': 2


# =============================================================================
# SECTION 4 — range() FUNCTION
# =============================================================================
# range(stop)              → 0 to stop-1
# range(start, stop)       → start to stop-1
# range(start, stop, step) → start to stop-1, jumping by step
#
# range() is memory-efficient — it does NOT create the full list in memory.

print("── Squares from 1 to 5 ──")
for i in range(1, 6):
    print(f"{i}² = {i**2}", end="   ")
print()

print("── Even numbers 0–18 (step = 2) ──")
for i in range(0, 20, 2):       # start=0, stop=20, step=2
    print(i, end=" ")
print()

print("── Countdown from 10 (step = -1) ──")
for i in range(10, 0, -1):      # negative step goes backwards
    print(i, end=" ")
print()


# =============================================================================
# SECTION 5 — enumerate(): Loop With an Index
# =============================================================================
# enumerate() gives you both the index AND the value while looping.
# Much cleaner than manually tracking a counter variable.

languages = ["Python", "JavaScript", "Java", "C++"]

print("── Programming Languages (with rank) ──")
for index, language in enumerate(languages, start=1):
    print(f"  {index}. {language}")


# =============================================================================
# SECTION 6 — zip(): Loop Over Two Lists Together
# =============================================================================
# zip() pairs elements from two (or more) lists side by side.

students = ["Yash", "Priya", "Rahul"]
scores   = [88,     95,      73]

print("── Student Score Card ──")
for student, score in zip(students, scores):
    grade = "Pass" if score >= 50 else "Fail"
    print(f"  {student}: {score}/100 → {grade}")


# =============================================================================
# SECTION 7 — WHILE LOOP
# =============================================================================
# Repeats as long as the condition remains True.
# ⚠️  Always make sure the condition will eventually become False
#     to avoid an infinite loop.

print("── Count by 1 ──")
count = 1
while count <= 5:
    print(f"  count: {count}")
    count += 1      # increment — without this the loop never ends!

print("── Count by 2 (original code fixed) ──")
count = 1
while count < 6:
    print(f"  count: {count}", end=" ")
    count += 2      # jumps: 1 → 3 → 5 → stops (7 is not < 6)
print()


# =============================================================================
# SECTION 8 — break AND continue
# =============================================================================
# break    → EXIT the loop immediately, skip remaining iterations
# continue → SKIP the current iteration, jump to the next one

print("── break: stop at 'banana' ──")
for fruit in ["apple", "mango", "banana", "grape"]:
    if fruit == "banana":
        break               # loop ends here
    print(fruit, end=" ")
print()

print("── continue: skip 'mango' ──")
for fruit in ["apple", "mango", "banana", "grape"]:
    if fruit == "mango":
        continue            # skip this iteration only
    print(fruit, end=" ")
print()

print("── break in while: first multiple of 7 > 50 ──")
num = 51
while num < 200:
    if num % 7 == 0:
        print(f"  First multiple of 7 above 50: {num}")
        break
    num += 1


# =============================================================================
# SECTION 9 — LOOP ELSE CLAUSE
# =============================================================================
# Python loops have an optional else block that runs ONLY if the loop
# completed normally (i.e., was NOT stopped by a break).

print("── else block: search for a number ──")
target   = 99
numbers  = [10, 25, 33, 47, 88]

for num in numbers:
    if num == target:
        print(f"  Found {target}!")
        break
else:
    print(f"  {target} not found in the list.")   # ← runs (99 isn't there)


# =============================================================================
# SECTION 10 — NESTED LOOPS
# =============================================================================
# A loop inside another loop.
# Outer loop runs once → inner loop completes all iterations → repeat.

print("── Multiplication Table (3×3) ──")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row * col:3}", end="")  # :3 pads to width 3 for alignment
    print()

print("── Pattern: right-angled triangle ──")
for row in range(1, 6):
    print("* " * row)


# =============================================================================
# SECTION 11 — LIST COMPREHENSION (Compact Loop)
# =============================================================================
# A one-line way to build a new list using a loop.
#
# Syntax:  [expression  for  item  in  iterable  if  condition]

squares      = [x**2 for x in range(1, 6)]
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]

print(f"Squares 1–5       : {squares}")        # [1, 4, 9, 16, 25]
print(f"Even squares 1–10 : {even_squares}")   # [4, 16, 36, 64, 100]


# =============================================================================
# SECTION 12 — ORIGINAL CODE (CORRECTED & EXPLAINED)
# =============================================================================

# ── Original for loop ─────────────────────────────────────────────────────────
fruits = ["apple", "mango", "banana"]

for a in fruits:
    print(a)                # each fruit on its own line

for a in fruits:
    print(a, end=" ")       # all on one line — end replaces "\n" with " "
print()

# ── Original string loop ───────────────────────────────────────────────────────
name = "Prashant"
for chr in name:
    print(chr, end=",")     # P,r,a,s,h,a,n,t,
print()

# ── Original range examples ────────────────────────────────────────────────────
for i in range(1, 6):
    print(i**2, end=" ")    # 1 4 9 16 25
print()

for i in range(0, 20, 2):
    print(i, end=" ")       # 0 2 4 6 8 10 12 14 16 18
print()

# ── Original while loop ────────────────────────────────────────────────────────
count = 1
while count < 6:
    print(f" count : {count}")
    count += 2              # 1 → 3 → 5 → stops


# =============================================================================
# SECTION 13 — PRACTICE QUESTIONS
# =============================================================================
#
# ── Beginner ──────────────────────────────────────────────────────────────────
#
# Q1. Print numbers 1 to 20 using a for loop with range().
#
# Q2. Print the multiplication table of any number (e.g., 7).
#
# Q3. Use a while loop to keep asking the user to guess a secret number (42).
#     Stop when they guess correctly.
#
# Q4. Print all odd numbers between 1 and 30 using range() with a step.
#
# Q5. Given a list of numbers, print only the even ones.
#     numbers = [3, 8, 15, 22, 7, 14, 9, 40]
#
# ── Intermediate ──────────────────────────────────────────────────────────────
#
# Q6. Reverse a string using a for loop (without slicing).
#
# Q7. Count how many times the letter 'a' appears in a sentence using a loop.
#
# Q8. Use enumerate() to print a numbered shopping list.
#     items = ["bread", "milk", "eggs", "butter"]
#
# Q9. Use zip() to compare two lists and print which score improved.
#     last_week  = [55, 70, 88]
#     this_week  = [60, 65, 92]
#     names      = ["Yash", "Priya", "Rahul"]
#
# Q10. Print a full 10×10 multiplication table using nested loops.
#
# ── Advanced ──────────────────────────────────────────────────────────────────
#
# Q11. FizzBuzz: for numbers 1–50, print:
#      "Fizz" if divisible by 3
#      "Buzz" if divisible by 5
#      "FizzBuzz" if divisible by both
#      the number itself otherwise
#
# Q12. Find all prime numbers between 1 and 100 using nested loops and break.
#
# Q13. Flatten a 2D list into a 1D list using a nested loop.
#      matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# =============================================================================
# SECTION 14 — SOLUTIONS TO ALL PRACTICE QUESTIONS
# =============================================================================

print("\n" + "="*60)
print("SOLUTIONS")
print("="*60)

# ── Q1: Numbers 1 to 20 ───────────────────────────────────────────────────────
print("\nQ1 — Numbers 1 to 20:")
for i in range(1, 21):
    print(i, end=" ")
print()

# ── Q2: Multiplication table of 7 ────────────────────────────────────────────
print("\nQ2 — Multiplication table of 7:")
for i in range(1, 11):
    print(f"  7 × {i:2} = {7 * i}")

# ── Q3: Guess the number (simulated — no input() in a script) ─────────────────
print("\nQ3 — Guess the number (simulated):")
secret  = 42
guesses = [10, 55, 42]   # simulating user input

for guess in guesses:
    if guess == secret:
        print(f"  Correct! The number was {secret}.")
        break
    else:
        print(f"  {guess} is wrong. Try again.")

# ── Q4: Odd numbers 1–30 ──────────────────────────────────────────────────────
print("\nQ4 — Odd numbers 1–30:")
for i in range(1, 31, 2):
    print(i, end=" ")
print()

# ── Q5: Even numbers from list ────────────────────────────────────────────────
print("\nQ5 — Even numbers from list:")
numbers = [3, 8, 15, 22, 7, 14, 9, 40]
for n in numbers:
    if n % 2 == 0:
        print(n, end=" ")
print()

# ── Q6: Reverse a string ──────────────────────────────────────────────────────
print("\nQ6 — Reverse a string:")
word     = "Python"
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word   # prepend each character
print(f"  '{word}' reversed → '{reversed_word}'")

# ── Q7: Count letter 'a' ──────────────────────────────────────────────────────
print("\nQ7 — Count 'a' in sentence:")
sentence = "Yash practices Python at an amazing pace"
count = 0
for char in sentence:
    if char.lower() == 'a':
        count += 1
print(f"  Letter 'a' appears {count} times.")

# ── Q8: Numbered shopping list with enumerate() ───────────────────────────────
print("\nQ8 — Shopping list:")
items = ["bread", "milk", "eggs", "butter"]
for index, item in enumerate(items, start=1):
    print(f"  {index}. {item}")

# ── Q9: Score comparison with zip() ──────────────────────────────────────────
print("\nQ9 — Score comparison:")
names      = ["Yash", "Priya", "Rahul"]
last_week  = [55, 70, 88]
this_week  = [60, 65, 92]

for name, old, new in zip(names, last_week, this_week):
    diff = new - old
    trend = "↑ Improved" if diff > 0 else ("↓ Dropped" if diff < 0 else "→ Same")
    print(f"  {name}: {old} → {new}  ({trend} by {abs(diff)})")

# ── Q10: 10×10 multiplication table ──────────────────────────────────────────
print("\nQ10 — 10×10 Multiplication Table:")
print("     " + "  ".join(f"{i:3}" for i in range(1, 11)))
print("    " + "-" * 40)
for row in range(1, 11):
    row_values = "  ".join(f"{row * col:3}" for col in range(1, 11))
    print(f"  {row:2} |{row_values}")

# ── Q11: FizzBuzz ─────────────────────────────────────────────────────────────
print("\nQ11 — FizzBuzz (1–50):")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

# ── Q12: Prime numbers 1–100 ─────────────────────────────────────────────────
print("\nQ12 — Prime numbers between 1 and 100:")
primes = []
for num in range(2, 101):
    is_prime = True
    for divisor in range(2, int(num**0.5) + 1):  # only check up to √num
        if num % divisor == 0:
            is_prime = False
            break                                 # not prime, stop checking
    if is_prime:
        primes.append(num)
print(primes)

# ── Q13: Flatten a 2D list ────────────────────────────────────────────────────
print("\nQ13 — Flatten 2D list:")
matrix  = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat    = []
for row in matrix:
    for element in row:
        flat.append(element)
print(f"  Matrix : {matrix}")
print(f"  Flat   : {flat}")


# =============================================================================
# QUICK RECAP
# =============================================================================
# ✅  for loop          → iterate over list, string, range, etc.
# ✅  range()           → range(stop) / range(start,stop) / range(start,stop,step)
# ✅  while loop        → repeat until condition is False
# ✅  break             → exit the loop immediately
# ✅  continue          → skip current iteration
# ✅  else (on loop)    → runs only if loop was NOT broken
# ✅  enumerate()       → loop with index + value
# ✅  zip()             → loop over two lists in parallel
# ✅  nested loops      → loop inside a loop
# ✅  list comprehension→ compact one-line loop to build a list
# =============================================================================