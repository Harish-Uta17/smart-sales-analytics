from sqlalchemy import create_engine # type: ignore
import pandas as pd

engine = create_engine("postgresql+psycopg2://postgres:9913933238@localhost/demo")

sales = pd.read_sql("SELECT * FROM sales", engine)
products = pd.read_sql("SELECT * FROM products", engine)
customers = pd.read_sql("SELECT * FROM customers", engine)

print(sales.head())
print(products.head())
print(customers.head())
