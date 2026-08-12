# Netflix Content Type Analysis Dashboard

## Overview

This project is Task 2 of my Data Analysis Using Python Internship at Auspify Technology.

The objective of this task is to analyze the distribution of Movies and TV Shows available in the Netflix dataset and compare their proportions using numerical analysis and visualizations.

The cleaned dataset generated during Task 1: Data Cleaning was used as the input for this analysis.

---

## Objectives

The main objectives of this task are:

- Analyze the distribution of Movies and TV Shows.
- Calculate the total number of Movies and TV Shows.
- Calculate the proportion of each content type.
- Create visualizations to compare content distribution.
- Identify key insights from the analysis.
- Present the findings in a clear and concise summary.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- VS Code

---

## Dataset Information

The analysis was performed using the cleaned Netflix dataset produced during Task 1.

- Total Records: 8,790
- Total Columns: 10

The primary column used for this analysis was:

```text
type
```

This column contains two content categories:

- Movie
- TV Show

---

## Analysis Workflow

### 1. Load the Cleaned Dataset

The cleaned Netflix dataset was loaded using Pandas.

### 2. Identify Content Types

The `type` column was examined to identify the available content categories.

### 3. Calculate Content Counts

The `value_counts()` function was used to determine the number of Movies and TV Shows.

### 4. Calculate Content Proportions

The proportion of each content type was calculated as a percentage of the total number of titles.

### 5. Create Visualizations

Two visualizations were created:

- Bar Chart — compares the actual number of Movies and TV Shows.
- Pie Chart — illustrates the proportion of each content type.

### 6. Extract Key Findings

The results were interpreted to identify the dominant content type and its proportion within the dataset.

---

## Results

| Content Type | Number of Titles | Percentage |
|--------------|-----------------:|-----------:|
| Movie | 6,126 | 69.69% |
| TV Show | 2,664 | 30.31% |
| **Total** | **8,790** | **100%** |

---

## Key Findings

- The dataset contains 8,790 Netflix titles.
- Movies are the dominant content type, with 6,126 titles.
- Movies represent approximately 69.69% of the dataset.
- TV Shows account for 2,664 titles, representing approximately 30.31%.
- Movies make up more than twice the number of TV Shows in the analyzed dataset.
- The visualizations clearly demonstrate the difference in both content volume and proportion.

---

## Visualizations

### Content Distribution

The bar chart compares the actual number of Movies and TV Shows in the dataset.

### Content Proportion

The pie chart illustrates the percentage share of Movies and TV Shows within the dataset.

---

## Project Structure

```text
TASK 2 CONTENT TYPE ANALYSIS
│
├── cleaned_netflix_dataset.csv
├── task2.py
├── task2.ipynb
└── README.md
```

### File Description

| File | Description |
|------|-------------|
| `cleaned_netflix_dataset.csv` | Cleaned Netflix dataset used for analysis |
| `task2.py` | Python script containing the analysis code |
| `task2.ipynb` | Jupyter Notebook containing code, analysis, visualizations, and findings |
| `README.md` | Documentation for Task 2 |

---

## Learning Outcomes

Through this task, I strengthened my understanding of:

- Loading datasets using Pandas
- Working with categorical data
- Using `value_counts()` for frequency analysis
- Calculating proportions and percentages
- Performing vectorized calculations in Pandas
- Creating bar charts using Matplotlib
- Creating pie charts using Matplotlib
- Interpreting visualizations
- Extracting data-driven insights
- Documenting an analysis project professionally

---

## Author

**Salman Khan**

Data Analysis Using Python Intern  
Auspify Technology

University of Swabi

---

## Internship Progress

- Task 1 — Data Cleaning — Completed
- Task 2 — Content Type Analysis Dashboard — Completed

More data analysis projects and tasks will be added as the internship progresses.

---

## Technologies

Python | Pandas | Matplotlib | Jupyter Notebook | VS Code