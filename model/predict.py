import joblib

model = joblib.load("model/revenue_model.pkl")

month = int(input("Enter month number (1-12): "))
prediction = model.predict([[month]])

print("Predicted Revenue:", round(prediction[0],2))
