# =============================================================================
#  PYTHON JSON FILE HANDLING — Complete Beginner-to-Advanced Guide
#  Purpose : Learn how to read, write, update, and append JSON files
#
#  HOW TO USE THIS FILE:
#  ----------------------
#  This script is fully self-contained. You don't need to create any files
#  or folders yourself — when you run it, it first creates the sample JSON
#  files it needs (student.json, etc.), then walks through every JSON
#  operation on them: reading simple and nested data, writing dicts and
#  lists, updating existing files, "appending" to a JSON list, and
#  converting between JSON strings and Python objects — with clear
#  comments explaining WHY each thing is done, not just what the code does.
#
#  Just run:  python json_handling.py
#  ...and read the printed output alongside the comments below.
# =============================================================================

# ── WHAT IS JSON? ────────────────────────────────────────────────────────────
# JSON stands for "JavaScript Object Notation", but it's used everywhere in
# Python too — it's the most common format for storing STRUCTURED data:
# data that can be nested, like an object with properties, or a list full
# of objects. It's used constantly in web APIs, app config/settings files,
# and databases, because it maps almost perfectly onto Python's own
# dictionaries and lists.
#
# JSON  <-->  Python — how the pieces match up:
#   {}          <-->  dict            e.g. {"name": "Yash"}
#   []          <-->  list            e.g. [1, 2, 3]
#   "string"    <-->  str
#   123 / 1.5   <-->  int / float
#   true/false  <-->  True / False   (note the capital letters in Python!)
#   null        <-->  None
#
# THE 4 MAIN TOOLS IN THE json MODULE:
#   json.load(file)        -> reads JSON from an open FILE  -> Python object
#   json.loads(text)       -> reads JSON from a STRING      -> Python object
#                              (notice the extra "s" — it means "string")
#   json.dump(data, file)  -> writes a Python object into an open FILE as JSON
#   json.dumps(data)       -> converts a Python object into a JSON STRING
#                              (again, the extra "s" means "string")

import json
import os

# BASE = the folder this script lives in. Every other path is built
# relative to it, so the script works no matter where you place the
# project folder on your computer.
BASE = os.path.dirname(os.path.abspath(__file__))

json_path   = os.path.join(BASE, "PythonBasics", "files",  "student.json")
output_path = os.path.join(BASE, "PythonBasics", "output", "json", "student.json")

def section(title):
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}")


# =============================================================================
# PART 0 — ONE-TIME SETUP: create the folders and the sample JSON file
# =============================================================================
# This just prepares a student.json file (with a nested "students" section
# inside it) so the rest of the script has real data to practice on. Feel
# free to skim this — the real JSON learning starts at PART 1.

def setup_sample_json():
    section("0. SETUP — creating the sample student.json file (if missing)")

    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Only create it if it doesn't already exist, so re-running this
    # script won't wipe out any edits you've made to it.
    if not os.path.exists(json_path):
        sample_student = {
            "name": "Yash",
            "age": 20,
            "course": "Python",
            "marks": {"Python": 92, "Maths": 85},
            "passed": True,
            # a JSON file can hold MULTIPLE nested records too — here,
            # "students" is a dict where each KEY is a student id and each
            # VALUE is another dict describing that student.
            "students": {
                "s1": {"name": "Rohit",  "marks": 88},
                "s2": {"name": "Ananya", "marks": 95},
                "s3": {"name": "Aarav",  "marks": 76},
            }
        }
        with open(json_path, "w", encoding="utf-8") as file:
            json.dump(sample_student, file, indent=4)
        print(f"Created sample file: {json_path}")
    else:
        print("Sample file already exists, skipping creation.")

setup_sample_json()


# =============================================================================
# PART 1 — READING JSON FILES
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
section("1A. json.load() — read a JSON file into a Python dict")
# ─────────────────────────────────────────────────────────────────────────────
# json.load(file) parses the JSON text inside the file and hands us back a
# normal Python object — usually a dict (if the file starts with { } ) or
# a list (if the file starts with [ ]).

with open(json_path, "r", encoding="utf-8") as file:
    student = json.load(file)

print(student)
print(f"(This came back as a Python {type(student).__name__})")   # <class 'dict'>


# ─────────────────────────────────────────────────────────────────────────────
section("1B. Accessing individual values from the loaded dict")
# ─────────────────────────────────────────────────────────────────────────────
# NOTE: when you build an f-string that ALSO needs quotes inside it (like
# student['marks']["Python"] below), Python lets you mix single quotes '
# and double quotes " so the string doesn't get confused about where it
# ends. That's why you'll see 'name' in single quotes here.

print(
    f"{student['name']} | {student['age']} | {student['course']} | "
    f"{student['marks']} | {int(student['passed'])}"
)

# We can also reach INSIDE a nested value. student["marks"] is itself a
# dictionary, so student["marks"]["Python"] means "go into marks, then
# grab the Python key from there".
print(
    f"{student['name']} | {student['age']} | {student['course']} | "
    f"Python marks: {student['marks']['Python']} | Passed: {int(student['passed'])}"
)


