# =============================================================================
#  PYTHON CSV FILE HANDLING — Complete Beginner-to-Advanced Guide
#  Purpose : Learn how to read, filter, sort, write, and append CSV files
#
#  HOW TO USE THIS FILE:
#  ----------------------
#  This script is fully self-contained. You don't need to create any files
#  or folders yourself — when you run it, it first creates a small sample
#  "students.csv" file for you, then walks through every CSV operation on
#  it, from the simplest possible read all the way to filtering, sorting,
#  writing, and appending — with clear comments explaining WHY each thing
#  is done, not just what the code does.
#
#  Just run:  python csv_handling.py
#  ...and read the printed output alongside the comments below.
# =============================================================================

# ── WHAT IS A CSV FILE? ─────────────────────────────────────────────────────
# CSV stands for "Comma Separated Values". It's basically a plain-text
# spreadsheet: each LINE in the file is one ROW of data, and the values in
# that row are separated by commas.
#
#   Example of one row:   101,Yash,89,A
#
# Opening a .csv file in Excel or Google Sheets shows it as neat columns,
# but underneath, it is really just plain text with commas as separators.
#
# WHY USE Python's built-in "csv" MODULE instead of just doing
# line.split(",") ourselves?
#   Splitting manually seems simple, but it breaks in common edge cases —
#   for example, if a value itself contains a comma, like a name written
#   as "Sharma, Rohit". The csv module already knows how to handle these
#   tricky cases correctly (quoted values, different delimiters, etc.), so
#   we always prefer it over manual string splitting.
#
# THE 4 MAIN TOOLS IN THE csv MODULE:
#   csv.reader(file)                    -> reads each row as a plain LIST
#   csv.DictReader(file)                -> reads each row as a DICTIONARY,
#                                          using the header row as the keys
#   csv.writer(file)                    -> writes rows FROM lists
#   csv.DictWriter(file, fieldnames=[]) -> writes rows FROM dictionaries
#
# IMPORTANT: whenever we open a CSV file (for reading OR writing), we pass
# newline="" to open(). This is a small technical requirement of the csv
# module — without it, Windows computers can sometimes add extra blank
# rows into the file by mistake.

import csv
import os

# BASE = the folder where this script itself is saved. We build every other
# path relative to it, so the script works no matter where you put the
# project folder on your computer.
BASE = os.path.dirname(os.path.abspath(__file__))

# Paths to our input file (the CSV we will read) and our output file (the
# CSV we will write to). Using os.path.join() instead of typing "/" or "\"
# by hand makes the paths work correctly on Windows, Mac, and Linux alike.
csv_path    = os.path.join(BASE, "PythonBasics", "files",  "students.csv")
output_path = os.path.join(BASE, "PythonBasics", "output", "csv", "student.csv")

def section(title):
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}")


# =============================================================================
# PART 0 — ONE-TIME SETUP: create the folders and the sample CSV file
# =============================================================================
# This part just prepares a students.csv file to practice on, so the rest
# of the script actually has real data to work with. Feel free to skim
# this and jump to PART 1 — the real CSV learning starts there.

def setup_sample_csv():
    section("0. SETUP — creating the sample students.csv file (if missing)")

    # Make sure both the "files" (input) and "output/csv" (output) folders
    # exist. exist_ok=True means "don't complain if the folder is already
    # there".
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Only create the sample file if it doesn't already exist, so running
    # this script again later won't wipe out any changes you've made.
    if not os.path.exists(csv_path):
        with open(csv_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "age", "marks", "grade"])   # header row
            writer.writerow(["Yash",   20, 89.456, "A"])
            writer.writerow(["Rohit",  21, 55.2,   "C"])
            writer.writerow(["Ananya", 22, 95.0,   "A+"])
            writer.writerow(["Aarav",  20, 40.75,  "F"])
            writer.writerow(["Diya",   23, 91.3,   "A+"])
        print(f"Created sample file: {csv_path}")
    else:
        print("Sample file already exists, skipping creation.")

