import pandas as pd


def menu():
    print("1: Show products")
    print("2: Add to cart")
    print("3: Remove from cart")
    print("4: Rearrange cart")
    print("5: Show cart")
    print("6: Edit product quantity")
    print("0: Exit")


def show(df):
    df_to_show = df.copy()
    df_to_show.loc[:, 'id'] = range(1, len(df_to_show) + 1)

    columns = df_to_show.columns.tolist()
    columns = ['id'] + [col for col in columns if col != 'id']

    column_widths = {
        col: max(df_to_show[col].astype(str).apply(len).max(), len(col))
        for col in columns
    }

    header = " | ".join([f"{col:<{column_widths[col]}}" for col in columns])
    print(header)
    print("-" * len(header))

    for _, row in df_to_show.iterrows():
        row_data = " | ".join([f"{str(row[col]):<{column_widths[col]}}" for col in columns])
        print(row_data)

    if 'total' in df_to_show.columns:
        print(f"Your total is: {df_to_show['total'].sum()}")
    print()


def add_to_cart(warehouse: pd.DataFrame, shoplist: pd.DataFrame, product: str, quantity: int = 0) -> pd.DataFrame:
    product_lower = product.lower()

    if product_lower in warehouse['name'].str.lower().values:
        price = warehouse.loc[warehouse['name'].str.lower() == product_lower, 'price'].values[0]

        if product_lower in shoplist['name'].str.lower().values:
            print("This product is already in the cart. Updating quantity...")
            existing_index = shoplist[shoplist['name'].str.lower() == product_lower].index[0]
            current_quantity = shoplist.loc[existing_index, 'quantity']
            shoplist.loc[existing_index, 'quantity'] = current_quantity + quantity
        else:
            new_row = {
                'name': product,
                'quantity': quantity,
                'price': price
            }
            shoplist = pd.concat([shoplist, pd.DataFrame([new_row])], ignore_index=True)

        shoplist.to_csv('database/cart.csv', index=False)
    else:
        print("Product not found in warehouse!")

    return shoplist


def remove_from_cart(shoplist: pd.DataFrame, product: str) -> pd.DataFrame:
    product_lower = product.lower()
    if product_lower in shoplist['name'].str.lower().values:
        shoplist = shoplist[shoplist['name'].str.lower() != product_lower]
        shoplist.to_csv('database/cart.csv', index=False)
        print(f"{product} removed from cart.")
    else:
        print(f"{product} not found in cart.")
    return shoplist


def edit_cart(shoplist: pd.DataFrame) -> pd.DataFrame:
    product = input("Enter the product name to edit quantity: ").lower()

    if product not in shoplist['name'].str.lower().values:
        print(f"Product '{product}' not found in cart!")
        return shoplist

    index = shoplist[shoplist['name'].str.lower() == product].index[0]
    current_quantity = shoplist.loc[index, 'quantity']
    print(f"Current quantity of {shoplist.loc[index, 'name']}: {current_quantity}")

    try:
        new_quantity = int(input("Enter new quantity: "))
        if new_quantity <= 0:
            print("Quantity must be greater than 0!")
            return shoplist

        shoplist.loc[index, 'quantity'] = new_quantity
        shoplist = add_total_column(shoplist)
        shoplist.to_csv('database/cart.csv', index=False)
        print("✅ Quantity updated successfully!")

    except ValueError:
        print("Invalid quantity! Please enter a number.")

    return shoplist


def rearrange_cart(shoplist: pd.DataFrame, product: str, product2: str) -> pd.DataFrame:
    p1_lower = product.lower()
    p2_lower = product2.lower()

    if p1_lower in shoplist['name'].str.lower().values and p2_lower in shoplist['name'].str.lower().values:
        index1 = shoplist[shoplist['name'].str.lower() == p1_lower].index[0]
        index2 = shoplist[shoplist['name'].str.lower() == p2_lower].index[0]

        shoplist.iloc[[index1, index2]] = shoplist.iloc[[index2, index1]].values
        shoplist.to_csv('database/cart.csv', index=False)
        print(f"{product} and {product2} rearranged in cart.")
    else:
        print("One or both products not found in cart.")
    return shoplist


def exit_program(cart_path='database/cart.csv'):
    try:
        shoplist = pd.read_csv(cart_path)
        shoplist = shoplist.iloc[0:0]
        shoplist.to_csv(cart_path, index=False)
        print("✅ Cart reset!")
    except Exception as e:
        print(f" An error occurred while clearing the cart: {e}")
    print(" Exiting the program...")
    exit()


def add_total_column(shoplist: pd.DataFrame) -> pd.DataFrame:
    if 'price' in shoplist.columns and 'quantity' in shoplist.columns:
        shoplist['total'] = shoplist['price'] * shoplist['quantity']
        shoplist.to_csv('database/cart.csv', index=False)
    else:
        print("Error: 'price' or 'quantity' column not found in cart.")

    return shoplist


def auth_system():
    # بارگذاری اولیه کاربران
    users = pd.read_csv('database/users.csv')
    all_usernames = users['username'].tolist()
    all_passwords = users['password'].tolist()

    print("Welcome to the system!")

    while True:
        print("1: Sign In")
        print("2: Sign Up")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")

            # بارگذاری مجدد کاربران برای اطمینان از به‌روزرسانی
            users = pd.read_csv('database/users.csv')
            all_usernames = users['username'].tolist()
            all_passwords = users['password'].tolist()

            if username in all_usernames:
                index = all_usernames.index(username)
                if all_passwords[index] == password:
                    print("Login successful!")
                    return True
            print("Invalid username or password. Please try again.")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")

            # بررسی وجود کاربر
            users = pd.read_csv('database/users.csv')
            if username in users['username'].values:
                print(f"Username {username} already exists. Please try again.")
                continue

            # افزودن کاربر جدید
            new_user = pd.DataFrame({'username': [username], 'password': [password]})
            users = pd.concat([users, new_user], ignore_index=True)
            users.to_csv('database/users.csv', index=False)
            print(f"User {username} registered successfully! Please sign in now.")

            # به‌روزرسانی لیست‌ها
            all_usernames = users['username'].tolist()
            all_passwords = users['password'].tolist()

        else:
            print("Invalid choice. Please try again.")


def start_shopping():
    warehouse = pd.read_csv('database/warehouse.csv')
    shoplist = pd.read_csv('database/cart.csv')

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            show(warehouse)
        elif choice == "2":
            product = input("Enter the product you want to add: ")
            quantity = int(input("Enter quantity: "))
            shoplist = add_to_cart(warehouse, shoplist, product, quantity)
        elif choice == "3":
            product = input("Enter the product you want to remove: ")
            shoplist = remove_from_cart(shoplist, product)
        elif choice == "4":
            product = input("Enter the first product to rearrange: ")
            product2 = input("Enter the second product to rearrange: ")
            shoplist = rearrange_cart(shoplist, product, product2)
        elif choice == "5":
            show(shoplist)
        elif choice == "6":
            print("Signing out...")
            break
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice. Please try again.")


def main():
    # First, let the user sign in or sign up
    if auth_system():
        # If sign in is successful, start shopping
        start_shopping()


if __name__ == "__main__":
    main()
