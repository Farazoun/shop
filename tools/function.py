from traceback import print_tb

import pandas as pd

df = pd.read_csv('../database/products.csv')


def show_products(df):
    print("Id | Name    | Price")
    print("---------------------")
    for index, row in df.iterrows():
        print(f"{row['id']} | {row['name']:<7}   | {row['price']}")





show_products(df)






#     # نمایش لیست محصولات در قالب جدول
#     print("\nProduct List:")
#     print("+----+------------+---------+")
#     print("| ID |   Name     |  Price  |")
#     print("+----+------------+---------+")
#     for product in df:
#         print(f"| {product['id']:2} | {product['name']:10} | {product['price']:7} |")
#     print("+----+------------+---------+")
#
#
#
#     # نمایش سبد خرید با جزئیات
#     if not cart:
#         print("\nYour cart is empty!")
#         return
#
#     total = 0
#     print("\nYour Shopping Cart:")
#     print("+----+------------+---------+--------+---------+")
#     print("| ID |   Name     | Unit Price | Quantity |  Total  |")
#     print("+----+------------+---------+--------+---------+")
#     for index, item in enumerate(cart, 1):
#         item_total = item['price'] * item['quantity']
#         total += item_total
#         print(f"| {index:2} | {item['name']:10} | {item['price']:7} | {item['quantity']:6} | {item_total:7} |")
#     print("+----+------------+---------+--------+---------+")
#     print(f"Total Amount: {total} Tomans\n")
#
#
# def add_to_cart():
#     # اضافه کردن محصول به سبد خرید
#     show_products()
#     try:
#         product_id = int(input("Enter product ID: "))
#         quantity = int(input("Enter quantity: "))
#
#         # پیدا کردن محصول
#         product = next((p for p in products if p['id'] == product_id), None)
#         if product:
#             # بررسی وجود محصول در سبد
#             for item in cart:
#                 if item['id'] == product_id:
#                     item['quantity'] += quantity
#                     print("Quantity updated!")
#                     return
#
#             # اضافه کردن آیتم جدید
#             cart.append({
#                 'id': product['id'],
#                 'name': product['name'],
#                 'price': product['price'],
#                 'quantity': quantity
#             })
#             print("Product added to cart!")
#         else:
#             print("Product not found!")
#     except:
#         print("Invalid input!")
#
#
# def remove_from_cart():
#     # حذف آیتم از سبد خرید
#     if not cart:
#         print("Cart is already empty!")
#         return
#
#     show_cart()
#     try:
#         item_id = int(input("Enter cart item ID: ")) - 1
#         if 0 <= item_id < len(cart):
#             cart.pop(item_id)
#             print("Item removed!")
#         else:
#             print("Invalid ID!")
#     except:
#         print("Invalid input!")
#
#
# def rearrange_cart():
#     # تغییر ترتیب آیتم‌های سبد خرید
#     if not cart:
#         print("Cart is empty!")
#         return
#
#     show_cart()
#     try:
#         old_pos = int(input("Current item position: ")) - 1
#         new_pos = int(input("New item position: ")) - 1
#
#         if 0 <= old_pos < len(cart) and 0 <= new_pos < len(cart):
#             item = cart.pop(old_pos)
#             cart.insert(new_pos, item)
#             print("Cart rearranged!")
#         else:
#             print("Invalid positions!")
#     except:
#         print("Invalid input!")
