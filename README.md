## 🚀 Live Demo
👉 [https://smart-sales-analytics.streamlit.app](https://smart-sales-analytics-xbjhl3hehextqwpbdpv4qv.streamlit.app/)



# 📊 Smart Sales Analytics & Revenue Forecasting Platform

An end-to-end enterprise-grade sales analytics system that performs real-time business intelligence and machine-learning-based revenue forecasting using PostgreSQL, Python, SQL, and Streamlit.

This project simulates how real companies build internal analytics products for management-level decision making.

---

## 🚀 Key Features

### Business Analytics (BI)
- Monthly revenue trend analysis
- Category-wise revenue performance
- Customer segmentation by city
- Product-wise profitability analysis
- Executive KPI cards (Revenue, Customers, Categories)

### Machine Learning
- Revenue forecasting using Linear Regression
- Trained model saved and reused (.pkl)
- Interactive prediction via dashboard

### Interactive Dashboard
- Clean, professional UI
- Filters by city and product category
- Live database-driven analytics
- Web-based Streamlit application

---

## 🛠 Tech Stack
- Python 3.10+
- PostgreSQL
- SQLAlchemy
- Pandas
- scikit-learn
- Streamlit
- Git & GitHub

---

## 📁 Project Structure

Smart-Sales-Analytics/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── data/
│
├── scripts/
│   ├── db_connect.py
│   ├── load_data.py
│   └── kpi_analysis.py
│
├── model/
│   ├── train_model.py
│   ├── predict.py
│   └── revenue_model.pkl
│
└── .venv/

---

## 📋 Prerequisites
- Python 3.10+
- PostgreSQL 13+
- pip
- Git

---

## ⚙️ Installation & Setup

### Clone Repository
git clone https://github.com/yourusername/smart-sales-analytics.git
cd smart-sales-analytics

### Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate

### Install Dependencies
pip install -r requirements.txt

---

## 🗄 PostgreSQL Setup

CREATE DATABASE demo;

CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  name VARCHAR(50),
  city VARCHAR(50),
  age INT
);

CREATE TABLE products (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(50),
  categoty VARCHAR(50),
  price NUMERIC(10,2)
);

CREATE TABLE sales (
  sale_id SERIAL PRIMARY KEY,
  customer_id INT REFERENCES customers(customer_id),
  product_id INT REFERENCES products(product_id),
  quantity INT,
  sale_date DATE
);

---

## Load Sample Data
python scripts/load_data.py

---

## Train Model
python model/train_model.py

---

## Run Dashboard
streamlit run app.py

Open browser: http://localhost:8501

---

## License
MIT License

---

## Author
Harish Uta
