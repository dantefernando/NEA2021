# Made by Dante Fernando February 2021
# https://github.com/dantefernando/NEA2021


from decimal import Decimal


"""

TODO LIST:
- Save the running totals to a file

--------------------------------------------------

- Allow the user to add, amend and delete menu items, and save menu changes

- Allow the menu to be saved to a file

--------------------------------------------------

- Calculate the total cost of the order

- Provide options to display the menu and running totals

- Display the order details for printing

- Loop for input of the next order
--------------------------------------------------

"""

default_menu = ["1,5.50,All day (large),breakfast",
                "2,3.50,All day (small),breakfast",
                "3,3.00,Hot dog,mains",
                "4,4.00,Burger,mains",
                "5,4.25,Cheese burger,mains",
                "6,3.50,Chicken goujons,mains",
                "7,1.75,Fries,extras",
                "8,2.20,Salad,extras",
                "9,2.20,Milkshake,drinks",
                "10,1.30,Soft drinks,drinks",
                "11,0.90,Still water,drinks",
                "12,0.90,Sparkling water,drinks"]


def finalize_order():
    pass


def change_menu_items():
    pass


# Displays the current order with the quantities of each menu item.
def display_order(total_price, total_quantity, quantity_dict, table_num):
    # By default the price doesn't display all 2 decimal points.
    # E.g. a price of "$2.50" would only display "$2.5"
    # These 3 lines below aim to fix this issue.
    total_price = str(total_price)
    if total_price[-2] == ".":
        total_price += "0"

    print("-" * 30)
    print(f"\nYour order for {table_num}: \n")
    for key, value in quantity_dict.items():
        print(key , ' == ', value)
    print(f"\nTotal Price = ${total_price}")
    print(f"Total Quantity of items ordered = {total_quantity}\n")
    print("-" * 30)
    print("\n")


def get_quantity(names):
    elements_dict = dict()
    for elem in names:  # Iterate over each element in list 
        if elem in elements_dict:  # If element exists add 1 to value else stay at one
            elements_dict[elem] += 1
        else:
            elements_dict[elem] = 1
    elements_dict = { key:value for key, value in elements_dict.items()}
    return elements_dict


def get_totals(full_order):  # Calculates quantity and cost totals
    prices = []
    for index in range(1, len(full_order)):
        item = full_order[index]  # Gets the Full item information
        price = item[1]  # Gets the price only
        prices.append(float(price))  # Converts the string price into a float and adds to prices. 
    total_price_tmp = 0
    for price in prices:  # Adds up the prices together
        total_price_tmp += price  # **total price currently**
    total_price = round(total_price_tmp,2)  # Total price stored as a float 

    names = []
    for index in range(1, len(full_order)):
        item = full_order[index]  # Gets the Full item information
        name = item[2]  # Gets name only of full item
        names.append(name)
    total_quantity = 0
    quantity_dict = get_quantity(names)
    for key, value in quantity_dict.items():
        total_quantity += value  # **total quantity currently**
    return total_price, total_quantity, quantity_dict


def get_order(data, menu_file):  # Checks order with the existing menu list stored in "menu.txt"
    full_order = []
    table_num = f"Table #{data[0]}"
    full_order.append(table_num)
    tmp_order = ""
    for i in range(1, len(data)):  # iterates over order input except for table num.
        menu_num = data[i]  # set the menu_num to i (any number greater than index: 0)
        for menu_item in menu_file:  # Searches for index num in menu_file
            if menu_item[0] == menu_num:
                tmp_order = menu_item
                full_order.append(tmp_order)
                break
    total_price, total_quantity, quantity_dict = get_totals(full_order)  # Calculates quantity and cost totals.
    display_order(total_price, total_quantity, quantity_dict, table_num)


