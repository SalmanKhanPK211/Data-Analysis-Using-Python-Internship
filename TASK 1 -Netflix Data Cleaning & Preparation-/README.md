#  Netflix Data Cleaning and Preparation

##  Overview

This project is the first task of my **Data Analysis Using Python Internship** at **Auspify Technology**.

The objective of this project is to clean and prepare the Netflix dataset for further analysis by identifying data quality issues, verifying the dataset structure, and exporting a cleaned version of the data.

---

##  Objective

The primary objectives of this project are:

- Import the Netflix dataset using Pandas.
- Explore the dataset structure.
- Check for missing values.
- Check for duplicate records.
- Standardize text columns.
- Export the cleaned dataset for future analysis.

---

##   Dataset Information

- **Dataset:** Netflix Titles Dataset
- **Total Records:** 8,790
- **Total Features:** 10

### Dataset Columns

- Show ID
- Type
- Title
- Director
- Country
- Date Added
- Release Year
- Rating
- Duration
- Listed In

---

##  Technologies Used

- Python
- Pandas
- Jupyter Notebook (VS Code)

---

##  Project Workflow

### Step 1
Import the required Python library (Pandas).

### Step 2
Load the dataset into a Pandas DataFrame.

### Step 3
Explore the dataset by examining:
- Dataset dimensions
- Column names
- Data types
- General information

### Step 4
Check for missing values.

### Step 5
Check for duplicate records.

### Step 6
Standardize text columns:
- Country
- Rating
- Type

### Step 7
Export the cleaned dataset as a new CSV file.

---

##  Data Cleaning Summary

| Check | Result |
|--------|--------|
| Missing Values |  No missing values found |
| Duplicate Records |  No duplicate records found |
| Data Types |  Correctly assigned |
| Text Standardization |  Country, Rating and Type standardized |

---

##  Project Structure

```
AUSPIFY Internship (Data Analysis using Python)
│
└──  TASK 1 DATA CLEANING
    │
    ├── Dataset.csv
    ├── cleaned_netflix_dataset.csv
    ├── task1.py
    ├── task1.ipynb
    └── README.md
```

---

##  Output

The cleaned dataset was exported as:

```
Netflix_Cleaned.csv
```

This file can be used for further data analysis and visualization tasks.

---

##  Learning Outcomes

Through this project, I learned how to:

- Import datasets using Pandas.
- Explore dataset structure.
- Inspect data types.
- Identify missing values.
- Detect duplicate records.
- Standardize textual data.
- Export cleaned datasets.
- Organize a data analysis project using Jupyter Notebook.

---

##  Author

**Salman Khan**

Data Analysis Using Python Intern  
Auspify Technology

---