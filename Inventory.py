# Variables
inventory = {'Coca Cola':       [2.00, 5], 
             'Snickers':        [1.50, 0], 
             'Bag of Chips':    [1.25, 7],
             'Water':           [1.00, 3]}

# Functions
def print_inventory():
    count = 1
    for key, value in inventory.items():
        print(f"{count}. {key} ({value[0]}) - {value[1]} left")
        count += 1