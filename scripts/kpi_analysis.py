import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:9913933238@localhost/demo")

query = """
SELECT 
    p.categoty,
    SUM(s.quantity * p.price) AS total_revenue,
    COUNT(DISTINCT s.customer_id) AS unique_customers
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.categoty;
"""

kpis = pd.read_sql(query, engine)
print("\n=== BUSINESS KPIs ===\n")
print(kpis)
