# 🛒 E-Commerce Sales ETL Pipeline (Python & SQL Server)

An automated End-to-End ETL (Extract, Transform, Load) pipeline project designed to process raw e-commerce sales data, perform data cleaning and quality validation using **Python (Pandas & NumPy)**, and load the cleaned dataset into **Microsoft SQL Server**.

---

## 🛠️ Tech Stack & Tools
- **Language:** Python
- **Libraries:** Pandas, NumPy
- **Database:** Microsoft SQL Server (T-SQL)
- **Tools:** VS Code, Git, SSMS

---

## 🚀 Key Pipeline Steps

### 1. Data Cleaning & Transformation (Python)
- Cleaned and standardized column header names.
- Converted date strings to datetime objects and filtered out future or invalid dates.
- Handled text formatting (trimmed whitespaces, title case for categories and locations).
- Managed extreme numerical outliers in `Sales` and `Profit` using the **Interquartile Range (IQR)** method.
- **Data Quality Assurance:** Implemented strict `assert` validation checks to guarantee zero duplicates and valid non-negative quantities before outputting the final dataset.

### 2. Database Staging & Loading (SQL Server)
- Designed a structured staging table (`stg_ecommerce_sales`) with proper primary keys, data types, and check constraints (`CHECK` for quantity, price, and discounts).
- Executed high-performance `BULK INSERT` to rapidly ingest the transformed CSV into SQL Server.

---

## 📂 Repository Structure
```text
📦 Python-SQL-Ecommerce-ETL
 ┣ 📜 Python code .py       # Main Python ETL script for cleaning & transformation
 ┣ 📜 SQLQuery1.sql         # SQL schema creation & BULK INSERT query
 ┗ 📜 README.md             # Project documentation