setup_sample_csv()


# =============================================================================
# PART 1 — READING CSV FILES
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
section("1A. csv.reader() — the simplest way to read a CSV: rows as LISTS")
# ─────────────────────────────────────────────────────────────────────────────
# csv.reader(file) gives us back a "reader" object. Looping over it hands
# us one row at a time, where each row is a plain Python LIST of strings.

with open(csv_path, "r", newline="", encoding="utf-8") as file:
    data = csv.reader(file)

    # The very first row in the file is the HEADER (column names), not
    # actual data. next(data) grabs that first row for us AND moves the
    # reader forward, so the loop below starts from the 2nd line onwards.
    header_data = next(data)
    print(f"Header: {header_data}")

    for row in data:
        # Each "row" looks like: ['Yash', '20', '89.456', 'A']
        print(f"row: {row}")


# ─────────────────────────────────────────────────────────────────────────────
section("1B. csv.reader() + converting text into real data types")
# ─────────────────────────────────────────────────────────────────────────────
# IMPORTANT: every single value read from a CSV file comes back as a
# STRING, even things that look like numbers (like "20" or "89.456"). If
# we want to do maths with them (compare, add, round, etc.) we must
# convert them ourselves using int() or float().

with open(csv_path, "r", newline="", encoding="utf-8") as file:
    data = csv.reader(file)
    header_data = next(data)   # skip the header row

    for row in data:
        name  = row[0]                       # stays as a string — names don't need converting
        age   = int(row[1])                  # "20"      -> 20        (whole number)
        marks = round(float(row[2]), 2)      # "89.456"  -> 89.46     (decimal, rounded to 2 places)
        grade = row[3]
        # :<10 pads the name with spaces so all rows line up neatly in the output
        print(f" Name: {name:<10} | Age: {age} | Marks: {marks} | Grade: {grade}")


# ─────────────────────────────────────────────────────────────────────────────
section("1C. csv.DictReader() — the easier way: rows as DICTIONARIES")
# ─────────────────────────────────────────────────────────────────────────────
# Instead of remembering "column 0 is name, column 1 is age...", DictReader
# automatically uses the header row as dictionary KEYS. This means we can
# access values by column NAME (row["name"]) instead of by position
# (row[0]), which is much easier to read and far less error-prone,
# especially once a CSV file has many columns.

with open(csv_path, "r", newline="", encoding="utf-8") as file:
    data = csv.DictReader(file)   # DictReader automatically skips/uses the header row for us
    for row in data:
        # row looks like: {'name': 'Yash', 'age': '20', 'marks': '89.456', 'grade': 'A'}
        name  = row["name"]
        age   = int(row["age"])
        marks = float(row["marks"])
        grade = row["grade"]
        print(f"{name:<10} | age: {age} | marks: {marks} | grade: {grade}")


# =============================================================================
# PART 2 — WORKING WITH THE DATA: filter, sort
# =============================================================================
# A very common real-world pattern: load the ENTIRE CSV into a Python list
# of dictionaries first, then do all your analysis (filtering, sorting,
# calculations) using plain Python, without touching the file again.

# ─────────────────────────────────────────────────────────────────────────────
section("2A. Load every row into a Python list (list of dicts)")
# ─────────────────────────────────────────────────────────────────────────────

students = []   # will end up looking like: [ {row1}, {row2}, {row3}, ... ]

with open(csv_path, "r", newline="", encoding="utf-8") as file:
    data = csv.DictReader(file)   # DictReader gives us: {}, {}, {}, {}...
    for row in data:
        students.append(row)

print(f"Loaded {len(students)} students into memory:")
for s in students:
    print(f"  {s}")


# ─────────────────────────────────────────────────────────────────────────────
section("2B. FILTER — keep only students who passed (marks >= 60)")
# ─────────────────────────────────────────────────────────────────────────────
# There are two common ways to filter a list in Python — both do exactly
# the same job, just written differently. Pick whichever style you find
# more readable.

