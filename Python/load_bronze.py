# %%
# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import psycopg2

# %%


# Set the path to the file you'd like to load
file_path = "amazon_sales_dataset.csv"

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "aliiihussain/amazon-sales-dataset",
  file_path,
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. See the 
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

print("First 5 records:", df.head())

# %%
df.head()

# %%
conn = psycopg2.connect(
    host="localhost",
    database= "postgres",
    user="postgres",
    password="postgres1234"
)

# %%
cursor = conn.cursor()

# %%
cursor.execute("TRUNCATE TABLE bronze.amazon_sale")


# %%
columns_list = df.columns.tolist()

# %%
columns_str = ", ".join(columns_list)
placeholders = ", ".join(["%s"] * len(columns_list))

# %%
for index, row in df.iterrows():
    cursor.execute(
        f"INSERT INTO bronze.amazon_sale ({columns_str}) VALUES ({placeholders})",
        tuple(row)
    )

# %%
conn.commit()
cursor.close()
conn.close()
