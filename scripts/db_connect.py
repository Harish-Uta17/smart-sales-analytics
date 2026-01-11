from sqlalchemy import create_engine # type: ignore
import pandas as pd

engine = create_engine("postgresql+psycopg2://postgres:9913933238@localhost/demo")

try:
    df = pd.read_sql("SELECT * FROM customers", engine)
    print("CONNECTED SUCCESSFULLY ✅")
    print(df)
except Exception as e:
    print("CONNECTION FAILED ❌")
    print(e)
