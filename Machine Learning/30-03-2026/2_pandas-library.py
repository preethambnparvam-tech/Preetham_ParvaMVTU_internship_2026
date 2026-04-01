# Pandas Library is used for creating DataFrames and to work with excel files(CSV - Comma Seperated Values) and Data Analysis

# importing pandas library with alias pd
import pandas as pd

# DataFrame()
data = {"Name": ["A", "B", "C", "D"], "Age": [20, 30, 40, 50]}
df = pd.DataFrame(data)
print(df)

# From List of Dictionaries
df = pd.DataFrame([
    {"Name": "Akshay", "Age": 24},
    {"Name": "Ajay", "Age": 23},
    {"Name": "Jay", "Age": 35},
])
print(df)

# read_csv()
df = pd.read_csv("data.csv")
print(df.head())
# info()
print(df.info())

df = pd.read_csv("weather.csv")
print(df.head())
print(df.info())
print(df.columns)

# head() and tail()
# To fetch the data from top or bottom with number-of-data
print(df.head(2))
print(df.tail(2))

# Targetting individual columns
# Column based selection
print("Cities:")
print(df["city"])
print("Temperature")
print(df["temp"])

# loc - label-based selection
# Row based selction
print(df.loc[3])

# iloc - index-based selection
print(df.iloc[0:1])

# conditional filtering
print(df[df["temp"] > 35.5])

print(df[(df["humidity"] > 40) & (df["humidity"] < 50)])

# adding new column
df["average-rainfall(%)"] = [20,23.5,15.3,26, 20, 23]
print(df)

# Update column
df["humidity"] = df["humidity"] + 5
print(df)

# Isnull() - handling the missing values
print(df.isnull())

# dropna() - dropping the rows with missing values
# df.dropna(inplace=True)
# print(df)

# fillna() - filling the missing values
df.fillna(0, inplace=True)
print(df)

# describe() - gives the statistical summary of the data
print(df.describe())

# mean()
print(df["humidity"].mean)

# sum()
print(df["humidity"].sum())

# sort_values()
print(df.sort_values("city"))
print(df.sort_values("temp"))

# group_by()
data = {
    "Dept": ["Dev", "Dev", "QA", "Dev", "QA"],
    "Salary": [15000, 18000, 13500, 20000, 16000]
    }

df = pd.DataFrame(data)
print(df.groupby("Dept").sum())

# unique() - gives the unique values in the column
print(df["Dept"].unique())

# value_counts() - gives the count of each unique values in the column
print(df["Dept"].value_counts())

# to_csv()
df.to_csv("new_data.csv", index=False)