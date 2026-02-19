# data_analyst_intern_assignment_py
Python project for data cleaning, funnel analysis, and customer insights
# 📊 Data Analyst Funnel Analysis (Python)

This project shows how to clean raw data, prepare it for analysis, and build a simple **engagement → purchase funnel** using Python and Pandas.  
The focus is on writing reliable data preparation code, applying clear assumptions, and presenting the workflow in a clean, reproducible way.

🎥 **Demo Video (Project Output):**  
👉 https://drive.google.com/file/d/1H77ByiBTZap2INmewruIvRnonTAzF3yb/view?usp=drivesdk

---

## 🎯 Project Goals

- Clean and standardize data from multiple sources  
- Prepare datasets for funnel analysis (user engagement → orders)  
- Ensure data quality (dates, duplicates, valid orders, IDs)  
- Document assumptions and decisions clearly  
- Present the workflow in a simple, easy-to-follow way  

---

## 📁 Repository Contents

- `analysis.py` (or `analysis.ipynb`)  
  - Contains the full Python code for:
    - Loading data
    - Converting date columns to proper datetime format
    - Removing duplicate records
    - Filtering only valid orders
    - Standardizing IDs for safe joins
    - Preparing data for funnel analysis and insights

- **output video Video (Google Drive)**  
  - A short walkthrough showing:
    - The project setup
    - Key data cleaning steps
    - The final outputs and explanations

---

## 🧹 What the Code Does

1. **Loads data** from three sources:
   - Customers
   - Orders
   - Events

2. **Cleans and prepares the data**:
   - Converts date columns to proper `datetime` format
   - Removes duplicate records
   - Filters orders to keep only `order_status = "Valid"`
   - Standardizes ID columns as strings to avoid formatting issues

3. **Prepares the data for analysis**:
   - Makes datasets safe for joins
   - Sets up the base for funnel metrics and customer insights

---

## 🔢 Funnel Logic (Concept)

- **Users with events** = unique users who triggered at least one event  
- **Users who ordered** = unique customers who placed at least one valid order  
- **Conversion rate** = Users who ordered ÷ Users with events  

This shows how user engagement translates into actual purchases.

---

## ⚠️ Assumptions

- Only orders with `order_status = "Valid"` are considered  
- `net_sales` is treated as the final sale value  
- `user_id` and `customer_id` are assumed to belong to the same ID space for funnel analysis  
- All ID columns are treated as text to avoid precision and formatting issues  
- The provided data is assumed to be correct for the given time period  

---

## 🛠 Tools Used

- Python  
- Pandas  

---

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install pandas
