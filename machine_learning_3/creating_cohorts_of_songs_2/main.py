import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.cluster import KMeans

# Create Data Frame
df = pd.read_csv('rolling_stones_spotify.csv')

# 1. Initial Data Inspection and Cleaning:
# Look for duplicates, missing values,
# irrelevant entries, or outliers

# Show info
print(df.info())
print(df.head())

# Check for missing values in data
print(df.isna().sum())
