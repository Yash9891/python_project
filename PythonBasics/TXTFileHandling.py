# =============================================================================
#  PYTHON FILE HANDLING — Complete Guide (Basic to Advanced)
#  Author  : Yash
#  Purpose : Learn how to work with TXT, CSV, and JSON files in Python
# =============================================================================

# FOLDER STRUCTURE (YOU CREATE THESE MANUALLY):
# ──────────────────────────────────────────────
# filehandling_project/
# │
# ├── filehandling.py              ← You are here (this file)
# │
# ├── data/
# │   ├── txt/
# │   │   ├── intro.txt
# │   │   ├── poem.txt
# │   │   └── notes.txt
# │   ├── csv/
# │   │   ├── students.csv
# │   │   └── products.csv
# │   └── json/
# │       ├── student.json
# │       ├── students_list.json
# │       └── config.json
# │
# ├── output/                      ← keep this folder empty, script fills it
# └── backup/                      ← keep this folder empty, script fills it

# -----------------------------------------------------------------------------
# WHAT IS FILE HANDLING?
# -----------------------------------------------------------------------------
# File handling means reading data FROM files and writing data INTO files.
# In real projects, you almost always need to:
#   - Save data so it is not lost when the program closes
#   - Read data from files created by someone else (CSV reports, JSON APIs)
#   - Write log files to track what happened in the program
#
# Python makes this very easy with just one built-in function: open()
# And two standard library modules: csv  and  json

import csv
import json

# We will use simple, direct file paths in this file.
# Since YOU create the folders, just make sure this script sits inside
# filehandling_project/ and the paths below will work.

def section(title):
    print(f"\n{'=' * 55}")
    print(f"  {title}")
    print(f"{'=' * 55}")


# =============================================================================
# PART 1 — TEXT FILE HANDLING (.txt)
# =============================================================================
#
# WHAT IS A TEXT FILE?
#   The simplest type of file. Stores plain readable text.
#   Opens in Notepad, VS Code, any text editor.
#   Each line inside the file ends with a hidden character called \n
#   (newline). That's what tells the computer "start a new line here".
#
# ─────────────────────────────────────────────────────────────────────────────
# THE open() FUNCTION — the only thing you need to work with files
# ─────────────────────────────────────────────────────────────────────────────
#
#   open("path/to/file",  "mode",  encoding="utf-8")
#          ↑                ↑              ↑
#     file location     what to do    handle special
#                       with it       characters safely
#
# FILE MODES — the second argument tells Python what you want to do:
#
#   "r"  → READ       Open the file and READ it. File must already exist.
#                     If file doesn't exist → FileNotFoundError crash.
#
#   "w"  → WRITE      Create a new file and WRITE into it.
#                     ⚠️  If file already exists → it gets DELETED and recreated!
#                     Use carefully.
#
#   "a"  → APPEND     Open file and ADD content at the END.
#                     Does NOT delete existing content.
#                     If file doesn't exist → creates a new one.
#
#   "x"  → CREATE     Create a brand new file.
#                     If file already exists → gives an error (safe mode).
#
# ─────────────────────────────────────────────────────────────────────────────
# THE "with" STATEMENT — always use this when opening files
# ─────────────────────────────────────────────────────────────────────────────
#
#   with open("file.txt", "r") as f:
#       content = f.read()
#
#   WHY use "with"?
#   When you open a file, Python "holds" it open (locks it).
#   If your code crashes in the middle, the file stays locked — bad!
#   "with" automatically CLOSES the file when you're done, no matter what.
#   Think of it like this: "with" = try + finally + file.close() all in one.
#
#   The variable after "as" (we use 'f') is the file object.
#   You call methods on it: f.read(), f.write(), etc.
#
# ─────────────────────────────────────────────────────────────────────────────
# BONUS: open()/close() WITHOUT "with" (the manual, old-school way)
# ─────────────────────────────────────────────────────────────────────────────
#
#   You *can* open a file without "with", but then YOU are responsible for
#   closing it yourself by calling file.close(). If you forget to close it,
#   or your code crashes before reaching close(), the file can stay locked.
#   This is why "with" (shown above) is always the recommended approach —
#   the example below is just to show you what's happening under the hood.
#
#   filepath = "data/txt/intro.txt"
#   file = open(filepath, "r")   # opening the file manually
#   desc = file.read()           # reading
#   file.close()                 # you must close it yourself
#   print(desc)


