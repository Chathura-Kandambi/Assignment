import pandas as pd
from pymongo import MongoClient


client = MongoClient("mongodb+srv://chathurakandambi47:F7WiXRAA8fsrZ5yk@chathura.ibge8.mongodb.net/product_data?retryWrites=true&w=majority")  # Replace with your connection string
db = client["product_data"]
collection = db["products"]


data = list(collection.find())  
df = pd.DataFrame(data)  


if 'Quantity' in df.columns and 'Price_per_Unit' in df.columns:
    df['profit'] = df['Quantity'] * df['Price_per_Unit']
else:
    print("Required columns 'Quantity' and 'Price_per_Unit' not found in the data.")


most_sold_products = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print("Most Sold Products:")
print(most_sold_products.head())  # Show top 5 products


most_used_payment_method = df["Payment_Method"].value_counts().idxmax()
print(f"Most Used Payment Method: {most_used_payment_method}")


if 'profit' in df.columns:
    most_profitable_category = df.groupby("Category")["profit"].sum().sort_values(ascending=False)
    print("Most Profitable Product Categories:")
    print(most_profitable_category.head())  # Show top 5 categories
else:
    print("Profit column is missing. Ensure 'Quantity' and 'Price_per_Unit' columns exist to calculate profit.")
