import pandas as pd

# Load dataset
df = pd.read_csv("hospital_operations_data.csv")

# ---------------------------------------
# 1. Convert date columns to datetime
# ---------------------------------------

df["Admission_Date"] = pd.to_datetime(
    df["Admission_Date"],
    errors="coerce"
)

df["Discharge_Date"] = pd.to_datetime(
    df["Discharge_Date"],
    errors="coerce"
)

# ---------------------------------------
# 2. Check missing values after conversion
# ---------------------------------------

print("Missing values after date conversion:")
print(df.isnull().sum())

# ---------------------------------------
# 3. Check duplicate Patient IDs
# ---------------------------------------

print("\nDuplicate Patient IDs:")
print(df["Patient_ID"].duplicated().sum())

# ---------------------------------------
# 4. Check age values
# ---------------------------------------

print("\nAge validation:")
print("Minimum age:", df["Age"].min())
print("Maximum age:", df["Age"].max())

# ---------------------------------------
# 5. Check wait-time values
# ---------------------------------------

wait_columns = [
    "Registration_Wait_Min",
    "Consultation_Wait_Min",
    "Diagnostic_Wait_Min",
    "Billing_Wait_Min",
    "Total_Wait_Min"
]

print("\nNegative wait times:")

for col in wait_columns:
    print(col, "=", (df[col] < 0).sum())

# ---------------------------------------
# 6. Check Length of Stay
# ---------------------------------------

print("\nLength of Stay:")
print("Minimum:", df["Length_of_Stay_Days"].min())
print("Maximum:", df["Length_of_Stay_Days"].max())

# ---------------------------------------
# 7. Check bed capacity
# ---------------------------------------

print("\nBed capacity validation:")

print(
    "Occupied beds greater than capacity:",
    (df["Occupied_Beds"] > df["Bed_Capacity"]).sum()
)

print(
    "Negative occupied beds:",
    (df["Occupied_Beds"] < 0).sum()
)

# ---------------------------------------
# 8. Check occupancy rate
# ---------------------------------------

calculated_occupancy = (
    df["Occupied_Beds"] / df["Bed_Capacity"] * 100
)

occupancy_difference = (
    calculated_occupancy - df["Occupancy_Rate"]
).abs()

print(
    "\nOccupancy rate differences greater than 0.1:",
    (occupancy_difference > 0.1).sum()
)

# ---------------------------------------
# 9. Check satisfaction score
# ---------------------------------------

print("\nSatisfaction score:")
print("Minimum:", df["Satisfaction_Score"].min())
print("Maximum:", df["Satisfaction_Score"].max())

# ---------------------------------------
# 10. Check admission types
# ---------------------------------------

print("\nAdmission types:")
print(df["Admission_Type"].value_counts())

# ---------------------------------------
# 11. Check departments
# ---------------------------------------

print("\nDepartments:")
print(df["Department"].value_counts())

# ---------------------------------------
# 12. Check genders
# ---------------------------------------

print("\nGender:")
print(df["Gender"].value_counts())

print("\nDATA VALIDATION COMPLETE")