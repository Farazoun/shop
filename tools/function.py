from traceback import print_tb

import pandas as pd

df = pd.read_csv('../database/warehouse.csv')


def show_products(df):
    print("Id | Name    | Price")
    print("---------------------")
    for index, row in df.iterrows():
        print(f"{row['id']} | {row['name']:<7}   | {row['price']}")


cart = []


def add_to_cart(warehouse: pd.DataFrame, shoplist: pd.DataFrame, product: str) -> pd.DataFrame:
    '''
    this functions use for adding prodouct to shoping list
    '''
    show_products(df)
    status = False
    if product in warehouse['name'].values:
        status = True
    if status:
        new_row = {'name': product}
        shoplist.loc[len(shoplist)] = new_row
    show_products(df)

    return shoplist


def remove_from_cart(shoplist: pd.DataFrame, product: str) -> pd.DataFrame:
    '''
        this functions use for removing prodouct from shoping list
    '''
    show_products(df)
    status = False
    if product in shoplist['name'].values:
        status = True
    if status:
        shoplist[shoplist['name'] != product]
    show_products(df)

    return shoplist


def rearrange_cart(shoplist: pd.DataFrame, product: str, product2: str) -> pd.DataFrame:
    '''
            this functions use for rearrange prodouct from shoping list
    '''
    show_products(df)
    if product in shoplist['name'].values and product2 in shoplist['name'].values:
        index1 = shoplist[shoplist['name'] == product].index[0]
        index2 = shoplist[shoplist['name'] == product2].index[0]

        shoplist.iloc[[index1, index2]] = shoplist.iloc[[index2, index1]].values
    show_products(df)

    return shoplist

# -------------------------------------------------------
# shop_list = []
# data = {'name': ['Ali', 'Sara', 'Reza']}
# df = pd.DataFrame(data)
# df2 = pd.read_csv('../database/warehouse.csv')
# shop=add_to_cart(df2,df,'faraz')
# shop=add_to_cart(df2,shop,'faraz')
# print(shop)
# -----------------------------------------------------------


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
