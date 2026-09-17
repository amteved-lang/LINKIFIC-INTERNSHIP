# 📊 Machine Learning Model Evaluation

## Project Overview

This project evaluates the Logistic Regression classification model created in the previous Machine Learning task.

The model classifies students into two performance categories based on their academic performance:

- High Performer
- Needs Improvement

The model was evaluated using Accuracy, Precision, Recall, F1 Score, and a Confusion Matrix.

## Objectives

- Evaluate a Machine Learning classification model
- Calculate Accuracy
- Calculate Precision
- Calculate Recall
- Calculate F1 Score
- Generate a Confusion Matrix
- Interpret model performance
- Identify a useful evaluation metric for the dataset

## Model Evaluated

### Logistic Regression

The Logistic Regression model from Task 11 was retrained using the same student dataset and feature selection.

### Feature

- Attendance

### Target

- Performance

## Evaluation Metrics

### Accuracy

Measures the overall percentage of correct predictions.

### Precision

Measures how many predicted High Performers were actually High Performers.

### Recall

Measures how many actual High Performers were correctly identified.

### F1 Score

Provides a balance between Precision and Recall.

## Confusion Matrix

A Confusion Matrix was generated to visualize the relationship between actual and predicted classifications.

It helps identify:

- Correct High Performer predictions
- Incorrect High Performer predictions
- Correct Needs Improvement predictions
- Incorrect Needs Improvement predictions

## Metric Selection

For this dataset, Recall is useful when the goal is to identify as many actual High Performers as possible.

F1 Score is also useful because it balances Precision and Recall.

The dataset is small, so evaluation results should be interpreted carefully because the testing set contains only a small number of samples.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- VS Code
- Git
- GitHub

## Project Files

- `model_evaluation.ipynb` - Model evaluation notebook
- `cleaned_students.csv` - Dataset used for evaluation
- `README.md` - Project documentation

## Reference

Scikit-learn Metrics Documentation:

https://scikit-learn.org/stable/modules/model_evaluation.html

## Conclusion

The Logistic Regression classification model was evaluated using multiple performance metrics. Accuracy, Precision, Recall, F1 Score, and a Confusion Matrix provided different perspectives on model performance and helped demonstrate the importance of selecting appropriate evaluation metrics for classification problems.