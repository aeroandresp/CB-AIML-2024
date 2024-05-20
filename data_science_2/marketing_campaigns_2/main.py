import pandas as pd

# Import Marketing Campaign Data into a Data Frame
df = pd.read_csv('marketing_data.csv')

# Print Columns of Marketing Data
print(df.columns)

# Print Data Types
print(df.dtypes)

# 1. Print Data for Income and Dt_Customer
income = df['Income']
Dt_Customer = df['Dt_Customer']
print(income, Dt_Customer)

# 2. Fill in Missing Values if Any
# Checking for missing values
missing_values = df.isnull().sum()
print("Missing Values per Column:")
print(missing_values)

# Income has 24 Missing Entries
# Use Education and Martial Status
# To Calculate an Average Income for Them
# df_filled = df.fillna(df.mean())


# Extract Entries with No Income Info
empty_entries = df[df['Income'].isnull() == True]
print(empty_entries['Marital_Status'],empty_entries['Education'])

# Remove Dollar Sign and Comma from String
income_fix = income.str.replace(r'[$,]+','', regex=True)

# Convert Income Values from Object to String
income = income_fix.astype('float')