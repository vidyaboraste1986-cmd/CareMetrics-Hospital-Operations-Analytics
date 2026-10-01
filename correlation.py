import pandas as pd

# Load cleaned dataset
df = pd.read_csv("hospital_operations_cleaned.csv")

# ==========================================
# CORRELATION ANALYSIS
# ==========================================

correlation = df[
    [
        "Total_Wait_Min",
        "Length_of_Stay_Days",
        "Occupancy_Rate",
        "Satisfaction_Score"
    ]
].corr()

print("\n========== CORRELATION MATRIX ==========")

print(correlation.round(3))


# ==========================================
# WAIT TIME VS SATISFACTION
# ==========================================

wait_satisfaction = df[
    ["Total_Wait_Min", "Satisfaction_Score"]
].corr().iloc[0, 1]

print(
    "\nCorrelation between Wait Time and Satisfaction:",
    round(wait_satisfaction, 3)
)


# ==========================================
# WAIT-TIME GROUPS
# ==========================================

df["Wait_Category"] = pd.cut(
    df["Total_Wait_Min"],
    bins=[0, 120, 180, 240, float("inf")],
    labels=[
        "<=120 min",
        "121-180 min",
        "181-240 min",
        ">240 min"
    ]
)

wait_group = df.groupby(
    "Wait_Category",
    observed=True
).agg(
    Patients=("Patient_ID", "count"),
    Avg_Satisfaction=("Satisfaction_Score", "mean"),
    Avg_LOS=("Length_of_Stay_Days", "mean")
).round(2)

print("\n========== WAIT CATEGORY ANALYSIS ==========")

print(wait_group)


# ==========================================
# SAVE RESULTS
# ==========================================

wait_group.to_csv("wait_category_analysis.csv")

print("\nCorrelation analysis completed!")