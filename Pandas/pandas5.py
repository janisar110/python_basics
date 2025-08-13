import pandas as pd
from io import StringIO
import time 


# Scenario: You’re preparing ride-hailing trip data for an AI pricing model.

# Tasks:

# Calculate trip duration in minutes.
# Create a new column "PricePerKM".
# Normalize the "DistanceKM" column between 0 and 1.


data = """TripID,PickupTime,DropTime,DistanceKM,Price
1,2024-03-01 08:00,2024-03-01 08:30,10,5
2,2024-03-01 09:15,2024-03-01 09:45,8,4
3,2024-03-01 10:00,2024-03-01 10:20,5,3"""


fd = pd.read_csv(StringIO(data))


# # point 01
# fd["Time Duration"] = pd.to_datetime(fd["PickupTime"]) - pd.to_datetime(fd["DropTime"])
# print(fd)

# point 02
fd["PricePerKM"] = fd["DistanceKM"] / fd["Price"]
print(fd)

# # Point 03
# FilteredFd3 = fd.groupby("Product")["Quantity"].sum().idxmax()
# print(FilteredFd3)


