# main.py
import pandas as pd
from tools import (
    show,
    menu,
    add_to_cart,
    remove_from_cart,
    exit_program,
    rearrange_cart,
    add_total_column,
    auth_system,
    edit_cart
)

print("Welcome to Farazoun shop!")

warehouse_path = 'database/warehouse.csv'
cart_path = 'database/cart.csv'
user_path = 'database/users.csv'

def main():
    warehouse = pd.read_csv(warehouse_path)
    cart = pd.read_csv(cart_path)

    if auth_system():
        while True:
            menu()
            choice = input("Choose from menu (0-6): ")

            if choice == "1":
                show(warehouse)

            elif choice == "2":
                product = input("Enter the product you want to add: ")
                quantity = int(input("Enter the quantity: "))
                cart = add_to_cart(warehouse, cart, product, quantity)
                cart = add_total_column(cart)
                show(cart)

            elif choice == "3":
                show(cart)
                product = input("Enter the product you want to remove: ")
                cart = remove_from_cart(cart, product)
                show(cart)

            elif choice == "4":
                product = input("Enter product 1: ")
                product2 = input("Enter product 2: ")
                cart = rearrange_cart(cart, product, product2)
                show(cart)

            elif choice == "5":
                show(cart)

            elif choice == "6":
                cart = edit_cart(cart)
                show(cart)

            elif choice == "0":
                exit_program(cart_path)
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()