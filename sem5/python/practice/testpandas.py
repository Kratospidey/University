import pandas as pd


df = pd.read_csv("data.csv")

# 1 i
# print(df[(df["Name"].str.startswith("A")) & (df["Percentage"] > 85)])

# 1 ii
# print(df.loc[:, "Age"])
# print(df.loc[:, "Age"].mean())

# 1 iii
# print(df.iloc[:, [0, 2]])

# 1 iv
# df["Percentage"] = df["Percentage"] / 100
# print(df)

# 2
# data = {
#     "Name": ["Alice", "Bob", None, "Charlie", "David"],
#     "Age": [25, None, 35, None, 29],
#     "City": ["New York", "San Francisco", "Los Angeles", None, "Chicago"],
# }
# dt = pd.DataFrame(data)
# print(dt.isnull().sum())

# dt["Name"].fillna("Unknown", inplace=True)
# dt["City"].fillna("Unknown", inplace=True)
# dt["Age"].fillna(0, inplace=True)
# print(dt)

# print(help(pd.DataFrame.loc))

