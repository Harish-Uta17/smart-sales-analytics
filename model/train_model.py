import pandas as pd
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
import joblib

engine = create_engine("postgresql+psycopg2://postgres:9913933238@localhost/demo")

# Load data
df = pd.read_sql("""
SELECT sale_date, quantity, price
FROM sales s JOIN products p ON s.product_id=p.product_id
""", engine)

# Feature Engineering
df['month'] = pd.to_datetime(df['sale_date']).dt.month
df['revenue'] = df['quantity'] * df['price']

X = df[['month']]
y = df['revenue']

# Train model
model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model/revenue_model.pkl")
print("MODEL TRAINED & SAVED ✅")
