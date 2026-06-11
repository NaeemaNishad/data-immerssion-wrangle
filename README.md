# ApexPlanet Sales Transaction Analytics Pipeline

## 📌 Project Objective
This repository contains the deliverables for Task 1 of my Data Analytics Internship at ApexPlanet. The goal is to ingest, profile, clean, and transform the official sales transaction dataset (1,000 records) into a pristine, structured format optimized for business intelligence reporting.

---

## 📊 Data Dictionary

| Column Name | Data Type | Description | Business Relevance |
| :--- | :--- | :--- | :--- |
| `Order_ID` | Alphanumeric | Unique string code identifying each specific transaction. | Essential for transaction tracking and tracking unique sales entries. |
| `Order_Date` | Datetime | The calendar date when the transaction occurred. | Allows temporal trend analysis, seasonality tracking, and monthly growth calculations. |
| `Customer_ID` | Alphanumeric | Unique code identifying an individual customer account. | Crucial for tracking user purchase frequency and calculating client retention rates. |
| `Customer_Name`| String | Full name of the purchasing customer. | Personalizes marketing materials and updates customer profiles. |
| `Age` | Integer | The age of the customer in years. | Allows age-cohort segmentation and targeted audience demographic insights. |
| `Gender` | Categorical | Customer-reported gender classification. | Used to segment product portfolios and consumer choices. |
| `City` | Categorical | The geographic location/city of the buyer. | Optimizes localized marketing spends and logistics/distribution planning. |
| `Product` | String | Specific name or type of the item purchased. | Informs inventory stocking levels and determines product popularity. |
| `Category` | Categorical | The high-level department grouping of the product. | Drives departmental revenue summaries and product taxonomy optimization. |
| `Quantity` | Integer | Number of units purchased in the transaction line. | Measures inventory depletion speed and helps scale price adjustments. |
| `Unit_Price` | Float | The financial cost of a single item unit. | Baseline price point used for margin analysis and discount planning. |
| `Total_Sales` | Float | The calculated line item revenue ($\text{Quantity} \times \text{Unit\_Price}$). | The primary gross revenue indicator used for financial bottom-line metrics. |
| `Age_Group` | Categorical | **[Engineered]** Customer demographic bins (Gen Z, Millennials, Gen X, Seniors). | Simplifies demographic analysis down to cohesive target buckets. |
| `Year_Month` | String | **[Engineered]** Extracted order period ($YYYY-MM$). | Essential for calculating month-over-month growth patterns. |
