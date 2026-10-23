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

# missing and duplicates

print("missing values:",df.isna().sum()["amount"],
     "|Duplicated:",df.duplicated().sum())