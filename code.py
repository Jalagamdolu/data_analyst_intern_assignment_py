import pandas as pd

# ----------------------
# Load data
# ----------------------
cx = pd.read_csv("cx_data.csv")                 # customers data
orders = pd.read_csv("orders_data.csv")         # orders data
events = pd.read_csv("Engagemnet metrics.csv")  # events data

# ----------------------
# Basic standardization
# ----------------------
# Strip column names (defensive)
cx.columns = cx.columns.str.strip()
orders.columns = orders.columns.str.strip()
events.columns = events.columns.str.strip()

# 1) Convert date fields to proper datetime
orders["order_date"] = pd.to_datetime(
    orders["order_date"], format="%d-%m-%Y %H:%M", errors="coerce"
)
events["event_date"] = pd.to_datetime(
    events["event_date"].astype(str), format="%Y%m%d", errors="coerce"
)
cx["registered_date"] = pd.to_datetime(
    cx["registered_date"], format="%d-%m-%Y %H:%M", errors="coerce"
)

# 2) Remove duplicate records
orders = orders.drop_duplicates()
events = events.drop_duplicates()
cx = cx.drop_duplicates()

# 3) Filter only valid orders (case-insensitive)
orders_valid = orders[orders["order_status"].str.lower() == "valid"].copy()

# 4) Ensure IDs are consistent (keep as strings for safe joins)
orders_valid["customer_id"] = orders_valid["customer_id"].astype(str)
cx["customer_id"] = cx["customer_id"].astype(str)
events["user_id"] = events["user_id"].astype(str)

# ASSUMPTION for funnel: user_id ≈ customer_id (same ID space)
