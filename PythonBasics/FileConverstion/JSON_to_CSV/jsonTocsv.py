# -----------------------------------------------------
# JSON TO CSV (Flatten Nested JSON)
# -----------------------------------------------------

# json module
# Used to read JSON files
import json

# csv module
# Used to create CSV files
import csv


# -----------------------------------------------------
# STEP 1 : Read the JSON File
# -----------------------------------------------------

# Open the JSON file in read mode ("r")
with open("PythonBasics\FileConverstion\JSON_to_CSV\Input_Json\employees_100_nested.json", "r", encoding="utf-8") as file:

    # json.load()
    # Converts JSON file into Python objects
    # Here it becomes a LIST of dictionaries
    employees = json.load(file)


# -----------------------------------------------------
# STEP 2 : Create CSV File
# -----------------------------------------------------

# Open CSV file in write mode
with open("PythonBasics\FileConverstion\JSON_to_CSV\Output_CSV\employees.csv", "w", newline="", encoding="utf-8") as csv_file:

    # Column names of CSV
    headers = [
        "Employee ID",
        "First Name",
        "Last Name",
        "Gender",
        "Age",
        "Email",
        "Phone",

        "Department",
        "Designation",
        "Salary",
        "Experience",
        "Joining Date",

        "City",
        "State",
        "Country",
        "Zipcode",

        "Manager ID",
        "Manager Name",

        "Skills",

        "Projects",

        "Rating",
        "Last Promotion Year",
        "Bonus"
    ]

    # Create CSV writer object
    writer = csv.writer(csv_file)

    # Write header row
    writer.writerow(headers)

    # -------------------------------------------------
    # STEP 3 : Read every employee
    # -------------------------------------------------

    for employee in employees:

        # ---------------------------
        # Convert Skills List to String
        # ---------------------------

        # Example:
        # ["Python","SQL","Azure"]
        #
        # becomes
        #
        # Python, SQL, Azure

        skills = ", ".join(employee["skills"])


        # ---------------------------
        # Convert Project List to String
        # ---------------------------

        # We will create one long string

        project_list = []

        for project in employee["projects"]:

            project_info = (
                project["project_name"]
                + " ("
                + project["status"]
                + ", "
                + str(project["duration_months"])
                + " Months)"
            )

            project_list.append(project_info)

        projects = " | ".join(project_list)


        # ---------------------------
        # Write One Employee
        # ---------------------------

        writer.writerow([

            employee["employee_id"],

            employee["personal_info"]["first_name"],
            employee["personal_info"]["last_name"],
            employee["personal_info"]["gender"],
            employee["personal_info"]["age"],
            employee["personal_info"]["email"],
            employee["personal_info"]["phone"],

            employee["job_details"]["department"],
            employee["job_details"]["designation"],
            employee["job_details"]["salary"],
            employee["job_details"]["experience"],
            employee["job_details"]["joining_date"],

            employee["address"]["city"],
            employee["address"]["state"],
            employee["address"]["country"],
            employee["address"]["zipcode"],

            employee["manager"]["manager_id"],
            employee["manager"]["manager_name"],

            skills,

            projects,

            employee["performance"]["rating"],
            employee["performance"]["last_promotion_year"],
            employee["performance"]["bonus"]

        ])

print("CSV file created successfully!")