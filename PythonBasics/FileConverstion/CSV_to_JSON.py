# --------------------------------------------------------
# CSV TO NESTED JSON
# --------------------------------------------------------

# Import required modules

import csv
import json


# --------------------------------------------------------
# STEP 1 : Read CSV File
# --------------------------------------------------------

# Open CSV file

with open("Output_CSV/employees.csv", "r", encoding="utf-8") as csv_file:

    # DictReader reads each row as a dictionary
    reader = csv.DictReader(csv_file)

    # Empty list to store all employees
    employees = []

    # ----------------------------------------------------
    # STEP 2 : Read Each Row
    # ----------------------------------------------------

    for row in reader:

        # ----------------------------
        # Convert Skills back to List
        # ----------------------------

        skills = row["Skills"].split(", ")

        # ----------------------------
        # Convert Projects back to List
        # ----------------------------

        projects = []

        project_strings = row["Projects"].split(" | ")

        for project in project_strings:

            # Example:
            # Payroll System (Completed, 12 Months)

            name, details = project.split(" (")

            details = details.replace(")", "")

            status, duration = details.split(", ")

            duration = int(duration.replace(" Months", ""))

            projects.append(
                {
                    "project_name": name,
                    "status": status,
                    "duration_months": duration
                }
            )

        # ----------------------------
        # Create Nested Dictionary
        # ----------------------------

        employee = {

            "employee_id": row["Employee ID"],

            "personal_info": {

                "first_name": row["First Name"],
                "last_name": row["Last Name"],
                "gender": row["Gender"],
                "age": int(row["Age"]),
                "email": row["Email"],
                "phone": row["Phone"]

            },

            "job_details": {

                "department": row["Department"],
                "designation": row["Designation"],
                "salary": int(row["Salary"]),
                "experience": float(row["Experience"]),
                "joining_date": row["Joining Date"]

            },

            "address": {

                "city": row["City"],
                "state": row["State"],
                "country": row["Country"],
                "zipcode": int(row["Zipcode"])

            },

            "manager": {

                "manager_id": row["Manager ID"],
                "manager_name": row["Manager Name"]

            },

            "skills": skills,

            "projects": projects,

            "performance": {

                "rating": float(row["Rating"]),
                "last_promotion_year": int(row["Last Promotion Year"]),
                "bonus": int(row["Bonus"])

            }

        }

        # Add employee to list
        employees.append(employee)


# --------------------------------------------------------
# STEP 3 : Save JSON File
# --------------------------------------------------------

with open("Output_Json/employees_from_csv.json", "w", encoding="utf-8") as json_file:

    json.dump(
        employees,
        json_file,
        indent=4
    )

print("Nested JSON created successfully!")