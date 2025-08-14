import pandas as pd
from io import StringIO
import time 

# Tasks
# 1. Har sale ka Total_Sales nikalna (Units_Sold × Unit_Price).
# 2. Region ke hisaab se total sales ka sum nikalna.
# 3. Product ke hisaab se average units sold nikalna.
# 4. Top 2 regions find karo jinke sales sabse zyada hain.
# 5. Sirf un rows ko filter karo jahan Total_Sales > 3000.

data = """Date,Region,Product,Units_Sold,Unit_Price
2025-01-01,East,Laptop,4,800
2025-01-01,West,Mobile,10,500
2025-01-02,East,Laptop,5,800
2025-01-02,North,Tablet,8,300
2025-01-03,South,Mobile,5,500"""


fd = pd.read_csv(StringIO(data))


# # point 01
# fd["Total_Sales"] = fd["Units_Sold"] *  fd["Unit_Price"] 
# print(fd)


# # point 02
# dataWithRegion = fd.groupby("Region")["Total_Sales"].sum().reset_index()
# print(dataWithRegion)


# # point 03
# totalAverage = fd.groupby("Product")["Units_Sold"].mean()
# print(totalAverage)


# # point 04
# top2Region = fd.sort_values("Total_Sales", ascending=False)
# print(top2Region.head(2))


#  # point 05
# totalSalesConditon = fd[fd["Total_Sales"] > 3000]
# print(totalSalesConditon)








