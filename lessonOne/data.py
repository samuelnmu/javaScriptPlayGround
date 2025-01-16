import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the "tips" dataset from Seaborn
tips = sns.load_dataset("tips")

# Display the first few rows of the dataset
print(tips.head())

# Summary statistics of the dataset
print(tips.describe())

# Information about the dataset
print(tips.info())

# Check for missing values
print(tips.isnull().sum())

# If there were missing values, you could handle them like this:
# tips.dropna(inplace=True)  # Drop missing values
# OR
# tips.fillna(method='ffill', inplace=True)  # Fill missing values using forward fill

plt.figure(figsize=(10, 6))
sns.histplot(tips['total_bill'], kde=True, bins=30)
plt.title('Distribution of Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Total Bill by Day')
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.show()

plt.figure(figsize=(10, 6))
corr = tips.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


#Explanation
#Importing Libraries: We import Pandas, NumPy, Matplotlib, and Seaborn libraries.
#Loading the Dataset: We load the "tips" dataset from Seaborn.
#Exploring the Dataset: We display the first few rows, summary statistics, and information about the dataset.
#Data Cleaning: We check for missing values and handle them if necessary.
#Data Visualization: We create various plots to visualize the data, including a histogram, scatter plot, box plot, and correlation heatmap.