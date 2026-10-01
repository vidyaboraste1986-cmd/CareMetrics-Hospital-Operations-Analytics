import pandas as pd

# ==========================================
# 1. LOAD THE DATASET
# ==========================================

df = pd.read_csv("hospital_operations_data.csv")

print("Dataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# ==========================================
# 2. CONVERT DATE COLUMNS
# ==========================================

df["Admission_Date"] = pd.to_datetime(
    df["Admission_Date"],
    errors="coerce"
)

df["Discharge_Date"] = pd.to_datetime(
    df["Discharge_Date"],
    errors="coerce"
)


# ==========================================
# 3. CREATE LENGTH OF STAY
# ==========================================

df["Calculated_LOS"] = (
    df["Discharge_Date"] - df["Admission_Date"]
).dt.days

df["LOS_Difference"] = (
    df["Length_of_Stay_Days"] - df["Calculated_LOS"]
)


# ==========================================
# 4. CREATE OCCUPANCY RATE
# ==========================================

df["Calculated_Occupancy_Rate"] = (
    df["Occupied_Beds"] /
    df["Bed_Capacity"] * 100
)


# ==========================================
# 5. CREATE MONTH INFORMATION
# ==========================================

df["Admission_Month"] = (
    df["Admission_Date"].dt.month
)

df["Admission_Month_Name"] = (
    df["Admission_Date"].dt.strftime("%B")
)


# ==========================================
# 6. CREATE DAY OF WEEK
# ==========================================

df["Admission_Day"] = (
    df["Admission_Date"].dt.day_name()
)


# ==========================================
# 7. CREATE AGE GROUP
# ==========================================

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 18, 35, 50, 65, 100],
    labels=[
        "0-18",
        "19-35",
        "36-50",
        "51-65",
        "66+"
    ]
)


# ==========================================
# 8. CHECK TOTAL WAIT TIME
# ==========================================

df["Calculated_Total_Wait"] = (
    df["Registration_Wait_Min"]
    + df["Consultation_Wait_Min"]
    + df["Diagnostic_Wait_Min"]
    + df["Billing_Wait_Min"]
)

df["Wait_Difference"] = (
    df["Total_Wait_Min"]
    - df["Calculated_Total_Wait"]
)


# ==========================================
# 9. VALIDATION RESULTS
# ==========================================

print("\n========== VALIDATION RESULTS ==========")

print(
    "Missing values:",
    df.isnull().sum().sum()
)

print(
    "Duplicate rows:",
    df.duplicated().sum()
)

print(
    "Total Wait mismatches:",
    (df["Wait_Difference"] != 0).sum()
)

print(
    "LOS mismatches:",
    (df["LOS_Difference"] != 0).sum()
)

print(
    "Invalid dates:",
    (df["Discharge_Date"] < df["Admission_Date"]).sum()
)

print(
    "Occupied beds > capacity:",
    (df["Occupied_Beds"] > df["Bed_Capacity"]).sum()
)


# ==========================================
# 10. SAVE CLEANED DATASET
# ==========================================

df.to_csv(
    "hospital_operations_cleaned.csv",
    index=False
)

print("\n========================================")
print("CLEANED DATASET CREATED SUCCESSFULLY!")
print("File: hospital_operations_cleaned.csv")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("========================================")