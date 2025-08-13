import pandas as pd
from io import StringIO


# Scenario: You have a hospital patient dataset and need to filter relevant data for analysis.

# Tasks:

# Get all patients from the "Cardiology" department.
# Find patients older than 40.
# Sort patients by age in descending order.


data = """PatientID,Name,Age,Department,VisitDate
1,Hamza,45,Cardiology,2024-03-01
2,Ayesha,32,Neurology,2024-03-02
3,Ali,60,Cardiology,2024-03-02
4,Sara,27,Orthopedics,2024-03-03"""


fd = pd.read_csv(StringIO(data))


# # point 01
# FilteredFd1 = fd[fd["Department"] == "Cardiology"]
# print(FilteredFd1)

# # point 02
# FilteredFd2 = fd[fd["Age"] > 40]
# print(FilteredFd2)

# # Point 03
# FilteredFd3 = fd.sort_values(by="VisitDate", ascending=[False])
# print(FilteredFd3)


