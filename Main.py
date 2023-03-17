# Imports
import Inventory
import User_input

# Functions
def main():
    print("Welcome to the Vending Machine!")
    
    m = float(User_input.get_money())
    print("\n")
    
    print("Here is a list of items you can purchase:")
    print('\n')
    
    invo = Inventory.print_inventory()
    print("\n")
    
    while True:
        user_choice = User_input.choice() - 1
        item_list = list(Inventory.inventory.keys())
        value_list = list(Inventory.inventory.values())

        selected_item = item_list[user_choice]
        selected_item_price = value_list[user_choice][0]
        selected_item_stock = value_list[user_choice][1]

        if selected_item_stock > 0:
            print(f'You have selected a {selected_item}. The price is ${selected_item_price}.')
            break
        else:
            print("Out of stock, try again.")
    print("\n")
    
    price = Inventory.inventory[][0]

    if m > price:
        print(f'You have inserted ${m}. Your change is ${m - selected_item_price}.')
    else:
        print(f'The item is {selected_item_price}! You put in {m}')
    print("\n")

    # print("Thank you for your purchase! Enjoy your Snickers Bar!")

# Code
main()