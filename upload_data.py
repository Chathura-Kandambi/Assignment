import pandas as pd
from pymongo import MongoClient


df = pd.read_csv("your_product_file.csv")  


client = MongoClient("mongodb+srv://chathurakandambi47:F7WiXRAA8fsrZ5yk@chathura.ibge8.mongodb.net/product_data?retryWrites=true&w=majority")
db = client["product_data"]
collection = db["products"]


data = df.to_dict(orient="records")  
collection.insert_many(data)

print("Data uploaded successfully!")

print("Column names in DataFrame:", df.columns)
print(df.head()) 