# ─────────────────────────────────────────────────────────────────────────────
section("1C. Looping through a nested dictionary (marks by subject)")
# ─────────────────────────────────────────────────────────────────────────────
# student["marks"] looks like: {"Python": 92, "Maths": 85}
# .items() lets us loop through BOTH the key (subject) and the value
# (score) at the same time.

for subject, score in student["marks"].items():
    print(f" {student['name']}  {subject:<10}: {score:<2}")


# ─────────────────────────────────────────────────────────────────────────────
section("1D. Reading MULTIPLE nested records stored inside one JSON file")
# ─────────────────────────────────────────────────────────────────────────────
# Our sample file also has a "students" section, which looks like:
#   "students": {
#       "s1": {"name": "Rohit",  "marks": 88},
#       "s2": {"name": "Ananya", "marks": 95},
#       ...
#   }
# This is a dictionary OF dictionaries — each key ("s1", "s2"...) points
# to another dict describing one student. We loop through it the same way
# as any other dict, using .items().

for key, value in student["students"].items():
    print(key, value)
    print(f"  -> {value['name']} | marks: {value['marks']}")


# =============================================================================
# PART 2 — WRITING JSON FILES
# =============================================================================
# json.dump(data, file, indent=4) writes our Python data into a file.
#   indent=4 -> makes the JSON file nicely indented and readable for
#               humans (without it, everything gets squeezed onto one
#               single line).

# ─────────────────────────────────────────────────────────────────────────────
section("2A. json.dump() — writing a simple dictionary to a JSON file")
# ─────────────────────────────────────────────────────────────────────────────

simple_output_path = os.path.join(BASE, "PythonBasics", "output", "json", "simple.json")
os.makedirs(os.path.dirname(simple_output_path), exist_ok=True)

data = {"name": "Naman", "age": 34, "city": "Delhi"}

with open(simple_output_path, "w", encoding="utf-8") as file:
    json.dump(data, file)   # no indent here -> saved as one compact line

print("Write is complete.")
print(f"Saved to: {simple_output_path}")


# ─────────────────────────────────────────────────────────────────────────────
section("2B. json.dump() — writing DEEPLY NESTED data, with indent=4")
# ─────────────────────────────────────────────────────────────────────────────
# JSON isn't limited to flat key-value pairs — dictionaries can contain
# lists, which can contain more dictionaries, and so on, as deep as you
# need. Here's a realistic example: a company with a list of employees,
# where each employee has their own nested contact info, skills, and
# project list.

company_data = {
    "company": "TechInnovate",
    "employees": [
        {
            "id": 101,
            "name": "Alice Smith",
            "role": "Senior Developer",
            "contact": {
                "email": "alice.smith@example.com",
                "phone": "+1-555-0198"
            },
            "skills": ["Python", "AWS", "GraphQL"],
            "projects": [
                {"name": "Alpha", "status": "Completed"},
                {"name": "Beta", "status": "In Progress"}
            ]
        },
        {
            "id": 102,
            "name": "Bob Jones",
            "role": "UI/UX Designer",
            "contact": {
                "email": "bob.jones@example.com",
                "phone": "+1-555-0143"
            },
            "skills": ["Figma", "React", "CSS"],
            "projects": [
                {"name": "Beta", "status": "In Progress"},
                {"name": "Gamma", "status": "Planning"}
            ]
        }
    ]
}

nested_output_path = os.path.join(BASE, "PythonBasics", "output", "json", "nested.json")
os.makedirs(os.path.dirname(nested_output_path), exist_ok=True)

with open(nested_output_path, "w", encoding="utf-8") as file:
    # indent=4 formats the JSON with 4-space indentation, which makes deeply
    # nested files like this MUCH easier for a human to read and debug.
    json.dump(company_data, file, indent=4)

print(f"Saved nested company data to: {nested_output_path}")


# ─────────────────────────────────────────────────────────────────────────────
section("2C. Writing a Python LIST (of dicts) to a JSON file")
# ─────────────────────────────────────────────────────────────────────────────
# A JSON file doesn't have to start with a dict ( { } ) — it can start
# with a list ( [ ] ) too, if that's what you hand json.dump().

user_profiles = [
    {"user_id": "usr_01", "username": "coder_ace", "active": True,  "login_count": 42},
    {"user_id": "usr_02", "username": "pixel_art", "active": False, "login_count": 12},
    {"user_id": "usr_03", "username": "data_wiz",  "active": True,  "login_count": 115},
]

list_output_path = os.path.join(BASE, "PythonBasics", "output", "json", "list.json")
os.makedirs(os.path.dirname(list_output_path), exist_ok=True)

with open(list_output_path, "w", encoding="utf-8") as file:
    json.dump(user_profiles, file, indent=2)

print(f"Saved list of user profiles to: {list_output_path}")