# METHOD 1: a "list comprehension" — reads as "give me each student s,
# but only keep it if s['marks'] is 60 or more".
pass_students = [s for s in students if float(s["marks"]) >= 60]

# METHOD 2: using the built-in filter() function with a lambda (a small,
# unnamed function). filter() keeps only the items where the lambda
# returns True, and list() turns the result back into a normal list.
# (This line is commented out because it does the exact same thing as
# METHOD 1 above — uncomment it if you'd like to see it work too.)
# pass_students = list(filter(lambda s: float(s["marks"]) >= 60, students))

print(f"\n--- Students who passed (marks >= 60): {len(pass_students)} ---")
for passing_student in pass_students:
    print(passing_student["name"], "-", passing_student["marks"])


# ─────────────────────────────────────────────────────────────────────────────
section("2C. SORT — rank students from highest marks to lowest")
# ─────────────────────────────────────────────────────────────────────────────
# sorted(list, key=..., reverse=...) creates a NEW sorted list without
# changing the original one.
#   key=lambda s: float(s["marks"])  -> tells Python "sort using each
#                                       student's marks value"
#   reverse=True                     -> highest marks first (descending)
#
# NOTE: we must convert marks to float() inside the key, because
# DictReader gives us marks as a STRING, and sorting strings would
# incorrectly put "9.0" after "80.0" (since it compares them character by
# character, like a dictionary would, not as real numbers).

sorted_students = sorted(students, key=lambda s: float(s["marks"]), reverse=True)

print("\n--- Full ranking table ---")
for rank, s in enumerate(sorted_students, start=1):
    # f"{s['name']:<10}" pads the name with spaces so the ranks line up neatly.
    print(f"Rank {rank}: {s['name']:<10} : {s['marks']}")


# =============================================================================
# PART 3 — WRITING CSV FILES
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
section("3A. csv.writer() — write a few individual rows")
# ─────────────────────────────────────────────────────────────────────────────
# "w" (write) mode creates a brand-new file, or ERASES the file completely
# if it already exists, before writing our new rows into it. Be careful —
# only use "w" when you genuinely want to replace the file's content.

with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "marks"])   # header row — always written first
    writer.writerow(["Prashant", 90])
    writer.writerow(["Yash", 89])
    writer.writerow(["Rohit", 88])

print(f"File written: {output_path}")


# ─────────────────────────────────────────────────────────────────────────────
section("3B. csv.writer() — write MANY rows at once with writerows()")
# ─────────────────────────────────────────────────────────────────────────────
# writer.writerows(list_of_lists) is much quicker than calling writerow()
# over and over — you just hand it a list where each item is itself a row
# (a list of values), including the header as the very first item.

students_table = [
    ["Name", "Marks"],      # header row
    ["Yash", 89],
    ["Rohit", 88],
    ["Ananya", 95],
    ["Aarav", 76],
    ["Diya", 91],
    ["Kabir", 84],
    ["Meera", 92],
    ["Vivaan", 68],
    ["Isha", 73],
    ["Rohan", 85],
]

with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(students_table)   # this OVERWRITES the file from Part 3A

print(f"File written (overwritten with the new table): {output_path}")


# ─────────────────────────────────────────────────────────────────────────────
section("3C. csv.DictWriter() — write rows FROM a list of dictionaries")
# ─────────────────────────────────────────────────────────────────────────────
# DictWriter is handy when your data is already stored as a list of
# dictionaries in your program (which is very common), because you don't
# have to manually reorder each dict's values into a list yourself.

