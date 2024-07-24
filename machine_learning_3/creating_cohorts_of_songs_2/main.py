import functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from sklearn.cluster import KMeans

# Control Variables
show_plots = False

# Create Data Frame
df = pd.read_csv('rolling_stones_spotify.csv')

# 1. Initial Data Inspection and Cleaning:
# Look for duplicates, missing values,
# irrelevant entries, or outliers

# Show info
print(df.info())
# print(df.head())

# Check for missing values in data
print('Number of missing values for each column:')
print(df.isna().sum())

# Drop Unnamed Column
df1 = df.drop(columns='Unnamed: 0')

# Check for duplicates
print('Number of duplicate entries:', df1.duplicated().sum())

# Box plots to detect outliers
columns = df1.columns.tolist()
# print(columns)
functions.box_plot_outlier(df, columns, show_plots)

###
# Perform outlier treatment here (Work in Progress)
###

# 2. Refine Data (Work in Progress)

# 3. Perform Exploritory Data Analysis and Feature Engineering
# a. Use visualizations to identify the two most popular albums

print(df['popularity'])
print(df['album'].unique())
# sns.scatterplot(data=df, x="id", y="popularity")
# plt.show()