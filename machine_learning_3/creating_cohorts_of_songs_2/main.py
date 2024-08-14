import functions
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

####################################################
# Perform outlier treatment here (Work in Progress)
####################################################

# 2. Refine Data (Work in Progress)

# 3. Perform Exploritory Data Analysis and Feature Engineering
# a. Use visualizations to identify the two most popular albums

# print(df['popularity'])

# Shows Unique Entries in the "Album" Column
print(df['album'].unique())

# Groups Data Based on Album, then the Sum of "Popularity"
# is Taken Based on "Album," and finally, Values are Sorted
df_total_popular = df.groupby(['album'])['popularity'].sum().sort_values(ascending=False)
print('Most Popular Albums', df_total_popular.head())

# Bar Plot
sns.barplot(x=df_total_popular.tail().index, y=df_total_popular.head().values)
plt.title('Bar plot')
if show_plots:
    plt.show()

# b. Delve into Various Features of Songs,
# Aiming to Identify Patterns

# c. Examine the Relationship Between a Song's Popularity
# and Various Factors, Exploring How This Correlation has Evolved

# d. Provide Insights on the Significance of Dimensionality Reduction
# Techniques. Share your Ideas and Elucidate your Observations

# 4. Perform Cluster Analysis
# a. Identify the Right Number of Clusters

# b. Use Appropriate Clustering Algorithms

# c. Define Each Cluster Based on the Features