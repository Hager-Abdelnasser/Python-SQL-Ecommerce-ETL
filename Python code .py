import numpy as np
import pandas as pd




file_path = "C:/Depi_Projects/First_Pipeline/Ecommerce_Sales_Data_2024_2025.csv"
print(f"--- Starting to read data from file: {file_path} ---")

df_raw = pd.read_csv(file_path)
df = df_raw.copy()
print("\n--- Overview of data before cleaning ---")
print(df.info())

# 2.Data cleaning & Transformation

df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("-", "_")


df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

df = df.dropna(subset=["Order_Date"])
df = df[df["Order_Date"] <= pd.Timestamp.now()]


if "Order_ID" in df.columns:
    df = df.drop_duplicates(subset=["Order_ID"], keep="first")

text_columns = [
    "Customer",
    "Region",
    "City",
    "Category",
    "Sub_Category",
    "Product_Name",
    "Payment_Mode",
]

for col in text_columns:
    if col in df.columns:
        df[col] = (
            df[col]
            .fillna("Unknown")
            .astype(str)
            .str.strip()
            .str.title()
        )

df["Quantity"] = (
    pd.to_numeric(df["Quantity"], errors="coerce")
    .fillna(0)
    .astype(int)
)

if "Sales" in df.columns:
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce").fillna(0).round(2)

if "Profit" in df.columns:
    df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce").fillna(0).round(2)

# Discount Formatting & Boundaries)
if "Discount" in df.columns:
    df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce").fillna(0)


for numeric_col in ["Sales", "Profit"]:
    if numeric_col in df.columns:
        Q1 = df[numeric_col].quantile(0.25)
        Q3 = df[numeric_col].quantile(0.75)
        IQR = Q3 - Q1
        upper_bound = Q3 + (1.5 * IQR)
        lower_bound = Q1 - (1.5 * IQR)
        
        df[numeric_col] = np.where(
            df[numeric_col] > upper_bound,upper_bound,
            np.where(df[numeric_col] < lower_bound, lower_bound, df[numeric_col])
        ).round(2)

df = df[(df["Sales"] >= 0) & (df["Quantity"] > 0)]

categorical_cols = ["Region", "Category", "Payment_Mode"]
for col in categorical_cols:
        df[col] = df[col].astype("category")
        
# Data Quality 
assert df["Order_ID"].is_unique, "Data Quality Error: Duplicate Order IDs found!"
assert (df["Sales"] >= 0).all(), "Data Quality Error: Negative sales values found!"
assert (df["Quantity"] > 0).all(), "Data Quality Error: Invalid quantity values found!"
assert not df["Order_Date"].isna().any(), "Data Quality Error: Missing order dates found!"

print(f"\nAll advanced cleaning steps executed successfully! Final valid rows count: {len(df)}")

print("\n--- Overview of data after advanced cleaning and transformation ---")
print(df.head())
print(df.info())

df.to_csv("C:/Depi_Projects/First_Pipeline/Cleaned_Ecommerce_Sales.csv", index=False)
print(" تم حفظ الملف")
