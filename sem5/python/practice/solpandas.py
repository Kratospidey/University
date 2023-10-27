# import pandas as pd

# Create a DataFrame
# df = pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"]})
# print(df)
# print(df["A"][1])

# print(pd.Series({"A": 1, "B": 2}))
# print(pd.DataFrame({"Name": ["Rima", "Alok"], "Age": [21, 19]}))
# print(pd.Series({"Name": "Param", "Age": 69}))

# df = pd.read_csv("data.csv")

# 1 i
# print(df[(df["Name"].str.startswith("A")) & (df["Percentage"] > 85)])

# 1 ii
# print(df.loc[:,'Age'])
# print(df.loc[:,'Age'].mean())

# 1 iii
# print(df.iloc[[0, 2]])

# 1 iv

# df["Percentage"] = df["Percentage"] / 100
# print(df)


data = {
    "Name": ["Alice", "Bob", None, "Charlie", "David"],
    "Age": [25, None, 35, None, 29],
    "City": ["New York", "San Francisco", "Los Angeles", None, "Chicago"],
}

# dt = pd.DataFrame(data)


# print(dt.isnull().sum())

# Cleaning Name column:
# dt["Name"].fillna("Unknown", inplace=True)

# Cleaning Age column:
# dt["Age"].fillna(0, inplace=True)

# Cleaning City column:
# dt["City"].fillna("Unknown", inplace=True)

# print(dt)
