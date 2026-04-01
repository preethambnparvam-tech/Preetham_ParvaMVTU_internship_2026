
# Student Performance Analysis


# Goal: Analyse the student marks and find insights


# Step 1: Load Data using Pandas
import pandas as pd


data = {
    "Name": ["A", "B", "C", "D"],
    "Maths": [85, 90, 75, 60],
    "Science": [78, 93, 72, 95]
}


df = pd.DataFrame(data)


# Step 2: Add New Column (Total & Average)
df["Total"] = df["Maths"] + df["Science"]
df["Average"] = df["Total"] / 2
print("Total & Average Marks Calculated")
print(df)


# Step 3: Find Top Performers
top_student = df.sort_values("Total", ascending=False).iloc[0]
print("Top Performer: \n",top_student)


# Step 4: Using Numpy for Statistics
import numpy as np


avg_marks = np.mean(df["Total"])
std_marks = np.std(df["Total"])


print("Overall Statistics:")
print(f"Average Marks: {avg_marks}")
print(f"Std Marks: {std_marks}")


# Step 5: Filtering Students
high_performers = df[df["Average"] > 75]
print("High Performers:\n", high_performers)


low_performers = df[df["Average"] < 70]
print("Low Performers:\n", low_performers)
