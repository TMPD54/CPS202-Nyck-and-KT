
import Inventory

# Variables
price = 0

# Functions
def get_money():
    while True:
        try:
            m = float(input("Please enter the amount of money you have: $"))
            if m > 0:
                return m
            else:
                print("Please input a number greater than 0.")
        except ValueError:
            print("Please enter a number.")

def choice():
    while True:
        try:
            choice = int(input("Please select the item number you wish to purchase: "))
            if choice > 0 and choice < len(Inventory.inventory.keys()):
                return choice
            else:
                print("Please input a valid choice from the list.")
        except ValueError:
            print("Please enter a number.")