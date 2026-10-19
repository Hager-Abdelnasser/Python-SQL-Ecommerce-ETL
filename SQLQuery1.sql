
CREATE DATABASE ecommerce_sales;
GO

USE ecommerce_sales;
GO
CREATE TABLE stg_ecommerce_sales (
  [Order ID] INT NOT NULL PRIMARY KEY,
    [Order Date] DATE NOT NULL,
   [Customer Name] NVARCHAR(150) NOT NULL,
    Region NVARCHAR(50) NOT NULL,
    City NVARCHAR(100) NOT NULL,
    Category NVARCHAR(100) NOT NULL,
    [Sub-Category] NVARCHAR(100) NOT NULL,
    [Product Name] NVARCHAR(255) NOT NULL,
    Quantity INT NOT NULL CHECK (Quantity > 0),
    [Unit Price] DECIMAL(10, 2) NOT NULL CHECK ([Unit Price] >= 0),
    Discount DECIMAL(5, 2) NOT NULL DEFAULT 0.00 CHECK (Discount BETWEEN 0 AND 100),
    Sales DECIMAL(12, 2) NOT NULL CHECK (Sales >= 0),
    Profit DECIMAL(12, 2) NOT NULL,
    [Payment Mode] NVARCHAR(50) NOT NULL
);
BULK INSERT stg_ecommerce_sales
FROM 'C:\Depi_Projects\First_Pipeline\Cleaned_Ecommerce_Sales.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    TABLOCK
);