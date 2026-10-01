import pandas as pd

# Load the verified CSV
df = pd.read_csv("hospital_operations_cleaned.csv")

# Remove accidental header rows, if any
df = df[df["Patient_ID"].astype(str) != "Patient_ID"].copy()

# Convert numeric columns
numeric_columns = [
    "Patient_ID",
    "Age",
    "Registration_Wait_Min",
    "Consultation_Wait_Min",
    "Diagnostic_Wait_Min",
    "Billing_Wait_Min",
    "Total_Wait_Min",
    "Length_of_Stay_Days",
    "Bed_Capacity",
    "Occupied_Beds",
    "Occupancy_Rate",
    "Satisfaction_Score",
    "Calculated_LOS",
    "LOS_Difference",
    "Calculated_Occupancy_Rate",
    "Admission_Month",
    "Calculated_Total_Wait",
    "Wait_Difference"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")


def sql_value(value):
    """Convert a Python/pandas value into a MySQL value."""
    
    if pd.isna(value):
        return "NULL"

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return str(value)

    value = str(value)
    value = value.replace("\\", "\\\\")
    value = value.replace("'", "''")

    return "'" + value + "'"


columns = [
    "Patient_ID",
    "Age",
    "Gender",
    "Department",
    "Admission_Type",
    "Admission_Date",
    "Discharge_Date",
    "Registration_Wait_Min",
    "Consultation_Wait_Min",
    "Diagnostic_Wait_Min",
    "Billing_Wait_Min",
    "Total_Wait_Min",
    "Length_of_Stay_Days",
    "Bed_Capacity",
    "Occupied_Beds",
    "Occupancy_Rate",
    "Satisfaction_Score",
    "Calculated_LOS",
    "LOS_Difference",
    "Calculated_Occupancy_Rate",
    "Admission_Month",
    "Admission_Month_Name",
    "Admission_Day",
    "Age_Group",
    "Calculated_Total_Wait",
    "Wait_Difference"
]

column_sql = ", ".join(f"`{col}`" for col in columns)

with open("hospital_operations_import.sql", "w", encoding="utf-8") as f:

    f.write("USE hospital_analytics;\n\n")

    f.write("TRUNCATE TABLE hospital_operations;\n\n")

    for start in range(0, len(df), 100):

        batch = df.iloc[start:start + 100]

        f.write(
            f"INSERT INTO hospital_operations ({column_sql}) VALUES\n"
        )

        rows = []

        for _, row in batch.iterrows():

            values = [
                sql_value(row[col])
                for col in columns
            ]

            rows.append("(" + ", ".join(values) + ")")

        f.write(",\n".join(rows))
        f.write(";\n\n")

print("SQL IMPORT FILE CREATED SUCCESSFULLY")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("File: hospital_operations_import.sql")