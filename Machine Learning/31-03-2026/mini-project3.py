# Data Cleaning


# Goal: Handle the missing data


# Step 1: Dataset with Missing Values
import numpy as np
import pandas as pd


data = {
    "Name": ["A", "B", "C", "D"],
    "Age": [24, None, 26, None],
    "Salary": [5000, 7000, None, 8000]
}


df = pd.DataFrame(data)
print(df)


# Step 2: Detect the Missing Values
print(df.isnull())


# Step 3: Fill the Missing Values using Numpy & Pandas
df["Age"].fillna(np.mean(df["Age"]), inplace=True)
df["Salary"].fillna(np.median(df["Salary"]), inplace=True)


print("Data after cleaning: \n",df)


# Step 4: Convert the data to Numpy Array
arr = df.values
print(arr)
