# Suicide Rate Analysis Project

## Overview
This project analyzes and visualizes suicide rate data in the United States across different demographics, ages, and time periods. The data is sourced from a comprehensive dataset that includes information on suicide rates by sex, race, Hispanic origin, and age.

## Dataset
The dataset used is `Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv` which contains the following key fields:
- INDICATOR: The measurement being recorded (suicide rates)
- UNIT: Measurement unit (Deaths per 100,000 resident population)
- STUB_NAME: Demographic group category
- AGE: Age group category
- YEAR: Year of data collection
- ESTIMATE: Death rate estimate
- Additional metadata and classification fields

## Analysis Performed
The code performs the following exploratory data analysis and visualizations:

1. **Overall Suicide Rate Trend**: Time-series visualization of suicide rates for all ages
2. **Statistical Distribution**: Histogram showing the distribution of suicide rates
3. **Demographic Comparison**: Box plots comparing suicide rates across different demographic groups
4. **Time Trends by Demographics**: Line plots showing how rates change over time for different groups
5. **Variable Correlation**: Heatmap displaying correlations between numerical variables
6. **Top Demographics**: Bar chart of demographics with highest suicide rates in the most recent year
7. **Yearly Averages**: Plot showing the average suicide rate trend over time
8. **Multivariate Relationships**: Pairplot showing relationships between key variables

## Requirements
To run this analysis, you need:
- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- NumPy

You can install these dependencies using pip:
```
pip install pandas matplotlib seaborn numpy
```

## Usage
1. Ensure the dataset file is in the same directory as the script
2. Run the script using Python:
   ```
   python main.py
   ```
3. The script will generate and display various visualizations for analysis

## Visualizations Explained

### 1. Suicide Rate Trend (All Ages)
This plot shows how the overall suicide rate has changed over time for the entire population, providing insight into general trends and potential historical influences.

### 2. Distribution of Suicide Rates
The histogram displays the statistical distribution of suicide rates across all records, helping identify common rate ranges and outliers.

### 3. Suicide Rates by Demographic Group
Box plots compare suicide rates across different demographic groups (categories in STUB_NAME), highlighting which populations may be at higher risk.

### 4. Suicide Rate Trends by Demographic Group
This visualization tracks how suicide rates have changed over time across different demographic groups, allowing identification of populations with increasing or decreasing trends.

### 5. Correlation Matrix
The heatmap reveals correlations between numerical variables in the dataset, helping identify potential relationships between factors.

### 6. Top Demographics by Suicide Rate
This bar chart identifies which demographic groups had the highest suicide rates in the most recent year available in the dataset.

### 7. Yearly Average Suicide Rate
This plot shows the annual average suicide rate trend, smoothing out demographic differences to focus on overall temporal patterns.

### 8. Relationships Between Key Variables
The pairplot displays relationships between year, age, and suicide rates, helping identify potential patterns and interactions between these variables.

## Future Work
Potential extensions to this analysis could include:
- Statistical testing to determine significant differences between groups
- Predictive modeling to forecast future trends
- Geographic analysis if regional data becomes available
- Correlation with external socioeconomic or healthcare factors
