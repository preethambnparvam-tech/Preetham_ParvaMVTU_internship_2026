# Sales Data Analysis


# Goal: Analyze the Company Sales


import pandas as pd
import numpy as np


# Step 1: Prepare the Data
data = {
    "Product": ["Apple", "Samsung", "Apple", "Oppo", "Samsung"],
    "Sales": [150, 230, 135, 185, 210]
}


df = pd.DataFrame(data)


# Step 2: Total Sales per Product
sales_summary = df.groupby("Product").sum()
print("Sales Summary:\n",sales_summary)


# Step 3: Using Numpy for insights
sales_array = np.array(df["Sales"])


print("Max Sale:", np.max(sales_array))
print("Min Sale:", np.min(sales_array))


# Step 4: Sort Data
sorted_df = df.sort_values("Sales", ascending=False)
print("Sales Data from High to Low: \n",sorted_df)


# Step 5: Unique Products
print("Unique Products:")
print(df["Product"].unique())
