import pandas as pd

data = {
    "Name": ["Rima", "Alok", "Anandita", "Priyanka"],
    "Age": [21, 19, 20, 18],
    "Stream": ["Math", "Commerce", "Arts", "Biology"],
    "Percentage": [58, 92, 85, 30],
}

labels = ["A", "B", "C", "D"]

df = pd.DataFrame(data, index=labels)

print(df)
print("\nName starts with A and percentage is greater than 85: ")
print(df[(df["Name"].str[0] == "A") & (df["Percentage"] > 85)])
print("\nDisplay Age and per columns of only first and second row using loc()")

result = df.loc["A":"B", ["Age", "Percentage"]]
print(result)

print("\nDisplay Age column using loc()")
result = df.loc[:, 'Age']
print(result)

print("\nMean score of age column")
print(df['Age'].mean())

print("\nDisplay 0th and 2nd index using iloc()")
result = df.iloc[[0,2]]
print(result)


