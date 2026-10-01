import pandas as pd

# Load cleaned dataset
df = pd.read_csv("hospital_operations_cleaned.csv")

print("Dataset loaded!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# ==========================================
# CORRELATION ANALYSIS
# ==========================================

print("\n========== CORRELATION MATRIX ==========")

correlation = df[
    [
        "Total_Wait_Min",
        "Length_of_Stay_Days",
        "Occupancy_Rate",
        "Satisfaction_Score"
    ]
].corr()

print(correlation.round(3))

# ==========================================
# WAIT TIME vs SATISFACTION
# ==========================================

wait_satisfaction_corr = df[
    "Total_Wait_Min"
].corr(df["Satisfaction_Score"])

print("\n========== WAIT TIME vs SATISFACTION ==========")
print(
    "Correlation between Wait Time and Satisfaction:",
    round(wait_satisfaction_corr, 3)
)

# ==========================================
# WAIT-TIME CATEGORIES
# ==========================================

def classify_wait(wait):
    if wait <= 120:
        return "<=120 min"
    elif wait <= 180:
        return "121-180 min"
    elif wait <= 240:
        return "181-240 min"
    else:
        return ">240 min"


df["Wait_Category"] = df["Total_Wait_Min"].apply(classify_wait)

wait_analysis = df.groupby("Wait_Category").agg(
    Patients=("Patient_ID", "count"),
    Avg_Satisfaction=("Satisfaction_Score", "mean"),
    Avg_LOS=("Length_of_Stay_Days", "mean")
).reindex(
    ["<=120 min", "121-180 min", "181-240 min", ">240 min"]
)

print("\n========== WAIT CATEGORY ANALYSIS ==========")
print(wait_analysis.round(2))

# Save results
wait_analysis.to_csv("wait_category_analysis.csv")

print("\n========================================")
print("CORRELATION ANALYSIS COMPLETED!")
print("File created: wait_category_analysis.csv")
print("========================================")