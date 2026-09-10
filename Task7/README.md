## 🌦️ Week 1 Mini Project - Weather Data Analysis

### Project Overview

This mini project analyzes historical weather data using Python and popular data analysis and visualization libraries.

The project focuses on temperature, precipitation, wind speed, and weather conditions to identify trends and patterns in the dataset.

### Objectives

- Load a real-world weather dataset
- Clean basic missing data
- Perform exploratory data analysis
- Analyze temperature and precipitation
- Create meaningful visualizations
- Extract key insights from the dataset

### Dataset

The project uses a historical weather dataset containing daily observations with the following features:

- Location
- Date
- Precipitation
- Maximum Temperature
- Minimum Temperature
- Wind Speed
- Weather Condition

### Data Cleaning

- Converted the date column into datetime format
- Checked for missing values
- Filled missing numerical values using median values
- Filled missing weather conditions using the mode
- Removed records with missing dates

### Visualizations

1. Temperature Trend Over Time
2. Weather Condition Distribution
3. Rainfall Distribution
4. Average Maximum Temperature by Month

### Key Insights

- Identified the highest recorded temperature
- Identified the lowest recorded temperature
- Found the highest single-day precipitation
- Identified the most common weather condition
- Identified the warmest month
- Identified the month with the highest rainfall
- Calculated the overall average maximum temperature
- Calculated the average wind speed

### Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

### Project Structure

Task7/
├── weather_data_analysis.ipynb
├── weather.csv
├── README.md
└── outputs/
    ├── temperature_trend.png
    ├── weather_distribution.png
    ├── rainfall_distribution.png
    └── monthly_temperature.png

### Dataset Source

Observable Sample Datasets:
https://github.com/observablehq/sample-datasets/blob/main/weather.csv