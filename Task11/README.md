# 🤖 Classification Using Machine Learning

## Project Overview

This project demonstrates the basics of classification problems using Python and Scikit-learn.

A cleaned student performance dataset was used to train and compare two classification models: Logistic Regression and Decision Tree.

The models classify students into two performance categories based on their average marks.

## Learning Objectives

- Understand classification problems
- Learn the classification workflow
- Train a Logistic Regression model
- Train a Decision Tree model
- Generate predictions
- Compare models using accuracy

## Classification Problem

Students were divided into two categories:

- **High Performer** - Average Marks >= 80
- **Needs Improvement** - Average Marks < 80

## Feature

The model uses:

- Attendance

## Target

The target variable is:

- Performance

## Models Used

### Logistic Regression

Logistic Regression was trained to classify students into the two performance categories.

### Decision Tree

A Decision Tree classifier was trained to classify students based on attendance.

## Machine Learning Workflow

1. Loaded the cleaned student dataset
2. Calculated average marks
3. Created performance categories
4. Selected feature and target variables
5. Split the dataset into training and testing sets
6. Trained Logistic Regression
7. Trained Decision Tree
8. Generated predictions
9. Compared model accuracy

## Accuracy Comparison

The accuracy of both models was calculated using Scikit-learn's `accuracy_score`.

The actual accuracy values generated during execution were recorded in the notebook.

## Visualization

A bar chart was created to compare the accuracy of Logistic Regression and Decision Tree models.

## Observations

- Both models were trained using the same dataset.
- Both models were evaluated using the same test data.
- Accuracy was used as the comparison metric.
- The models predict whether a student is a High Performer or Needs Improvement.
- The dataset is relatively small, so accuracy should be interpreted in the context of the limited number of test samples.

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

- `classification_models.ipynb` - Classification notebook
- `cleaned_students.csv` - Cleaned student dataset
- `README.md` - Project documentation

## Reference

Scikit-learn Classification Documentation:

https://scikit-learn.org/stable/supervised_learning.html

## Conclusion

This project provided practical experience with classification algorithms and the Machine Learning workflow. Logistic Regression and Decision Tree models were trained to classify student performance, and their accuracy was compared using the same testing dataset.