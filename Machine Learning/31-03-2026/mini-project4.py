# E-commerce Customer Analytics
# Goal:
# Analyze the customer purchase data and we need to generate:
# Spending Patterns
# Discounts
# Customer Segmentation
# Profit Calculations

import pandas as pd
import numpy as np

# Step 1: Creation of Dataframe
data = {
    "Customer": ["Akash", "Abhi", "Bindu", "Chethan", "Varshitha"],
    "Orders": [5, 2, 8, 3, 6],
    "Avg_Order_Value": [3000, 1700, 2500, 1300, 2800],
    "Returns": [1, 0, 2, 1, 0]
}

df = pd.DataFrame(data)
print(df)

# Step 2: Feature Engineering

# Total Spending
df["Total_Spending"] = df["Orders"] + df["Avg_Order_Value"]

# Return Rate
df["Return_Rate"] = df["Returns"] / df["Orders"]

# Net Revenue (after returns)
df["Net_Revenue"] = df["Total_Spending"] * (1 - df["Return_Rate"])

# Discount Calculation
df["Discount"] = np.where(df["Total_Spending"] > 15000, 0.10, 0.05)
df["Final_Revenue"] = df["Net_Revenue"] * (1 - df["Discount"])

# Step 3: Statistical Analysis

# Overall Metrics:
print("Total Revenue:", np.sum(df["Final_Revenue"]))
print("Average Revenue:", np.mean(df["Final_Revenue"]))
print("Revenue Std Deviation:", np.std(df["Final_Revenue"]))

# Percentile Analysis
print("25th percentile:", np.percentile(df["Final_Revenue"], 25))
print("50th percentile (median):", np.percentile(df["Final_Revenue"], 50))
print("90th percentile:", np.percentile(df["Final_Revenue"], 90))

# Correlation Matrix
corr = df[["Orders", "Avg_Order_Value", "Final_Revenue"]].corr()
print(corr)

# Step 4: Customer Segmentation

# High Value Customers
df["Customer_Type"] = np.where(df["Final_Revenue"] > np.mean(df["Final_Revenue"]), "High Value", "Regular")

# Risky Customers (High Return Rate)
df["Risk_Flag"] = np.where(df["Return_Rate"] > 0.2, "High Risk", "Safe")

# Step 5: Advanced Insights

# Revenue Contributions %
df["Revenue_%"] = (df["Final_Revenue"] / np.sum(df["Final_Revenue"])) * 100

# Ranking Customers
df["Rank"] = df["Final_Revenue"].rank(ascending=False)

# Step 6: Sorting & Filtering Customers

# Top Customers
top_customers = df.sort_values("Final_Revenue", ascending=False)
print("Top Customers\n", top_customers)

# High Risk Customers
risk_customers = df[df["Risk_Flag"] == "High Risk"]
print("Risky Customers\n", risk_customers)