def print_menu(menu_file):
    items = []
    for element in menu_file:  # Takes menu_file items and strips them of the categoy e.g. "breakfast"
        tmp = []
        for index, el in enumerate(element):
            if not index == 3:
                tmp.append(el)
        items.append(tmp)

    tmp2 = []  # Finds which element in the array has the greatest amount of chars.
    for element in items:
        string = ""
        for el in element:
            string += el
        tmp2.append(string)
    max_len_el = max([len(i) for i in tmp2])
    max_len = max_len_el + 5

    real_output = []
    for element in menu_file:  # Formats each menu item with the right amount of periods "."
        number = element[0]
        price = element[1]
        name = element[2]
        full_item_tmp = f"{number}. {name} {price}"
        length_of_full = len(full_item_tmp)
        period_num = max_len - length_of_full
        periods = period_num * "."
        full_item = f"{number}. {name} {periods} {price}"
        real_output.append(full_item)
    for item in real_output:
        print(f"\n{item}")  # Prints all menu items formatted with perfect amount of periods.
    print("\n")


def get_order_input(menu_file):  # Validates Order 
    print_menu(menu_file)
    while True:
        print("-" * 30)
        print("\nE.g. \"6, 4, 4, 7, 8, 10, 10\""
              " Would be an order from Table 6 for 2 Burgers, 1 Fries, 1 Salad and 2 Soft"
              " Drinks.")
        data = input("\nType order here: ").split(",")
        tmp_last_item = menu_file[len(menu_file) -  1]  # Assigns Last entry's index
        last_item = tmp_last_item[0]                    # to "last_item"
        invalid = ""
        invalidTable = ""
        for index, element in enumerate(data):  # Takes each element in the array
            if index == 0:  # If the element is first (table number doesn't apply for these rules)
                if element.isnumeric() == False:
                    invalid = True  # ^If the digit length is greater than 10 is not integer
                elif int(element) > 10:  # If the element is numerically greater than number of tables in (10)
                    invalidTable = True
            else:
                if len(element) > len(last_item) or element.isnumeric() == False:
                    invalid = True  # ^If the digit length is greater than the digit length in the menu or is not integer
                elif int(element) > int(last_item):  # If the element is numerically greater than the last item
                    invalid = True
        if invalidTable:
            print("\nWe only have 10 tables! Table number must be lower than 10, please try again.")
        elif invalid:  # If there are letters or symbols in the input: 
            print("\nYour order has invalid characters, please try again.")
        elif len(data) == 1:
            print("\nAt least one order must be made per table, please try again.")
        else:
            break
    get_order(data, menu_file)
    print(data)


def main_menu(menu_file):  # Main Menu, first menu that the user sees.
    print("\n----------Main Menu-----------")
    menu = {
        "1": [": Input order data", get_order_input],
        "2": [": Change Menu Items", change_menu_items],
        "3": [": Finalize Order", finalize_order]
    }

    for key in sorted(menu.keys()):
        print(key + menu[key][0])  # Prints each menu index and its corresponding functions description

    while True:  # Loop until a valid index is received
        print("-" * 30)
        index = input("Select an index: ")
        try:  # Try to convert to an integer
            index = int(index)  # Converts to an integer
            if 1 <= index <= 3:  # In range
                break
            else:  # Out of range
                print("Out of range try again!")
        except ValueError:  # If it can't be converted to an integer
            print("Invalid index")
    data = ""
    print("-" * 30)
    if index == 1:  # Get Order data
        data = menu[str(index)][1](menu_file)
    elif index == 2:  # change_menu_items
        menu[str(index)][1]()
    else:
        menu[str(index)][1](data)


def check_file(default_menu):  # Checks for menu and Creates default_menu if doesn't exist.
    for i in range(2):  # Quick fix for the file not being read on first try idk.
        try:  # Check for existing file by trying to read the file
            with open("menu.txt", "r") as file:
                whole_file = file.readlines()  # Stores the menu in the file as "whole_file"
                menu_file = []
                for element in whole_file:
                    element = element.strip("\n")
                    element = element.split(",")
                    menu_file.append(element)
                file.close()
                return menu_file
        except IOError:  # If menu.txt is not found, make a new file
            with open("menu.txt", "w") as file:  # Creates the file and writes default menu
                for line in default_menu:
                    file.write(f"{line}\n")
                file.close()
            check_file(default_menu)


def main():
    menu_file = check_file(default_menu)  # Checks for menu and Creates default_menu if doesn't exist.
    main_menu(menu_file)


if __name__ == "__main__":
    main()

