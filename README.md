# CareMetrics – Hospital Operations & Patient Flow Analytics

##  Project Overview

CareMetrics is a data analytics project focused on analyzing hospital operations and patient flow using synthetic hospital data.

The project analyzes patient waiting time, length of stay, bed occupancy, admission types, departments, age groups, and patient satisfaction. The analysis was performed using Python, MySQL, and Power BI.

---

## Project Objectives

- Analyze hospital patient waiting times.
- Identify waiting-time patterns across departments.
- Analyze bed occupancy and utilization.
- Compare different admission types.
- Analyze patient length of stay.
- Study patient satisfaction.
- Identify patients experiencing high waiting times.
- Build an interactive Power BI dashboard.
- Perform data analysis using Python and SQL.

---

##  Tools & Technologies

- **Python**
  - Pandas
  - Data cleaning
  - Exploratory Data Analysis
  - Statistical analysis
- **MySQL / phpMyAdmin**
  - Database management
  - SQL analysis
- **Power BI**
  - Interactive dashboard
  - KPI cards
  - Charts and slicers
- **Microsoft Word / PDF**
  - Project documentation

---

## Dataset

The project uses a **synthetic hospital operations dataset** containing 500 patient records.

The dataset includes information such as:

- Patient ID
- Age
- Gender
- Department
- Admission Type
- Admission Date
- Discharge Date
- Registration Wait Time
- Consultation Wait Time
- Diagnostic Wait Time
- Billing Wait Time
- Total Wait Time
- Length of Stay
- Bed Capacity
- Occupied Beds
- Occupancy Rate
- Satisfaction Score

The cleaned dataset contains **26 columns** after adding calculated and analytical fields.

---

## Data Cleaning & Validation

Python was used to clean and validate the dataset.

The cleaning process included:

- Checking missing values
- Checking duplicate records
- Validating dates
- Calculating length of stay
- Validating total waiting time
- Calculating occupancy rate
- Creating age groups
- Creating admission month fields
- Comparing calculated and original values

### Validation Results

- Records: **500**
- Missing values: **0**
- Duplicate rows: **0**
- Invalid dates: **0**
- Total wait mismatches: **0**
- LOS mismatches: **0**
- Occupied beds greater than capacity: **0**

---

## Key Results

| KPI | Result |
|---|---:|
| Total Patients | 500 |
| Average Waiting Time | 174.07 minutes |
| Average Length of Stay | 7.99 days |
| Average Occupancy | 57.15% |
| Average Satisfaction | 3.01 / 5 |
| High-Wait Patients (>240 min) | 32 |
| High-Wait Percentage | 6.4% |

---

##  Waiting-Time Analysis

Average waiting time was approximately **174.07 minutes**.

The average waiting-time components were:

| Waiting Stage | Average Time |
|---|---:|
| Registration | 25.11 min |
| Consultation | 49.94 min |
| Diagnostic | 65.07 min |
| Billing | 33.95 min |
| **Total** | **174.07 min** |

Diagnostic waiting time was the largest component of the overall average waiting time.

---

##  Department Analysis

The project analyzed patient volume, waiting time, occupancy, and satisfaction across eight departments:

- Cardiology
- Dermatology
- ENT
- General Medicine
- Gynecology
- Neurology
- Orthopedics
- Pediatrics

Some department-level observations:

- Gynecology had an average waiting time of **183.45 minutes**.
- Pediatrics had an average waiting time of **168.32 minutes**.
- Orthopedics recorded the highest patient volume with **75 patients**.
- Gynecology had an average occupancy rate of **61.90%**.
- ENT had an average satisfaction score of **2.72**.

---

##  Admission Type Analysis

The dataset contains three admission types:

- Emergency
- OPD
- Planned

The analysis compares these admission types based on:

- Patient volume
- Average waiting time
- Length of stay
- Satisfaction score

---

## Age Group Analysis

Patients were grouped into:

- 0–18
- 19–35
- 36–50
- 51–65
- 66+

The analysis compares waiting time, length of stay, and satisfaction across these age groups.

---

## 🛏️ Bed Occupancy Analysis

The overall average bed occupancy rate was:

**57.15%**

Department-level occupancy was also analyzed to understand differences in bed utilization.

---

##  Patient Satisfaction

The satisfaction score ranges from **1 to 5**.

Overall average satisfaction:

**3.01 / 5**

The project also examined satisfaction across:

- Departments
- Admission types
- Age groups
- Waiting-time categories

---

##  Correlation Analysis

Correlation analysis was performed to examine relationships between operational variables and satisfaction.

Observed correlations included:

| Variables | Correlation |
|---|---:|
| Waiting Time vs Satisfaction | -0.047 |
| Length of Stay vs Satisfaction | -0.065 |
| Occupancy vs Satisfaction | -0.025 |
| Waiting Time vs Length of Stay | 0.005 |

These values are close to zero, indicating weak linear relationships in this synthetic dataset.

Correlation should not be interpreted as proof of causation.

---

## Power BI Dashboard

An interactive Power BI dashboard was created to provide an overview of hospital operations.

### Dashboard Components

- Total Patients KPI
- Average Waiting Time KPI
- Average Length of Stay KPI
- Average Occupancy KPI
- Average Satisfaction KPI
- Patient Count by Department
- Average Waiting Time by Department
- Waiting-Time Components
- Monthly Patient Volume
- Occupancy by Department
- Department slicer
- Admission Type slicer
- Gender slicer

---

##  Project Structure

```text
CareMetrics-Hospital-Operations-Analytics/
│
├── Datasets/
│   ├── hospital_operations_data.csv
│   └── hospital_operations_cleaned.csv
│
├── MySQL/
│   └── hospital_operations_import.sql
│
├── PowerBi/
│   └── Hospital_Operations_Analytics.pbix
│
├── Project Report/
│   └── Project_Report.docx
│
├── Python files/
│   ├── clean.py
│   ├── additional_column.py
│   ├── eda_analysis.py
│   ├── department_analysis.py
│   ├── admission_type_analysis.py
│   ├── age_group_analysis.py
│   ├── correlation.py
│   ├── correlation_analysis.py
│   ├── create_mysql_import.py
│   └── hospital.py
│
├── SQL Screenshot/
│   └── SQL analysis screenshots
│
└── README.md

 Dataset Note

This project uses synthetic data created for educational and analytics purposes. It does not contain real patient medical records.
