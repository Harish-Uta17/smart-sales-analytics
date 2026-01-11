import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

engine = create_engine(st.secrets["DB_URL"])

customers = pd.DataFrame({
    "customer_id":[1,2,3],
    "name":["Rahul","Anita","Suresh"],
    "city":["Bangalore","Hyderabad","Chennai"],
    "age":[22,24,27]
})

products = pd.DataFrame({
    "product_id":[101,102,103],
    "product_name":["Laptop","Mobile","Headphones"],
    "categoty":["Electronics","Electronics","Accessories"],
    "price":[50000,30000,3000]
})

sales = pd.DataFrame({
    "customer_id":[1,2,3,1,2],
    "product_id":[101,102,103,102,101],
    "quantity":[1,2,3,1,2],
    "sale_date":["2024-01-10","2024-01-12","2024-02-05","2024-02-20","2024-03-01"]
})

customers.to_sql("customers",engine,if_exists="append",index=False)
products.to_sql("products",engine,if_exists="append",index=False)
sales.to_sql("sales",engine,if_exists="append",index=False)

print("DATA INSERTED INTO SUPABASE SUCCESSFULLY")
