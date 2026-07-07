#Reading json files
import json

json_path="PythonBasics/files/student.json"


with open(json_path,"r") as file:
    student=json.load(file)

# print(student)

# Use single quotes inside the f-string to avoid syntax errors
# print(
#     f"{student['name']} | {student['age']} | {student['course']} | {student['marks']} | {int(student['passed'])}"
# )  
# print(
#     f"{student['name']} | {student['age']} | {student['course']} | {student['marks']["Python"]} | {int(student['passed'])}"
# )

# for subject, score in student["marks"].items():
#     print(f" {student['name']}  {subject:<10}:{score:<2}")   


# multiple records in nested json

for key, value in student["students"].items():
    print(key, value)
    print(f"{value['name']}| {value['marks']}")
    