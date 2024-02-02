import pandas as pd

# More on pivot table: https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html
# Read Excel File
df = pd.read_excel('supermarket_sales.xlsx')

# Select columns: 'Gender', 'Product line', 'Total'
df = df[['Gender', 'Product line', 'Total']]

# Make pivot table
pivot_table = df.pivot_table(index='Gender', columns='Product line',
                             values='Total', aggfunc='sum').round(0)

# Export pivot table to Excel file