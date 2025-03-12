import pandas as pd
# لیست محصولات پیشفرض

products = [
    {"id": 1, "name": "Bread", "price": 5000},
    {"id": 2, "name": "Milk", "price": 15000},
    {"id": 3, "name": "Eggs", "price": 30000},
    {"id": 4, "name": "Cheese", "price": 25000}
]

# سبد خرید کاربر
df = pd.DataFrame(products)
print(df)
cart = []