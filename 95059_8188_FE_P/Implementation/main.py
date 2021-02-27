# Made by Dante Fernando February 2021
# https://github.com/dantefernando/NEA2021


"""

TODO LIST:
--------------------------------------------------

- Allow the user to add, amend and delete menu items, and save menu changes

- Allow the menu to be saved to a file

--------------------------------------------------

- Calculate the total cost of the order

- Provide options to display the menu and running totals

- Display the order details for printing

- Loop for input of the next order
--------------------------------------------------

- When printing the menu, display when the file was made/last modified

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


# Allows user to delete menu items
def delete_menu_items():
    pass


# Allows user to edit menu items
def edit_menu_items(menu_file):
    pass
    # max_index = len(menu_file)  # The highest index out of all the items on the menu list 


# Allows user to add menu items to the menu
def add_menu_items(menu_file):

    # User inputs category for new item 
    categories = ["breakfast", "mains", "extras", "drinks"]
    print("-" * 30)
    while True:
        print("Please choose the menu category of your new menu item:\n"
              "Categories to choose from: Breakfast, Mains, Extras and drinks\n")
        while True:
            category = input("Your category: ").lower()
            if not category in categories:
                print("Please enter a valid category, try again.\n")
            else:
                break

        # User inputs name for new item
        print("-" * 30)
        print("Please choose the name of your new menu item.\n")
        while True:
            name = input("Name of new menu item: ")
            if not name.isalpha():
                print("Name must contain alphabetic characters only, try again.\n")
            else:
                break

        # User inputs price for new item
        print("-" * 30)
        print("Please choose the price of your new menu item.\n")
        while True:
            try:
                price_unrounded = float(input("Price of new menu item: $"))
                price = round(price_unrounded,2)  # Total price stored as a float 
                break
            except ValueError:
                print("Please input numeric characters only, try again.\n")
        price = str(price)
        if price[-2] == ".":
            price += "0"

        # Takes all categories in menu.txt and only
        # stores the category in an array: 'categories_in_file'
        categories_in_file = []
        for element in menu_file:  # Iterates over each element in menu.txt
            categories_in_file.append(element[3])

        # Finds how many of 'category' is in 'categories_in_file'
        # and stores it in variable: 'categories_present'
        # Along with how what their specific indexes are on
        # the menu in the 'categories_present_index' variable
        categories_present = 0
        categories_present_index = []
        for index, category_tmp in enumerate(categories_in_file):
            if category_tmp == category:
                categories_present += 1
                categories_present_index.append(int(index+1))

        start_line = min(categories_present_index)  # Assigns min index value
        final_line = max(categories_present_index)  # Assigns max index value
        print("-" * 30)
        print_menu(menu_file, start_line=start_line, final_line=final_line)

        # Get new item's index from user and insert it into the menu file
        print("What index would you like to assign to your new menu item?\n"
              f"Please note that items shown above are for the {category} category. "
              f"Choose an index between {start_line} and {final_line}. "
              )
        while True:
            try:
                new_index = int(input("Your new menu item index: "))
                break
            except ValueError:
                print("Your index must contain only numeric characters only, try again.")

        # Formatting the new menu item for it to be written to menu.txt
        new_item = [f'{new_index}', f"{price}", f"{name}", f"{category}"]

        # Adds 1 to the existing menu items' indexes
        for index, el in enumerate(menu_file, start=1):
            if index >= new_index:
                el_index = int(el[0])
                el_index += 1
                el[0] = str(el_index)
        menu_file.insert(new_index-1, new_item)

        # TODO: write menu_file to menu.txt

# Provides menu interface for user to choose to Add, edit or delete menu items
def editing_main_menu(menu_file):  # Credits to github.com/RoyceLWC for Menu. 
    print("\n-------Edit Menu Items--------")
    menu = {
        "1": [": Add menu items", add_menu_items],
        "2": [": Edit an existing menu item", edit_menu_items],
        "3": [": Delete menu items", delete_menu_items],
        "4": [": Exit to main menu"]
    }

    # Prints each menu index and its corresponding functions description
    for key in sorted(menu.keys()):
        print(key + menu[key][0])

    while True:  # Loop until a valid index is received
        print("-" * 30)
        index = input("Select an index: ")
        try:  # Try to convert to an integer
            index = int(index)  # Converts to an integer
            if 1 <= index <= 4:  # In range
                break
            else:  # Out of range
                print("Out of range try again!")
        except ValueError:  # If it can't be converted to an integer
            print("Invalid index")
    print("-" * 30)
    if index == 1:  # add_menu_items
        menu[str(index)][1](menu_file)
    elif index == 2:  # edit_menu_items
        menu[str(index)][1](menu_file)
    elif index == 3:  # delete_menu_items
        menu[str(index)][1](menu_file)


# Writes running totals to running_totals.txt
def write_order(total_price, total_quantity, quantity_dict, table_num):
    with open("running_totals.txt", "w") as file:  # Creates the file and writes default menu
        file.write(f"{total_price}\n")
        file.write(f"{total_quantity}\n")
        # file.write(f"{quantity_dict}\n")
        # file.write(f"{table_num}")


# Displays the current order with the quantities of each menu item.
def display_order(total_price, total_quantity, quantity_dict, table_num):

    # By default the price doesn't display all 2 decimal points.
    # E.g. a price of "$2.50" would only display "$2.5"
    # These 3 lines below fix this issue.
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


# Generates a dictionary of how many of each item has been ordered in a simple dict format.
def get_quantity(names):
    elements_dict = dict()
    for elem in names:  # Iterate over each element in list 
        if elem in elements_dict:  # If element exists add 1 to value else stay at one
            elements_dict[elem] += 1
        else:
            elements_dict[elem] = 1
    elements_dict = { key:value for key, value in elements_dict.items()}
    return elements_dict


# Calculates quantity and cost totals
def get_totals(full_order):
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


# Checks order with menu in "menu.txt" and generates 'full_order' var
def get_order(data, menu_file):
    full_order = []
    table_num = f"Table #{data[0]}"
    full_order.append(table_num)
    tmp_order = ""
    for i in range(1, len(data)):  # iterates over order input (data) except for table num.
        menu_num = data[i]  # set the menu_num to i (any number greater than index: 0)
        for menu_item in menu_file:  # Searches for index num in menu_file
            if menu_item[0] == menu_num:
                tmp_order = menu_item
                full_order.append(tmp_order)
                break
    # The 'full_order' var consists of the table num at 0 and each element 
    # contains the each order's line in menu.txt one by one.

    total_price, total_quantity, quantity_dict = get_totals(full_order)  # Calculates quantity and cost totals.
    display_order(total_price, total_quantity, quantity_dict, table_num)
    write_order(total_price, total_quantity, quantity_dict, table_num)
    return total_price, total_quantity, quantity_dict, table_num


# Takes menu.txt from the "menu_file" var and prints it to user 
def print_menu(menu_file, **kwargs):
    items = []
    for element in menu_file:  # Takes menu_file items and strips them of the category e.g. "breakfast"
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

    # Sets values using kwargs to determine
    # which specfic lines to iterate over
    start_line = kwargs.get("start_line")
    final_line = kwargs.get("final_line")

    # Print if no kwargs are provided
    if start_line == None and final_line == None:
        for item in real_output:
            print(f"\n{item}")  # Prints all menu items formatted with perfect amount of periods.
        print("\n")

    # kwargs are provided (start_line and final_line)
    else:
        for index, item in enumerate(real_output):
            if start_line <= index+1 <= final_line:  # Index is in correct printing range
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
    # data variable is input data in array format.
    total_price, total_quantity, quantity_dict, table_num = get_order(data, menu_file)
    return total_price, total_quantity, quantity_dict, table_num


# Main Menu, first menu that the user sees.
def main_menu(menu_file):   # Credits to github.com/RoyceLWC for Menu. 
    hasData = False
    while True:
        print("\n----------Main Menu-----------")
        menu = {
            "1": [": Input order data", get_order_input],
            "2": [": Change Menu Items", editing_main_menu],
            "3": [": Finalize Order", finalize_order]
        }

        # Prints each menu index and its corresponding functions description
        for key in sorted(menu.keys()):
            print(key + menu[key][0])

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
        if index == 1:  # Get all data about the order, e.g. price, quantity and table num.
            total_price, total_quantity, quantity_dict, table_num = menu[str(index)][1](menu_file)
            hasData = True
        elif index == 2:  # change_menu_items
            menu[str(index)][1](menu_file)
        else:
            menu[str(index)][1](total_price, total_quantity, quantity_dict, table_num, hasData)


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

