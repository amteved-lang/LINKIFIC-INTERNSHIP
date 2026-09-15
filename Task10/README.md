# 🤖 Machine Learning & Linear Regression

## Project Overview

This project demonstrates the basic Machine Learning workflow using Python and Scikit-learn.

A cleaned student performance dataset was used to build a simple Linear Regression model. The model analyzes the relationship between student attendance and average marks and generates predictions.

## Learning Objectives

- Understand the basic Machine Learning workflow
- Prepare data for Machine Learning
- Split data into training and testing sets
- Train a Linear Regression model
- Make predictions using a trained model
- Evaluate the performance of the model

## Machine Learning Workflow

The following Machine Learning workflow was implemented:

1. Load the dataset
2. Select features and target variable
3. Split the dataset into training and testing data
4. Train the Linear Regression model
5. Make predictions
6. Evaluate the model
7. Test the model with new input data

## Dataset

The project uses a cleaned student performance dataset containing:

- Student Name
- Age
- Gender
- Python Marks
- Math Marks
- Science Marks
- Attendance
- City

An additional feature called `Average_Marks` was calculated from the three subject marks.

## Feature and Target

### Feature

`Attendance`

### Target

`Average_Marks`

The model attempts to predict a student's average marks based on their attendance percentage.

## Model Used

### Linear Regression

Linear Regression was selected to understand the relationship between attendance and student academic performance.

The dataset was divided into:

- 80% Training Data
- 20% Testing Data

## Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

These metrics help measure how accurately the model predicts average student marks.

## Prediction

The trained model was also used to predict the expected average marks for a new student with a given attendance percentage.

## Visualization

A scatter plot with the regression line was created to visualize the relationship between attendance and average marks.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter Notebook
- VS Code
- Git
- GitHub

## Project Files

- `ml_linear_regression.ipynb` - Machine Learning practice notebook
- `cleaned_students.csv` - Cleaned student dataset
- `README.md` - Project documentation

## Key Concepts Covered

- Machine Learning workflow
- Features and target variables
- Training and testing data
- Train-test split
- Linear Regression
- Model prediction
- Model evaluation
- Data visualization

## Reference

Scikit-learn Getting Started Guide:

https://scikit-learn.org/stable/getting_started.html

## Conclusion

This project provided practical experience with the fundamental Machine Learning workflow. A Linear Regression model was trained using student attendance data to predict average academic performance. The project demonstrates the complete process from dataset preparation to model training, prediction, evaluation, and visualization.