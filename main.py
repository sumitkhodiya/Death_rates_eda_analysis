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
plt.title('Suicide Rate Trend (All Ages)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Deaths per 100,000 population', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 2. Distribution of suicide rates
plt.figure(figsize=(10, 6))
sns.histplot(df['ESTIMATE'].dropna(), bins=30, kde=True)
plt.title('Distribution of Suicide Rates', fontsize=16)
plt.xlabel('Deaths per 100,000 population', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.show()

# 3. Box plot showing suicide rates by demographic groups
plt.figure(figsize=(12, 6))
demo_data = df[(df['AGE'] == 'All ages')]
sns.boxplot(x='STUB_NAME', y='ESTIMATE', data=demo_data)
plt.title('Suicide Rates by Demographic Group (All Ages)', fontsize=16)
plt.xlabel('Demographic Group', fontsize=12)
plt.ylabel('Deaths per 100,000 population', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Demographic group comparisons over time
plt.figure(figsize=(14, 7))
demo_time_data = df[(df['AGE'] == 'All ages') & (df['STUB_NAME'] != 'Total')]

for stub in demo_time_data['STUB_NAME'].unique():
    group_data = demo_time_data[demo_time_data['STUB_NAME'] == stub]
    plt.plot(group_data['YEAR'], group_data['ESTIMATE'], label=stub, marker='.', alpha=0.7)
    
plt.title('Suicide Rate Trends by Demographic Group (All Ages)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Deaths per 100,000 population', fontsize=12)
plt.legend(title='Demographic Group')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 5. Create a correlation heatmap for numerical columns
numerical_cols = ['YEAR', 'YEAR_NUM', 'AGE_NUM', 'ESTIMATE']
correlation = df[numerical_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix of Numerical Variables', fontsize=16)
plt.tight_layout()
plt.show()

# 6. Top demographic groups with highest suicide rates (most recent year)
recent_demo = df[(df['YEAR'] == df['YEAR'].max()) & 
                 (df['AGE'] == 'All ages') & 
                 (df['STUB_NAME'] != 'Total')]

plt.figure(figsize=(12, 6))
sorted_demo = recent_demo.sort_values('ESTIMATE', ascending=False).head(10)
sns.barplot(x='ESTIMATE', y='STUB_NAME', data=sorted_demo)
plt.title(f'Top Demographics by Suicide Rate ({df['YEAR'].max()})', fontsize=16)
plt.xlabel('Deaths per 100,000 population', fontsize=12)
plt.ylabel('Demographic Group', fontsize=12)
plt.tight_layout()
plt.show()

# 7. Time series decomposition - showing yearly trends
plt.figure(figsize=(14, 6))
yearly_avg = df[(df['AGE'] == 'All ages') & (df['STUB_NAME'] == 'Total')].groupby('YEAR')['ESTIMATE'].mean()
yearly_avg.plot()
plt.title('Yearly Average Suicide Rate (All Ages)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Deaths per 100,000 population', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 8. Alternative to the problematic heatmap - Create a pairplot for key variables
sample_data = df.sample(min(1000, len(df)))
sns.pairplot(sample_data[['YEAR', 'AGE_NUM', 'ESTIMATE']])
plt.suptitle('Relationships Between Key Variables', y=1.02, fontsize=16)
plt.tight_layout()
plt.show()