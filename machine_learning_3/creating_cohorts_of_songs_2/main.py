import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from sklearn.cluster import KMeans

# Control Variables
show_plots = True

# Create Data Frame
df = pd.read_csv('rolling_stones_spotify.csv')

# 1. Initial Data Inspection and Cleaning:
# Look for duplicates, missing values,
# irrelevant entries, or outliers

# Show info
print(df.info())
# print(df.head())

# Check for missing values in data
print(df.isna().sum())

# Drop Unnamed Column
df1 = df.drop(columns='Unnamed: 0')

# Box Plots
columns = df1.columns.tolist()
print(columns)

for col in columns:
    # print(col, 'is', df1[col].dtypes)
    if df1[col].dtypes != 'object':
        sns.boxplot(y=col, data=df1)
        plt.title('Box Plot')
        plt.xlabel('All Data')
        plt.ylabel(col)
        if show_plots:
            plt.show()
