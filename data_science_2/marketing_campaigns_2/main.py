from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns
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

# Remove Dollar Sign and Comma from String
income_fix = income.str.replace(r'[$,]+', '', regex=True)

# Convert Income Values from Object to Float
income = income_fix.astype('float')

# Insert FLoat Income into Data Frame
df['Income'] = income
print(df['Income'])

# Extract Entries with No Income Info
empty_entries = df[df['Income'].isnull() == True]
print(empty_entries['Marital_Status'], empty_entries['Education'])

# Options for Marital Status in Missing Income Entries are as Follows:
# Single, Married, Together, and Widow
# Options for Education in Missing Income Entries are as Follows:
# Graduation, Master, PhD, and 2n Cycle

# Method for Replacing Null Income Values
# to Average Incomes Based on Marital
# Status and Education
for index, row in empty_entries.iterrows():
    # print(f"Index: {index}, Marital Status: {row['Marital_Status']}, Education: {row['Education']}")
    avg_value = df.loc[(df['Marital_Status'] == row['Marital_Status']) &
                       (df['Education'] == row['Education'])]['Income'].mean()
    # print(avg_value)
    df.loc[index, 'Income'] = avg_value

# Checking for missing values again
missing_values = df.isnull().sum()
print("Missing Values per Column:")
print(missing_values)

# 3. Find Total Number of Children, Age, and Spending Variables
current_year = date.today().year
df['total_children'] = df['Kidhome'] + df['Teenhome']
df['age'] = df['Year_Birth'].apply(lambda x: current_year - x)
df['total_spending'] = (df['MntWines'] + df['MntFruits'] + df['MntMeatProducts']
                        + df['MntFishProducts'] + df['MntSweetProducts'] + df['MntGoldProds'])


# 3a. Total Purchases Across the 3 Channels
df['total_purchases'] = df['NumWebPurchases'] + df['NumCatalogPurchases'] + df['NumStorePurchases']

# 4. Generate Box Plots and Histograms

# Total Children Box Plot (Doesn't make too much sense)
# sns.boxplot(y='total_children', data=df)
# plt.title('Box Plot: Total Number of Children Distribution')
# plt.xlabel('All Data')
# plt.ylabel('Total Number of Children')
# plt.show()

# Age Box Plot
sns.boxplot(y='age', data=df)
plt.title('Box Plot: Age Distribution')
plt.xlabel('All Data')
plt.ylabel('Age in Years')
plt.show()

# Total Spending Box Plot
sns.boxplot(y='total_spending', data=df)
plt.title('Box Plot: Total Spending Distribution')
plt.xlabel('All Data')
plt.ylabel('Total Spending in US Dollars')
plt.show()

# Total Purchases Box Plot
sns.boxplot(y='total_purchases', data=df)
plt.title('Box Plot: Total Purchases Distribution')
plt.xlabel('All Data')
plt.ylabel('Total Purchases in Count')
plt.show()

# Histogram of Age
sns.histplot(df['age'], bins=20, kde=True)
plt.title('Histogram: Distribution of Age')
plt.show()

# Histogram of Total Spending
sns.histplot(df['total_spending'], bins=10, kde=True)
plt.title('Histogram: Distribution of Total Spending')
plt.show()

# Histogram of Total Purchases
sns.histplot(df['total_purchases'], bins=20, kde=True)
plt.title('Histogram: Distribution of Total Purchases')
plt.show()

# 5. Apply Ordinal and One-Hot Encoding 