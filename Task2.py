import pandas as pd
from pathlib import Path
file_path = Path("orders.csv")
data = """order_id,customer_id,amount
1,101,500
2,102,
3,101,700
3,101,700
4,103,300
5,104,900"""
file_path.write_text(data)
df = pd.read_csv(file_path)
print("Missing:", df.isna().sum()["amount"],
      "| Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()
df["amount"] = pd.to_numeric(df["amount"])
median_value = df["amount"].median()
df["amount"] = df["amount"].fillna(median_value)

print("Median used:", median_value)
df["order_id"] = df["order_id"].astype(str)
result = df.groupby("customer_id").agg(
    total=("amount", "sum"),
    orders=("order_id", "count")
)

print(result)
import pandas as pd


data = """customer_id,name,city
101,Arun,Chennai
102,Priya,Mumbai
103,Rahul,Chennai
105,Divya,Bangalore
"""
with open("customers.csv", "w") as file:
    file.write(data)
orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")
orders = orders.drop_duplicates()
orders["amount"] = orders["amount"].fillna(
    orders["amount"].median()
)
inner = pd.merge(
    orders, customers,
    on="customer_id",
    how="inner"
)

print("Inner join rows:", len(inner))
print(inner)
left = pd.merge(
    customers, orders,
    on="customer_id",
    how="left"
)
no_orders = left[left["order_id"].isna()]

print("\nCustomers with no orders:")
print(no_orders[["customer_id", "name"]])
outer = pd.merge(
    orders, customers,
    on="customer_id",
    how="outer",
    indicator=True
)

unmatched_orders = outer[outer["_merge"] == "left_only"]

print("\nOrders without customer records:")
print(unmatched_orders[["order_id", "customer_id", "amount"]])
january_data = """order_id,customer_id,amount
1,101,500
2,102,600
3,101,700
4,103,300
"""

february_data = """order_id,customer_id,amount
5,104,900
6,102,400
7,103,500
8,101,200
"""
with open("january.csv", "w") as f:
    f.write(january_data)

with open("february.csv", "w") as f:
    f.write(february_data)

january = pd.read_csv("january.csv")
february = pd.read_csv("february.csv")
all_orders = pd.concat(
    [january, february],
    ignore_index=True
)
all_orders = all_orders.drop_duplicates()
all_orders["amount"] = all_orders["amount"].fillna(
    all_orders["amount"].median()
)
result = all_orders.groupby("customer_id").agg(
    total=("amount", "sum"),
    orders=("order_id", "count")
)

print(result)