# =============================================================================
# 1A. READING a text file — 4 ways
# =============================================================================

section("1A. READ — Reading a text file")

# ── TINY EXAMPLE FIRST ───────────────────────────────────────────────────────
# Imagine data/txt/intro.txt contains:
#   Hello, this is a simple text file.
#   Python makes reading and writing files very easy.
#   This file has multiple lines.
#   Each line can be read separately.
#   End of file.

# ─── WAY 1: f.read() — gets the WHOLE file as ONE big string ─────────────────
# Use this when: you want everything at once, file is small.
print("\n--- WAY 1: f.read() — entire file as one string ---")

with open("data/txt/intro.txt", "r", encoding="utf-8") as f:
    content = f.read()      # reads EVERYTHING — one giant string

print(content)
# Output:
# Hello, this is a simple text file.
# Python makes reading and writing files very easy.
# ...

print(f"Data type returned: {type(content)}")   # <class 'str'>
print(f"Total characters : {len(content)}")


# ─── WAY 2: f.readlines() — gets ALL lines as a LIST ────────────────────────
# Use this when: you want to work with individual lines, small file.
# Each item in the list = one line from the file (including the \n at the end).
print("\n--- WAY 2: f.readlines() — all lines as a list ---")

with open("data/txt/intro.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()   # returns: ["line1\n", "line2\n", "line3\n", ...]

print(lines)
# Output: ['Hello, this is a simple text file.\n', 'Python makes....\n', ...]

print(f"Data type returned  : {type(lines)}")    # <class 'list'>
print(f"Number of lines     : {len(lines)}")
print(f"First line          : {lines[0].strip()}")   # .strip() removes the \n
print(f"Last line           : {lines[-1].strip()}")

# ─── EXTRA: readlines() gives you a LIST — so normal indexing works too ──────
# Since readlines() returns a list, you can grab ANY line by its index,
# not just first/last. Index 3 = the 4th line in the file.
print("\n--- Extra: indexing into the readlines() list ---")

with open("data/txt/intro.txt", "r", encoding="utf-8") as f:
    data_in_lines = f.readlines()

print(data_in_lines)
print(type(data_in_lines))
if len(data_in_lines) > 3:
    print(f"4th line (index 3): {data_in_lines[3].strip()}")


# ─── WAY 3: f.readline() — reads ONE line at a time ──────────────────────────
# Use this when: you want to process one line at a time manually.
# Every call to readline() moves forward to the next line.
print("\n--- WAY 3: f.readline() — one line at a time ---")

with open("data/txt/intro.txt", "r", encoding="utf-8") as f:
    first_line  = f.readline()   # reads line 1, cursor moves to line 2
    second_line = f.readline()   # reads line 2, cursor moves to line 3
    third_line  = f.readline()   # reads line 3

print(f"Line 1 → {first_line.strip()}")
print(f"Line 2 → {second_line.strip()}")
print(f"Line 3 → {third_line.strip()}")

# ─── EXTRA: readline() always returns a STRING — convert it if you need to ───
# f.readline() (and f.read()) ALWAYS give you back a string (type str),
# even if the line only contains digits like "12345". If you need it as a
# real number, you must convert it yourself using int() or float().
print("\n--- Extra: converting a line's text into a number ---")

print(f"Type of second_line: {type(second_line)}")   # <class 'str'>

# Only try int() conversion if the stripped line is actually numeric,
# otherwise Python will raise a ValueError.
stripped_third = third_line.strip()
if stripped_third.isdigit():
    phonenum = int(stripped_third)
    print(f"{phonenum}, {type(phonenum)}")
else:
    print(f"Line 3 is not a plain number, so it stays a string: '{stripped_third}'")


# ─── WAY 4: Loop directly over the file (BEST PRACTICE for large files) ──────
# Use this when: file is large (thousands of lines), you process line by line.
# This does NOT load the whole file into memory at once — very efficient.
# enumerate(f, start=1) gives you a line number alongside each line.
print("\n--- WAY 4: Loop line by line (best for large files) ---")

with open("data/txt/intro.txt", "r", encoding="utf-8") as f:
    for line_number, line in enumerate(f, start=1):
        clean_line = line.strip()    # remove \n from the end
        print(f"  Line {line_number}: {clean_line}")

# Output:
#   Line 1: Hello, this is a simple text file.
#   Line 2: Python makes reading and writing files very easy.
#   ...


# =============================================================================
# 1B. WRITING to a text file
# =============================================================================

section("1B. WRITE — Writing to a text file")

# ─── TINY EXAMPLE: write a single line ───────────────────────────────────────
# "w" mode creates the file if it doesn't exist.
# ⚠️  If the file ALREADY EXISTS — "w" mode DELETES the old content first!
print("\n--- Simple write: one line ---")

with open("output/simple.txt", "w", encoding="utf-8") as f:
    f.write("Hello from Python!\n")   # \n = go to next line

print("Done! Check output/simple.txt")

# ─── EXTRA: "w" mode creates missing FOLDERS' files too, but not folders ─────
# Note: open() will happily create a new FILE even if the filename looks
# unusual (e.g. "writefile.txt67"), as long as the FOLDER already exists.
# It will NOT create missing folders for you — only the file itself.
print("\n--- Extra: write() always creates the file if the folder exists ---")

sample_text = "Hello,  How r u 2 \ni am fine"
with open("output/writefile_demo.txt", "w", encoding="utf-8") as f:
    f.write(sample_text)

print("File is done, check: output/writefile_demo.txt")


# ─── Write multiple lines one by one ─────────────────────────────────────────
print("\n--- Write multiple lines using f.write() ---")

with open("output/my_output.txt", "w", encoding="utf-8") as f:
    f.write("Line 1: This file was created by Python.\n")
    f.write("Line 2: Writing is easy with Python.\n")
    f.write("Line 3: File handling is very useful!\n")

print("Written: output/my_output.txt")

# Read it back and confirm
with open("output/my_output.txt", "r", encoding="utf-8") as f:
    print(f.read())


# ─── writelines() — write a LIST of lines all at once ────────────────────────
# Note: writelines does NOT add \n automatically — you must include it yourself.
print("\n--- writelines(): write from a list ---")

my_lines = [
    "First line from a list\n",
    "Second line from a list\n",
    "Third line from a list\n",
]

with open("output/list_output.txt", "w", encoding="utf-8") as f:
    f.writelines(my_lines)   # writes all 3 lines at once

print("Written: output/list_output.txt")

# Read it back
with open("output/list_output.txt", "r", encoding="utf-8") as f:
    print(f.read())

# ─── EXTRA: writelines() with a longer list, last item without \n ───────────
# It's common to leave the \n off the very last item in the list, since
# there's nothing after it that needs to start on a new line.
print("\n--- Extra: writelines() with 5 lines (last one has no \\n) ---")

sample_list = [
    "First line of text\n",
    "Second line of text\n",
    "Third line of text\n",
    "Fourth line of text\n",
    "Fifth line of text",
]

with open("output/writefile_list.txt", "w", encoding="utf-8") as f:
    f.writelines(sample_list)

print("File is written: output/writefile_list.txt")


# =============================================================================
# 1C. APPEND — Adding to a file without deleting existing content
# =============================================================================

section("1C. APPEND — Adding to an existing file")

# ─── TINY EXAMPLE: what append looks like ────────────────────────────────────
# "a" mode = ADD to the end. Never deletes existing content.
# If the file doesn't exist yet — "a" creates it (like "w").
print("\n--- Append mode demo ---")

# Step 1: create the file with some initial content
with open("output/log.txt", "w", encoding="utf-8") as f:
    f.write("=== Application Log ===\n")
    f.write("Log started.\n")

print("Initial file created.")

# Step 2: append more lines later (imagine this runs later in the day)
with open("output/log.txt", "a", encoding="utf-8") as f:
    f.write("Entry: User logged in.\n")
    f.write("Entry: File uploaded successfully.\n")

print("Two entries appended.")

# Step 3: append even more later
with open("output/log.txt", "a", encoding="utf-8") as f:
    f.write("Entry: User logged out.\n")

print("One more entry appended.")

# Read the final file — you will see ALL entries, nothing was deleted
with open("output/log.txt", "r", encoding="utf-8") as f:
    print("\nFinal log.txt content:")
    print(f.read())

# Output:
# === Application Log ===
# Log started.
# Entry: User logged in.
# Entry: File uploaded successfully.
# Entry: User logged out.

# ─── EXTRA: appending a mix of a literal string and a variable ─────────────
# You can call f.write() more than once inside the same "a" block, mixing
# a plain string with a variable that holds more text.
print("\n--- Extra: appending a literal string plus a variable ---")

extra_data = "\nHello 12 3"
with open("output/log.txt", "a", encoding="utf-8") as f:
    f.write("\nThis is a new append line")
    f.write(extra_data)

print("Data appended (literal string + variable).")

with open("output/log.txt", "r", encoding="utf-8") as f:
    print(f.read())


# =============================================================================
# 1D. USEFUL TEXT FILE OPERATIONS
# =============================================================================

section("1D. Useful Text File Operations")

# ─── Count lines, words, and characters ──────────────────────────────────────
print("\n--- Count: lines, words, characters in a file ---")

with open("data/txt/intro.txt", "r", encoding="utf-8") as f:
    content = f.read()

# splitlines() splits by \n and gives a clean list (no \n in each item)
all_lines = content.splitlines()

# split() splits by any whitespace (spaces, tabs, newlines) — gives words
all_words = content.split()

print(f"Lines      : {len(all_lines)}")
print(f"Words      : {len(all_words)}")
print(f"Characters : {len(content)}")

# ─── EXTRA: splitlines() vs split(" ") side by side ─────────────────────────
# splitlines() breaks the text into a list of LINES (splits on \n).
# split(" ") breaks the text into a list of WORDS (splits on the space
# character specifically — note this can leave extra blank items if there
# are double spaces, unlike plain split() which collapses all whitespace).
print("\n--- Extra: splitlines() vs split(' ') ---")

print("splitlines() result:")
print(all_lines)
print(f"First line via splitlines(): {all_lines[0]}")

words_by_space = content.split(" ")   # split specifically on the space char
print("\nsplit(' ') result (splits on spaces only):")
print(words_by_space)


# ─── Search for a keyword ─────────────────────────────────────────────────────
# Open the file, go through each line, check if keyword is in that line.
# .lower() on both sides = case-insensitive search (Python == python == PYTHON)
print("\n--- Search: find which lines contain a keyword ---")

keyword = "Python"

with open("data/txt/intro.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        if keyword.lower() in line.lower():
            print(f"  Found '{keyword}' on line {i}: {line.strip()}")


# ─── Find and Replace ────────────────────────────────────────────────────────
# Python's str.replace() method swaps every occurrence of a word.
# Steps: Read → Replace in memory (string) → Write back to new file.
print("\n--- Find and Replace ---")

with open("data/txt/intro.txt", "r", encoding="utf-8") as f:
    content = f.read()                              # step 1: read

modified = content.replace("Python", "🐍 Python")  # step 2: replace in memory

with open("output/modified_intro.txt", "w", encoding="utf-8") as f:
    f.write(modified)                               # step 3: write to new file

print("Saved to output/modified_intro.txt")

# Quick verify
with open("output/modified_intro.txt", "r", encoding="utf-8") as f:
    print(f.read())

# ─── EXTRA: CONDITIONAL find-and-replace — only update if the word exists ───
# Sometimes you don't want to blindly overwrite a file every time.
# Better pattern: check "if keyword in data" FIRST, and only replace +
# save the file when the keyword is actually found. Otherwise leave the
# file untouched and just report that nothing changed.
print("\n--- Extra: conditional find-and-replace (only if found) ---")

search_word = "Python"
replace_word = "Java"

with open("data/txt/intro.txt", "r", encoding="utf-8") as f:
    data = f.read()

if search_word in data:
    print("Data is found")
    updateddata = data.replace(search_word, replace_word)
    with open("output/conditional_replace.txt", "w", encoding="utf-8") as f:
        f.write(updateddata)
    print("Data is updated → saved to output/conditional_replace.txt")
else:
    print("No data present: No update")


# ─── Read a specific line number ─────────────────────────────────────────────
# readlines() gives a list. Index [2] = line 3 (lists start from 0).
print("\n--- Read only line number 3 ---")

with open("data/txt/intro.txt", "r", encoding="utf-8") as f:
    all_lines = f.readlines()

print(f"Line 3: {all_lines[2].strip()}")   # index 2 = 3rd line


# ─── Read poem.txt and notes.txt just for practice ───────────────────────────
print("\n--- Reading poem.txt ---")
with open("data/txt/poem.txt", "r", encoding="utf-8") as f:
    print(f.read())

print("\n--- Reading notes.txt ---")
with open("data/txt/notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(" ", line.strip())