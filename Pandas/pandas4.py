import pandas as pd
from io import StringIO


# Scenario: You’re working with e-commerce transaction logs for AI purchase prediction.

# Tasks:

# Find total amount spent by each customer.
# Count how many different products each customer bought.
# Find the most purchased product.


data = """Customer,Product,Quantity,Price
Ali,Laptop,1,800
Sara,Mouse,2,15
John,Keyboard,1,45
Ali,Monitor,1,1000
Sara,Mouse,1,15"""


fd = pd.read_csv(StringIO(data))


# # point 01
# fd["Total"] = fd["Price"] * fd["Quantity"]
# print(fd)

# # point 02
# FilteredFd2 = fd.groupby("Customer")["Product"].nunique()
# print(FilteredFd2)

# # Point 03
# FilteredFd3 = fd.groupby("Product")["Quantity"].sum().idxmax()
# print(FilteredFd3)


