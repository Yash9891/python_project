# csv_path=PythonBasics/files/student.csv
import csv
#1. Reading csv files

csv_path="PythonBasics/files/students.csv"

# with open(csv_path, "r", newline="") as file:
#     data=csv.reader(file)

#     header_data=next(data) # it will start reading from 2nd line
#     print(f"Header: {header_data}")

#     for row in data:
#         print(f"rows: {row}")

    
# add dataypes in csv while reading

# with open(csv_path, "r", newline="") as file:
#     data=csv.reader(file)

#     header_data=next(data) # it will start reading from 2nd line
#     # print(f"Header: {header_data}")

#     for row in data:
#         name=row[0]
#         age=int(row[1])       
#         marks=round(float(row[2]), 3)  # .2f u can use in string
#         grade=row[3]
#         print(f" Name: {name:<10} | Age : {age} | Marks {marks}  Grade: {grade}")



# 2nd DictReader

# with open(csv_path, "r", newline="") as file:
#     data=csv.DictReader(file)
#     for row in data:
#         name=row["name"]
#         age=int(row["age"]) 
#         marks=float(row["marks"])
#         grade=(row["grade"])
#         print(f"{name:<10} | age: {age} | marks: {marks}| grade : {grade}")

# Apply filters

students=[]# [row1, row2, row3]

with open(csv_path, "r", newline="") as file:
    data=csv.DictReader(file) # [{}, {}, {}, {}]
    for row in data:
        students.append(row)
        
# print(students)

# pass_students=[s for s in students if int(s["marks"])>=60 ]

# pass_students= list(filter(lambda s: int(s["marks"])>=60,students) )

# for passing_student in pass_students:
#     print(passing_student["name"], "-", passing_student["marks"])


# sorted_students=sorted(students, key=lambda s: int(s["marks"]), reverse=True)

# print(sorted_students)

# for index,s in enumerate(sorted_students, start=2):
#     print(f"Rank:{index}:{s["name"]:<10}:{s["marks"]}")


# writing csv files

output_path="PythonBasics/output/csv/student.csv"
# with open(output_path, "w", newline="") as file:
#     writer=csv.writer(file) 
#     writer.writerow(["name", "marks"]) # header
#     writer.writerow(["Prashant", 90])
#     writer.writerow(["yash", 89])
#     writer.writerow(["Rohit", 88])

# print("File is written")


# writing multiple records in csv

# students = [
#     ["Name", "Marks"], # header
#     ["Yash", 89],
#     ["Rohit", 88],
#     ["Ananya", 95],
#     ["Aarav", 76],
#     ["Diya", 91],
#     ["Kabir", 84],
#     ["Meera", 92],
#     ["Vivaan", 68],
#     ["Isha", 73],
#     ["Rohan", 85]
# ]

# with open(output_path, "w", newline="") as file:
#     writer=csv.writer(file)
#     writer.writerows(students)

# print("File is written")

# Writing muliple dict records in csv

# students = [
#     {"Roll_No": 101, "Name": "Yash", "Score": 89, "Grade": "A", "Attendance_Pct": 92.5, "Status": "Pass"},
#     {"Roll_No": 102, "Name": "Rohit", "Score": 88, "Grade": "A", "Attendance_Pct": 88.0, "Status": "Pass"},
#     {"Roll_No": 103, "Name": "Ananya", "Score": 95, "Grade": "A+", "Attendance_Pct": 96.2, "Status": "Pass"},
#     {"Roll_No": 104, "Name": "Aarav", "Score": 76, "Grade": "B", "Attendance_Pct": 81.0, "Status": "Pass"},
#     {"Roll_No": 105, "Name": "Diya", "Score": 91, "Grade": "A+", "Attendance_Pct": 94.0, "Status": "Pass"},
#     {"Roll_No": 106, "Name": "Kabir", "Score": 84, "Grade": "B+", "Attendance_Pct": 87.5, "Status": "Pass"},
#     {"Roll_No": 107, "Name": "Meera", "Score": 92, "Grade": "A+", "Attendance_Pct": 95.0, "Status": "Pass"},
#     {"Roll_No": 108, "Name": "Vivaan", "Score": 68, "Grade": "C", "Attendance_Pct": 74.5, "Status": "Pass"},
#     {"Roll_No": 109, "Name": "Isha", "Score": 73, "Grade": "B", "Attendance_Pct": 79.0, "Status": "Pass"},
#     {"Roll_No": 110, "Name": "Rohan", "Score": 85, "Grade": "A", "Attendance_Pct": 89.1, "Status": "Pass"}
# ]

# # headers list- we can not chnge the colmn
# header=["Roll_No","Name", "Score", "Grade", "Attendance_Pct","Status"]

# with open(output_path, "w", newline="") as file:
#     writer=csv.DictWriter(file, fieldnames=header)
#     writer.writeheader()
#     writer.writerows(students)
# print("File is written")



# Append in csv files

new_student=[[345, "Naman2",90, "A"]]

with open(output_path, "a", newline="") as file:
    writer=csv.writer(file)
    writer.writerows(new_student)

print("New student added")




