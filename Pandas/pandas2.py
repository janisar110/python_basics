import pandas as pd
from io import StringIO
# Scenario: You’re cleaning student performance data before training an AI model.

# Tasks:

# 1: Fill missing values with the column mean.
# 2: Rename columns to lowercase.
# 3: Create a new column called "Average" showing each student's average score.


data = """Name,Math,Science,English
Ayesha,90,88,92
Bilal,85,,80
Sara,78,75,NaN
John,NaN,82,85
"""


fd = pd.read_csv(StringIO(data))

# # point 01
meansVal = fd.fillna(fd.mean(numeric_only=True))

# # point 02
# lowerCaseValues = fd.columns.str.lower()
# print(lowerCaseValues)

# point 03
meansVal["Average"] = meansVal[["Math", "Science", "English"]].mean(axis=1)

print("data",meansVal)
