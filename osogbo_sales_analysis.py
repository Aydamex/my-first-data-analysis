# My First Data Analysis - by Adedamola Adeyinka - Osogbo Focus
import pandas as pd

# Sample sales data for an Osogbo business
data = {
    'Product': ['Palm Oil', 'Cocoa', 'Adire Fabric', 'Ofada Rice', 'Plantain'],
    'Sales': [65000, 48000, 72000, 55000, 39000],
    'Profit': [12000, 8500, 15000, 9000, 6200]
}

df = pd.DataFrame(data)

print("=== OSOGBO SALES ANALYSIS ===")
print(df)
print("\nTotal Sales: N", df['Sales'].sum())
print("Total Profit: N", df['Profit'].sum())
print("Best Selling Product:", df.loc[df['Sales'].idxmax(), 'Product'])
print("Most Profitable Product:", df.loc[df['Profit'].idxmax(), 'Product'])

print("\nAnalysis done by Adedamola Adeyinka - Accountant & Data Analyst Learner")