import pandas as pd
import numpy as np

data = {
    "Name": ["Rima", "Alok", "Priyanka", "Anandita", "Priyanka"],
    "Age": [21, np.nan, 18, 20, 18],
    "Stream": ["Math", "Commerce", "Biology", "Arts", "Biology"],
    "Percentage": [58, 92, 90, np.nan, 90],
    "Count": [1, 2, 3, 4, 5],
}

labels = ["A", "B", "C", "D", "E"]

df = pd.DataFrame(data,index=labels)
print (df)

print("\nDescribe the df")
print(df.describe())

print("\nRows where Percentage is missing:")
print(df[df['Percentage'].isnull()])

print("\nPrint all rows having any column missing")
print(df.isnull())

print("\nDisplay df excluding nan rows")
print(df.dropna())

print("\nRemove Duplicate rows")
df=df.drop_duplicates()
print(df)

print("\nReplacing missing values")
df=df.fillna(0)
print(df)


