# 🧹 Data Cleaning and Preprocessing

## Project Overview

This project demonstrates basic data cleaning and preprocessing techniques using Python and Pandas.

The project uses a student performance dataset containing academic and attendance information.

## Objectives

- Load a dataset using Pandas
- Identify missing values
- Handle missing values
- Remove duplicate records
- Rename columns
- Convert incorrect data types
- Save the cleaned dataset

## Data Cleaning Techniques

### Missing Values

Missing numerical values were identified and handled using median values.

### Duplicate Records

Duplicate student records were identified and removed using Pandas.

### Column Renaming

Column names were standardized for easier analysis and better readability.

### Data Type Conversion

Numerical columns were converted to appropriate numeric data types.

### Text Cleaning

Text fields such as names, gender, and city were standardized.

## Dataset Before Cleaning

The original dataset contained missing values and duplicate records.

## Dataset After Cleaning

The cleaned dataset contains no missing values or duplicate records and uses standardized column names and appropriate data types.

## Technologies Used

- Python
- Pandas
- Jupyter Notebook
- VS Code
- Git
- GitHub

## Project Files

- `data_cleaning.ipynb` - Data cleaning notebook
- `dirty_students.csv` - Original dataset
- `cleaned_students.csv` - Cleaned dataset

## Reference

Pandas Missing Data Documentation:
https://pandas.pydata.org/docs/user_guide/missing_data.html