students_records = [
    {"Roll_No": 101, "Name": "Yash",   "Score": 89, "Grade": "A",  "Attendance_Pct": 92.5, "Status": "Pass"},
    {"Roll_No": 102, "Name": "Rohit",  "Score": 88, "Grade": "A",  "Attendance_Pct": 88.0, "Status": "Pass"},
    {"Roll_No": 103, "Name": "Ananya", "Score": 95, "Grade": "A+", "Attendance_Pct": 96.2, "Status": "Pass"},
    {"Roll_No": 104, "Name": "Aarav",  "Score": 76, "Grade": "B",  "Attendance_Pct": 81.0, "Status": "Pass"},
    {"Roll_No": 105, "Name": "Diya",   "Score": 91, "Grade": "A+", "Attendance_Pct": 94.0, "Status": "Pass"},
]

# "header" here lists the CSV columns IN ORDER. This must exactly match
# the keys used inside each dictionary above (fieldnames tells DictWriter
# which key goes into which column, and in what order).
header = ["Roll_No", "Name", "Score", "Grade", "Attendance_Pct", "Status"]

with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()             # writes the column names as the first row
    writer.writerows(students_records)   # then writes every record below it

print(f"File written (dictionary records): {output_path}")


# =============================================================================
# PART 4 — APPENDING TO AN EXISTING CSV FILE
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
section("4A. Append a new row WITHOUT erasing what's already in the file")
# ─────────────────────────────────────────────────────────────────────────────
# "a" (append) mode keeps everything already in the file and simply adds
# new rows to the END of it — unlike "w" mode, which would erase
# everything first. This is the mode to use when you want to keep adding
# new records over time (e.g. a new student enrolling, a new sale being
# recorded, and so on).

new_student = [[345, "Naman2", 90, "A"]]   # writerows() expects a list of rows,
                                            # so even one row must be wrapped in [ ]

with open(output_path, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(new_student)

print("New student added to the file (previous rows are untouched).")

# Let's read the file back to PROVE that both the old rows AND the new row
# are present — nothing was lost.
print("\n--- Final contents of the output file ---")
with open(output_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# =============================================================================
# QUICK REFERENCE CHEAT SHEET
# =============================================================================
#
#  ── Reading ────────────────────────────────────────────────────────────────
#  csv.reader(file)                      -> rows come back as plain LISTS
#  csv.DictReader(file)                  -> rows come back as DICTIONARIES
#                                            (uses the header row as keys)
#  next(reader)                          -> manually grab/skip the header row
#                                            (not needed with DictReader — it
#                                             handles the header automatically)
#  ALL values are read back as STRINGS — convert with int()/float() yourself.
#
#  ── Writing ────────────────────────────────────────────────────────────────
#  csv.writer(file)                      -> write rows FROM lists
#  csv.DictWriter(file, fieldnames=[...])-> write rows FROM dictionaries
#  writer.writerow([...])                -> write exactly ONE row
#  writer.writerows([[...], [...]])      -> write MANY rows at once
#  writer.writeheader()                  -> write just the header row
#                                            (DictWriter only)
#
#  ── File modes ─────────────────────────────────────────────────────────────
#  "r"  -> read only (file must already exist)
#  "w"  -> write — creates a new file, or ERASES an existing one first
#  "a"  -> append — adds new rows to the end, keeps existing content
#  Always add newline="" when opening CSV files (read OR write), to avoid
#  extra blank rows appearing on Windows.
#
#  ── Filtering & sorting a list of dict rows ────────────────────────────────
#  [s for s in rows if CONDITION]                 -> list comprehension filter
#  list(filter(lambda s: CONDITION, rows))         -> same result, filter() style
#  sorted(rows, key=lambda s: s["col"], reverse=True) -> sort by any column
#
#  ── Golden rules to remember ──────────────────────────────────────────────
#  1. Always use "with open(...) as file:" so files close automatically.
#  2. Always pass newline="" when working with CSV files.
#  3. "w" mode ERASES existing content — use "a" if you want to keep it.
#  4. CSV values always come back as STRINGS — convert numbers yourself.
#  5. DictWriter's fieldnames must exactly match the keys in your dicts.
#  6. Use DictReader/DictWriter for readability once a file has many columns.

