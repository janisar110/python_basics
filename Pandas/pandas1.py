import pandas as pd
from io import StringIO

# Sample CSV data (simulating a file)
data = """OrderID,Customer,Product,Quantity,Price,Date
1,Ali,Laptop,1,800,2024-02-01
2,Sara,Mouse,2,15,2024-02-01
3,John,Keyboard,1,45,2024-02-02
4,Ali,Monitor,1,200,2024-02-03
5,Ali,Monitor,1,200,2024-02-03
6,Ali,Monitor,1,200,2024-02-03
7,Ali,Monitor,1,200,2024-02-03
8,Ali,Monitor,1,200,2024-02-03
9,Afzal,Monitor,1,1000,2024-02-03
"""
# CSV - Comma seperated Value
# Load CSV into DataFrame
df = pd.read_csv(StringIO(data))

# # 1. Display first 5 rows
# print("First 5 Rows:")
# print(df.head()) #default argument is 5 rows

# # 2. Column names and data types
# print("\nColumn Names:", df.columns.tolist())
# print("Data Types:\n", df.dtypes)

# # 3. Summary statistics
# print("\nSummary Statistics:")
# print(df.describe())

# # 4. Total revenue for all orders
# df["Total"] = df["Quantity"] * df["Price"]
# total_revenue = df["Total"].sum()
# print("\nTotal Revenue:", total_revenue)

# # 5. find the minimum price from data show this order details

# # print("Price Column: ", df["Price"].max())
# print("Winner: ", df.max())
# print("Winner: ", df.min())
