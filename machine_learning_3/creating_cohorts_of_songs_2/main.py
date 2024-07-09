import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.cluster import KMeans

# Create Data Frame
df = pd.read_csv('HR_comma_sep.csv')

# Show info
print(df.info())

# Show first rows
print(df.head())
