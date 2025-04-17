import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv')  


print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

# 1. Trend of suicide rates over time (for all ages)
plt.figure(figsize=(12, 6))
all_ages_total = df[(df['AGE'] == 'All ages') & (df['STUB_NAME'] == 'Total')]
plt.plot(all_ages_total['YEAR'], all_ages_total['ESTIMATE'], marker='o', linewidth=2)
plt.title('Suicide Rate Trend (All Ages, 1950-2018)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Deaths per 100,000 population', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Comparison of suicide rates by age groups (recent year)
recent_year = df['YEAR'].max()
recent_data = df[df['YEAR'] == recent_year]

# Filter for specific age groups, excluding 'All ages'
age_data = recent_data[(recent_data['AGE'] != 'All ages') & (recent_data['STUB_NAME'] == 'Total')]

plt.figure(figsize=(10, 6))
sns.barplot(x='AGE', y='ESTIMATE', data=age_data)
plt.title(f'Suicide Rates by Age Group ({recent_year})', fontsize=16)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Deaths per 100,000 population', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Heatmap showing suicide rates over time for different age groups
pivot_data = df[(df['AGE'] != 'All ages') & (df['STUB_NAME'] == 'Total')].pivot_table(
    values='ESTIMATE', index='YEAR', columns='AGE', aggfunc='mean')

plt.figure(figsize=(14, 8))
sns.heatmap(pivot_data, cmap='YlOrRd', annot=False, linewidths=.5)
plt.title('Suicide Rates Heatmap by Age Group Over Time', fontsize=16)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Year', fontsize=12)
plt.tight_layout()
plt.show()

# 4. Distribution of suicide rates
plt.figure(figsize=(10, 6))
sns.histplot(df['ESTIMATE'].dropna(), bins=30, kde=True)
plt.title('Distribution of Suicide Rates', fontsize=16)
plt.xlabel('Deaths per 100,000 population', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.show()

# 5. Box plot showing suicide rates by demographic groups
# Assuming STUB_NAME contains demographic information like gender, race, etc.
plt.figure(figsize=(12, 6))
sns.boxplot(x='STUB_NAME', y='ESTIMATE', data=df[df['AGE'] == 'All ages'])
plt.title('Suicide Rates by Demographic Group (All Ages)', fontsize=16)
plt.xlabel('Demographic Group', fontsize=12)
plt.ylabel('Deaths per 100,000 population', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Line chart showing trends for different demographic groups
plt.figure(figsize=(14, 7))
demographic_data = df[(df['AGE'] == 'All ages') & (df['STUB_NAME'] != 'Total')]
for stub, group in demographic_data.groupby('STUB_NAME'):
    plt.plot(group['YEAR'], group['ESTIMATE'], label=stub, marker='.', alpha=0.7)
plt.title('Suicide Rate Trends by Demographic Group (All Ages)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Deaths per 100,000 population', fontsize=12)
plt.legend(title='Demographic Group')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 7. Create a correlation matrix for numerical columns
numerical_cols = ['UNIT_NUM', 'STUB_NAME_NUM', 'STUB_LABEL_NUM', 'YEAR', 'YEAR_NUM', 'AGE_NUM', 'ESTIMATE']
correlation = df[numerical_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix of Numerical Variables', fontsize=16)
plt.tight_layout()
plt.show()

# 8. Time series decomposition (if you have seasonal data)
# Let's create a yearly average for all ages
yearly_avg = df[(df['AGE'] == 'All ages') & (df['STUB_NAME'] == 'Total')].set_index('YEAR')['ESTIMATE']

plt.figure(figsize=(14, 6))
yearly_avg.plot()
plt.title('Yearly Average Suicide Rate (All Ages)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Deaths per 100,000 population', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()