# =============================================================================
# PART 3 — UPDATING DATA IN A JSON FILE
# =============================================================================
# JSON files have NO built-in "append" or "update" mode, unlike text files
# ("a" mode). This is because the entire file is really just one single
# structured object — you can't safely tack extra text onto the end of it
# without possibly breaking the JSON format.
#
# Because of that, updating a JSON file ALWAYS follows the same 3 steps:
#   1. READ the file into a Python variable
#   2. MODIFY that Python variable using normal Python code
#   3. WRITE the whole updated variable back out to the file

# ─────────────────────────────────────────────────────────────────────────────
section("3A. Updating one value inside a JSON list")
# ─────────────────────────────────────────────────────────────────────────────

# Step 1: read the existing file back into Python.
with open(list_output_path, "r", encoding="utf-8") as file:
    data = json.load(file)

print(f"Username before update: {data[0]['username']}")

# Step 2: modify it like any normal Python list/dict.
data[0]["username"] = "coder_phase"

# Step 3: write the WHOLE updated list back out to the file (this
# overwrites the file completely with the new version).
with open(list_output_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)

print(f"Username after update : {data[0]['username']}")
print("File updated successfully.")


# =============================================================================
# PART 4 — "APPENDING" TO A JSON FILE (read -> modify -> write, again)
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
section("4A. Adding a new record to a JSON file that holds a list")
# ─────────────────────────────────────────────────────────────────────────────
# Reminder: JSON has NO append() function/mode of its own — we simulate
# "appending" using the same read -> modify -> write pattern as before,
# just using Python's normal list .append() method in the "modify" step.
#
# First, let's write out a small students LIST to output_path so we have
# something to append a new record to.

starter_students = [
    {"name": "Yash",  "age": 20, "marks": 92},
    {"name": "Priya", "age": 22, "marks": 55},
]
with open(output_path, "w", encoding="utf-8") as file:
    json.dump(starter_students, file, indent=3)

# Step 1: read the existing list of students from the file.
with open(output_path, "r", encoding="utf-8") as file:
    students = json.load(file)

print("Students before append:")
print(students)

# Step 2: use Python's normal list.append() to add one more student.
students.append({"name": "Rohit", "age": 45, "marks": 90})

# Step 3: write the WHOLE updated list back out to the file.
with open(output_path, "w", encoding="utf-8") as file:
    json.dump(students, file, indent=3)

print("\nStudents after append:")
print(students)
print(f"\nTotal students in file now: {len(students)}")


# =============================================================================
# PART 5 — json.dumps() / json.loads(): converting to/from TEXT (no file)
# =============================================================================
# Sometimes you don't want to touch the disk at all — you just want to
# turn Python data into a JSON-formatted STRING (for example, to print it,
# send it over a network/API, or store it inside a database column).
# That's exactly what the "s" versions of the functions are for
# (dumpS / loadS both mean "...to/from a string").

# ─────────────────────────────────────────────────────────────────────────────
section("5A. json.dumps() — Python dict -> JSON string")
# ─────────────────────────────────────────────────────────────────────────────

person = {"name": "Yash", "age": 24}

json_string = json.dumps(person, indent=3)
print(json_string)
print(f"(This is a Python {type(json_string).__name__})")   # <class 'str'>


# ─────────────────────────────────────────────────────────────────────────────
section("5B. json.loads() — JSON string -> Python dict (the reverse)")
# ─────────────────────────────────────────────────────────────────────────────

dict_format = json.loads(json_string)
print(dict_format)
print(f"(This is a Python {type(dict_format).__name__})")   # <class 'dict'>


# =============================================================================
# QUICK REFERENCE CHEAT SHEET
# =============================================================================
#
#  ── Reading ────────────────────────────────────────────────────────────────
#  json.load(file)          -> read a JSON FILE   -> Python dict/list
#  json.loads(text)         -> read a JSON STRING  -> Python dict/list
#  Access nested values just like normal Python: data["marks"]["Python"]
#  Loop through a dict's key/value pairs with: for key, value in d.items():
#
#  ── Writing ────────────────────────────────────────────────────────────────
#  json.dump(data, file)         -> write Python data  -> into a JSON FILE
#  json.dumps(data)              -> write Python data  -> as a JSON STRING
#  indent=4                      -> pretty-print with readable indentation
#                                    (omit it for a compact, one-line file)
#  ensure_ascii=False            -> allow special/non-English characters
#                                    to be saved as-is instead of \uXXXX codes
#
#  ── Updating / "Appending" (same pattern for both!) ────────────────────────
#  JSON has NO append mode. Always do:
#     1. data = json.load(file)      # READ
#     2. data[...] = new_value       # MODIFY   (or data.append(...) for lists)
#     3. json.dump(data, file, ...)  # WRITE the whole thing back
#
#  ── Golden rules to remember ──────────────────────────────────────────────
#  1. Always use "with open(...) as file:" so files close automatically.
#  2. Always pass encoding="utf-8" to avoid character/encoding problems.
#  3. "w" mode ERASES existing content — that's fine here, since updating
#     a JSON file always means "read it all, then write it all back".
#  4. Use indent=4 (or any number) whenever the file needs to stay
#     human-readable; skip it for machine-only files to save space.
#  5. dump/load = files.   dumpS/loadS = strings.  (the "s" is the clue!)

