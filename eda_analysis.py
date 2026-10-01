import pandas as pd

# ==========================================
# 1. LOAD CLEANED DATA
# ==========================================

df = pd.read_csv("hospital_operations_cleaned.csv")

print("Dataset loaded!")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# ==========================================
# 2. OVERALL KPIs
# ==========================================

print("\n========== OVERALL KPIs ==========")

print("Total Patients:", df["Patient_ID"].nunique())

print(
    "Average Total Wait:",
    round(df["Total_Wait_Min"].mean(), 2),
    "minutes"
)

print(
    "Median Total Wait:",
    df["Total_Wait_Min"].median(),
    "minutes"
)

print(
    "Average Length of Stay:",
    round(df["Length_of_Stay_Days"].mean(), 2),
    "days"
)

print(
    "Average Occupancy Rate:",
    round(df["Occupancy_Rate"].mean(), 2),
    "%"
)

print(
    "Average Satisfaction:",
    round(df["Satisfaction_Score"].mean(), 2),
    "/ 5"
)


# ==========================================
# 3. DEPARTMENT ANALYSIS
# ==========================================

print("\n========== DEPARTMENT ANALYSIS ==========")

department_analysis = df.groupby("Department").agg(
    Patients=("Patient_ID", "count"),
    Avg_Wait=("Total_Wait_Min", "mean"),
    Avg_LOS=("Length_of_Stay_Days", "mean"),
    Avg_Occupancy=("Occupancy_Rate", "mean"),
    Avg_Satisfaction=("Satisfaction_Score", "mean")
).round(2)

print(department_analysis)


# ==========================================
# 4. WAIT-TIME BREAKDOWN
# ==========================================

print("\n========== WAIT-TIME BREAKDOWN ==========")

wait_analysis = df[
    [
        "Registration_Wait_Min",
        "Consultation_Wait_Min",
        "Diagnostic_Wait_Min",
        "Billing_Wait_Min",
        "Total_Wait_Min"
    ]
].mean().round(2)

print(wait_analysis)


# ==========================================
# 5. ADMISSION TYPE ANALYSIS
# ==========================================

print("\n========== ADMISSION TYPE ==========")

admission_analysis = df.groupby("Admission_Type").agg(
    Patients=("Patient_ID", "count"),
    Avg_Wait=("Total_Wait_Min", "mean"),
    Avg_LOS=("Length_of_Stay_Days", "mean"),
    Avg_Satisfaction=("Satisfaction_Score", "mean")
).round(2)

print(admission_analysis)


# ==========================================
# 6. AGE GROUP ANALYSIS
# ==========================================

print("\n========== AGE GROUP ANALYSIS ==========")

age_analysis = df.groupby("Age_Group", observed=True).agg(
    Patients=("Patient_ID", "count"),
    Avg_Wait=("Total_Wait_Min", "mean"),
    Avg_LOS=("Length_of_Stay_Days", "mean"),
    Avg_Satisfaction=("Satisfaction_Score", "mean")
).round(2)

print(age_analysis)


# ==========================================
# 7. MONTHLY ANALYSIS
# ==========================================

print("\n========== MONTHLY ANALYSIS ==========")

monthly_analysis = df.groupby(
    "Admission_Month_Name"
).agg(
    Patients=("Patient_ID", "count"),
    Avg_Wait=("Total_Wait_Min", "mean"),
    Avg_Occupancy=("Occupancy_Rate", "mean"),
    Avg_Satisfaction=("Satisfaction_Score", "mean")
).round(2)

print(monthly_analysis)


# ==========================================
# 8. BED CAPACITY ANALYSIS
# ==========================================

print("\n========== BED CAPACITY ==========")

print(
    "Average Bed Capacity:",
    round(df["Bed_Capacity"].mean(), 2)
)

print(
    "Average Occupied Beds:",
    round(df["Occupied_Beds"].mean(), 2)
)

print(
    "Average Occupancy:",
    round(df["Occupancy_Rate"].mean(), 2),
    "%"
)


# ==========================================
# 9. HIGH WAIT-TIME PATIENTS
# ==========================================

print("\n========== HIGH WAIT-TIME ANALYSIS ==========")

high_wait = df[df["Total_Wait_Min"] > 240]

print(
    "Patients waiting more than 240 minutes:",
    len(high_wait)
)

print(
    "Percentage:",
    round(len(high_wait) / len(df) * 100, 2),
    "%"
)


# ==========================================
# 10. SATISFACTION ANALYSIS
# ==========================================

print("\n========== SATISFACTION ==========")

satisfaction = df.groupby(
    "Satisfaction_Score"
).size()

print(satisfaction)


# ==========================================
# 11. SAVE SUMMARY FILES
# ==========================================

department_analysis.to_csv(
    "department_analysis.csv"
)

admission_analysis.to_csv(
    "admission_type_analysis.csv"
)

age_analysis.to_csv(
    "age_group_analysis.csv"
)

monthly_analysis.to_csv(
    "monthly_analysis.csv"
)

print("\n========================================")
print("EDA ANALYSIS COMPLETED!")
print("Summary files created successfully.")
print("========================================")