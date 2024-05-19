import pandas as pd

# Import Marketing Campaign Data into a Data Frame
df = pd.read_csv('marketing_data.csv')

# Print Columns of Marketing Data
print(df.columns)

# 1. Print Data for Income and Dt_Customer
income = df['Income']
Dt_Customer = df['Dt_Customer']
print(income, Dt_Customer)

# 2. Fill in Missing Values if Any