# Made by Dante Fernando February 2021
# https://github.com/dantefernando/NEA2021


"""

TODO LIST:

~Order Section~

- Add confirmation when renaming the categories for edit_menu_items()

"""

# DEFAULT_MENU is used in check_file() upon running program for first time.

DEFAULT_MENU = ("1,5.50,All day (large),breakfast",
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
                "12,0.90,Sparkling water,drinks")


def finalize_order(total_price, total_quantity, quantity_dict, table_num, hasData):
    print("\n######## BEGIN PRINTING ########\n")
    print("TIMS DINER\n")
    print("\nFinal order:")
    display_order(total_price, total_quantity, quantity_dict, table_num)

    while True:
        print("- Enter \"Y\" to Exit and enter another order\n"
              "- Enter \"N\" to Exit and keep current order\n"
              "- Enter \"Q\" to Quit the program\n")
        inp = input("Your choice: ").lower()

        if inp == "y":  # user exits and enters another order

            # Resets all order values
            total_price = None
            total_quantity = None
            quantity_dict = None
            table_num = None
            hasData = False

            return total_price, total_quantity, quantity_dict, table_num, hasData

        elif inp == "n":  # User exits and keeps current order
            return total_price, total_quantity, quantity_dict, table_num, hasData

        elif inp == "q":  # User quits the program
            quit()

        else:  # User input is invalid 
            print("Please enter \"y\" or \"n\" as your choice, try again.\n")



def options(menu_file):  # Options menu for the whole program
    print("\n-------Options Menu--------")
    print("1: Reset Menu Items File\n"
          "2: Exit to Main Menu\n")
    while True:  # Validates user input choice
        try:
            inp = int(input("Your Choice: "))
            if inp == 1:  # inp==1 | User attempts reset of file
                print("Are you sure you want to reset the Menu Items File? (menu.txt)?\n"
                      "This will erase all saved changes to the file and reset it to\n"
                      "defaults.\n\n"
                      "- Enter \"Y\" to CONFIRM MENU RESET\n"
                      "- Enter \"N\" to DISCARD CHANGES AND EXIT\n")

                while True:  # Validates input for Reset or Exit
                    choiceInp = input("Your choice: ").lower()

                    if choiceInp == "y":  # User wants to reset
                        with open("menu.txt", "w") as file:  # Creates the file and writes default menu
                            for line in DEFAULT_MENU:
                                file.write(f"{line}\n")
                        with open("menu.txt", "r") as file:
                            whole_file = file.readlines()  # Stores the menu in the file as "whole_file"
                            menu_file = []
                            for element in whole_file:
                                element = element.strip("\n")
                                element = element.split(",")
                                menu_file.append(element)

                        print("File reset!\n")
                        return menu_file

                    elif choiceInp == "n":  # User wants to exit 
                        break
                    else:
                        print("Please enter \"y\" or \"n\" as your choice, try again.\n")

                if choiceInp == "n":  # User exits instead of resetting
                    print("Exiting...\n")
                    break
            elif inp == 2:  # inp==2 | User Exits
                print("Exiting...\n")
                break
            else:  # Not valid
                print("Please enter 1 or 2 as your choice.\n")
        except ValueError:  # User doesn't input numeric characters
            print("Please enter numeric characters only, try again.\n")
    return menu_file


# Allows user to delete menu items
def delete_menu_items(menu_file):
    while True:
        print("-" * 30)
        print("\nThis is the current menu:")
        print_menu(menu_file)

        # Asks the user what menu item index they want to delete
        print("Enter a menu item index to delete\n"
              "Or type \"E\" to exit.\n")

        while True:  # Checks if user input is in range for deletion or if the user wants to exit "delete_menu_items"
            try:
                inp = input("Your choice: ")
                int_inp = int(inp)  # Converts to type: integer

                tmp_last_item = menu_file[len(menu_file) - 1]
                last_item_index = int(tmp_last_item[0])
                delete_index = int_inp
                if delete_index > last_item_index or delete_index < 1:  # Out of range
                    print(f"Your delete index must be between: 1 and {last_item_index}\n"
                          "Please try again...\n")
                else:
                    break
            except ValueError:  # Input is not an integer
                if inp == "e":
                    break
                else:
                    print("Please enter numeric characters only, try again\n")

        if inp == "e":
            break

        # Assigns Last entry's index to "last_item"
        name = menu_file[delete_index-1][2]

        print(f"Are you sure you want to delete {name}?\n"
              "- Enter \"Y\" to Confirm Menu Item Deletion\n"
              "- Enter \"N\" to Discard Changes and Exit to Edit Menu\n")

        while True:  # Validates input for delete item or Exit
            choiceInp = input("Your choice: ").lower()

            if choiceInp == "y":  # User wants to delete the menu item
                # Deletes the menu item
                del menu_file[delete_index-1]

                # Corrects menu index numbers in the list 
                for index, full_item in enumerate(menu_file, start=1):
                    full_item[0] = str(index)

                print(f"{name} Deleted!")
                break

            elif choiceInp == "n":  # User wants to exit 
                break
            else:
                print("Please enter \"y\" or \"n\" as your choice, try again.\n")

        if choiceInp == "n":  # User exits instead of deleting menu item
            print("Exiting...\n")
            break


    return menu_file


    if inp == "e":  # Breaks the whole loop and exits to menu
        return menu_file


def write_menu(menu_file):
    with open("menu.txt", "w") as file:  # Creates the file and writes menu_file
        for line in menu_file:  # Iterates over each full item in menu item
            index_num = line[0]  # Assigns to index number
            price = line[1]  # Assigns to price
            name = line[2]  # Assigns to name
            category = line[3]  # Assigns to category 

            file.write(f"{index_num},{price},{name},{category}\n")


# Allows user to edit menu items
def edit_menu_items(menu_file):
    while True:
        print("-" * 30)
        print("\nThis is the current menu:")
        print_menu(menu_file)

        # Asks the user what menu item index they want to edit
        print("Enter a menu item index to edit\n"
              "Or type \"e\" to exit.\n"
              )
        while True:
            try:
                inp = input("Your choice: ")
                edit_index = int(inp)

                # Assigns Last entry's index to "last_item"
                tmp_last_item = menu_file[len(menu_file) - 1]
                last_item_index = int(tmp_last_item[0])
                if edit_index > last_item_index or edit_index < 1:  # Out of range
                    print(f"Your index must be between: 1 and {last_item_index}\n"
                          "Please try again...\n")
                else:  # Index is valid
                    break
            except ValueError:  # User entered input other than an integer
                if inp == "e":
                    break
                else:
                    print("Please enter numeric characters only, try again.\n")

        if inp == "e":  # Breaks the whole loop and exits to menu
            return menu_file

        # Loop for asking user what to edit of that item until they choose to exit.
        while True:
            print("-" * 30)
            # Prints only that element in the menu with the catergory
            print_menu(menu_file, start_line=edit_index, final_line=edit_index)

            current_name = menu_file[edit_index-1][2]
            print(f"Enter a letter from below to choose what to edit of {current_name}:\n"
                  "(I)ndex # of item\n"
                  "(N)ame of item\n"
                  "(P)rice\n"
                  "(C)ategory\n"
                  "Enter \"E\" to (E)xit and choose another item edit or exit.\n"
                  )
            while True:  # Validates input for choice
                inp = input("Your choice: ").lower()
                if inp == "i" or inp == "n" or inp == "p" or inp == "c" or inp == "e": # Valid input is received
                    break  # Breaks the loop
                else:
                    print("Your input must be either: \"I\", \"N\", \"P\" or \"C\". Try again!")

            if inp == "i":  # User wants to change index number
                print_menu(menu_file, start_line=edit_index, final_line=edit_index)

                print("Choose the menu item index number that you want it to change to: ")
                while True:  # Validates input for inputting index to change to 
                    try:
                        inp = int(input("Index Number: "))
                        # Assigns Last entry's index to "last_item"
                        tmp_last_item = menu_file[len(menu_file) - 1]
                        last_item_index = int(tmp_last_item[0])
                        if inp > last_item_index or inp < 1:  # Out of range
                            print(f"Your index must be between: 1 and {last_item_index}\n"
                                  "Please try again...\n")
                        else:  # Index is valid
                            break
                    except ValueError:  # User entered input other than an integer
                        print("Please enter numeric characters only, try again.\n")

                tmp_menu_item = menu_file[edit_index-1]  # Sets tmp to selected item 
                tmp_menu_item[3] = menu_file[inp-1][3]  # Sets tmp's category to item to be inserted above

                del menu_file[edit_index-1]  # deletes the old item
                menu_file.insert(inp-1, tmp_menu_item)  # Inserts the tmp menu item

                # Corrects the index numbers in the list
                for index, full_item in enumerate(menu_file, start=1):
                    full_item[0] = str(index)

                print(f"Index changed to {inp}.")

                edit_index = inp

            elif inp == "n":  # User wants to change name
                original = menu_file[edit_index-1][2]  # Sets original to current name for item
                print(f"Current name of item is: {original}")

                print("Please choose the name of your new menu item.\n")
                while True:  # Validates Name
                    name_tmp = input("Name of new menu item: ")

                    # Checks if name contains only letters and spaces
                    if name_tmp[-1] == " ":
                        print("Name must not contain spaces at the end!")
                    elif not all(letter.isalpha() or letter.isspace() for letter in name_tmp):
                        print("Name must contain alphabetic characters only, try again.\n")
                    else:
                        name = ""
                        words = name_tmp.split()  # Splits name_tmp into list
                        len_words = len(words)

                        # Takes each word in the string, formats
                        # and concatenates it to variable: "name"
                        for index, word in enumerate(words):
                            if index == 0:  # First word
                                word = word.title()  # Makes first letter capital
                                name += f"{word} "
                            elif index+1 == len_words:  # last word
                                name += word
                            else:  # Other words
                                name += f"{word} "
                        break

                menu_file[edit_index-1][2] = name
                print(f"Name changed to {name}")

            elif inp == "p":  # User wants to change price
                original = menu_file[edit_index-1][1]  # Sets to current price of item
                print(f"Current price of item is: {original}")

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

                menu_file[edit_index-1][1] = price  # Assigns the new price to the menu item
                print(f"Price changed to {price}")

            elif inp == "c":  # User inputs category for new item 
                old_category = menu_file[edit_index-1][3]  # Sets to current/old category

                categories = ["breakfast", "mains", "extras", "drinks"]
                print("-" * 30)
                print("Please choose the menu category of your new menu item:\n"
                      "Categories to choose from: Breakfast, Mains, Extras and Drinks\n")

                while True:  # Validation of category
                    new_category = input("Your category: ").lower()
                    if new_category in categories:  # Category is valid
                        break
                    else:
                        print("Please enter a valid category, try again.\n")

                if new_category == old_category:  # Category hasn't changed
                    # menu_file[edit_index-1][3] = new_category  # Assigns the new category to the menu item
                    print(f"Category not changed. ({new_category} is the same category as before)")

                elif new_category != old_category:  # Categeory has changed

                    # Takes all categories in menu.txt and only
                    # stores the category in an array: 'categories_in_file'
                    categories_in_file = []
                    for element in menu_file:  # Iterates over each element in menu.txt
                        categories_in_file.append(element[3])

                    # Finds how many of 'category' is in 'categories_in_file'
                    # Along with how what their specific indexes are on
                    # the menu in the 'categories_present_index' variable
                    categories_present_index = []
                    for index, category_tmp in enumerate(categories_in_file):
                        if category_tmp == new_category:
                            categories_present_index.append(int(index+1))

                    start_line = min(categories_present_index)  # Assigns min index value
                    final_line = max(categories_present_index)  # Assigns max index value

                    print("-" * 30)
                    print_menu(menu_file, start_line=start_line, final_line=final_line)

                    # Get new item's index from user and insert it into the menu file
                    print("You must assign a new index to your item since it's in a different category than before.\n"
                          f"Please note that items shown above are for the {new_category} category.\n"
                          f"Choose an index between {start_line} and {final_line}.\n"
                          )

                    old_index = menu_file[edit_index-1][0]  # Saves old index for later

                    while True:  # Validation Check of menu item index number
                        try:
                            new_index = int(input("Your new menu item index: "))
                            if new_index < start_line or new_index > final_line:   # Out of range
                                print(f"Please enter a value between {start_line} and {final_line}.\n")
                            else:
                                break
                        except ValueError:
                            print("Your index must contain only numeric characters only, try again.\n")

                    tmp_new_item = menu_file[edit_index-1]  # Saves the new item to tmp_new_item
                    del menu_file[edit_index-1]  # Deletes the old item

                    tmp_new_item[0] = str(new_index)  # Assigns the new index to the menu item
                    tmp_new_item[3] = new_category  # Assigns the new category to the menu item

                    menu_file.insert(new_index-1, tmp_new_item)  # Inserts the tmp menu item
                    print(f"Index changed to {new_index}")

                    # Corrects the index numbers in the menu
                    for index, full_item in enumerate(menu_file, start=1):
                        full_item[0] = str(index)

                    edit_index = new_index  # Saves edit_index for next use

            else:  # User wants to exit editing loop of current item
                break


# Allows user to add menu items to the menu
def add_menu_items(menu_file):

    # Prints the current menu for the user to see
    print("-" * 30)
    print("\nThis is the current menu:")
    print_menu(menu_file)

    # User inputs category for new item 
    categories = ["breakfast", "mains", "extras", "drinks"]
    print("-" * 30)
    while True:  # Loops adding item process

        print("Please choose the menu category of your new menu item:\n"
              "Categories to choose from: Breakfast, Mains, Extras and drinks\n")
        while True:  # Validation of category
            category = input("Your category: ").lower()
            if not category in categories:
                print("Please enter a valid category, try again.\n")
            else:
                break

        # User inputs name for new item
        print("-" * 30)
        print("Please choose the name of your new menu item.\n")
        while True:  # Validates Name
            name_tmp = input("Name of new menu item: ")

            # Checks if name contains only letters and spaces
            if name_tmp[-1] == " ":
                print("Name must not contain spaces at the end!")
            elif not all(letter.isalpha() or letter.isspace() for letter in name_tmp):
                print("Name must contain alphabetic characters only, try again.\n")
            else:
                name = ""
                words = name_tmp.split()  # Splits name_tmp into list
                len_words = len(words)

                # Takes each word in the string, formats
                # and concatenates it to variable: "name"
                for index, word in enumerate(words):
                    if index == 0:  # First word
                        word = word.title()  # Makes first letter capital
                        name += f"{word} "
                    elif index+1 == len_words:  # last word
                        name += word
                    else:  # Other words
                        name += f"{word} "
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
        # Along with how what their specific indexes are on
        # the menu in the 'categories_present_index' variable
        categories_present_index = []
        for index, category_tmp in enumerate(categories_in_file):
            if category_tmp == category:
                categories_present_index.append(int(index+1))

        start_line = min(categories_present_index)  # Assigns min index value
        final_line = max(categories_present_index)  # Assigns max index value

        print("-" * 30)
        print_menu(menu_file, start_line=start_line, final_line=final_line)

        # Get new item's index from user and insert it into the menu file
        print("What index would you like to assign to your new menu item?\n"
              f"Please note that items shown above are for the {category} category.\n"
              f"Choose an index between {start_line} and {final_line}.\n"
              )

        while True:  # Validation Check of menu item index number
            try:
                new_index = int(input("Your new menu item index: "))
                if new_index < start_line or new_index > final_line:   # Out of range
                    print(f"Please enter a value between {start_line} and {final_line}.\n")
                else:
                    break
            except ValueError:
                print("Your index must contain only numeric characters only, try again.\n")

        # Formatting the new menu item for it to be written to menu.txt
        new_item = [f'{new_index}', f"{price}", f"{name}", f"{category}"]

        # Creates temp version as a preview for user 
        temp_menu_file = menu_file[:]

        # Adds 1 to the existing menu items' indexes
        for index, el in enumerate(temp_menu_file, start=1):
            if index >= new_index:
                el_index = int(el[0])
                el_index += 1
                el[0] = str(el_index)
        temp_menu_file.insert(new_index-1, new_item)  # Inserts the new item

        print("-" * 30)
        print_menu(temp_menu_file, start_line=start_line, final_line=final_line+1, inserted_line=new_index-1)

        print("\n(S)ave changes and exit\n"
              "(R)etry and discard changes\n"
              "Save Changes and (A)dd another menu item\n"
              "(D)iscard changes and exit\n"
              )
        while True:  # Validates input
            choice = input("Your Choice: ").lower()
            if choice == "s" or choice == "r" or choice == "a" or choice == "d":
                break
            else:
                print("Please enter either:"
                      "\"S\" to save,\n"
                      "\"R\" to retry,\n"
                      "\"A\" to add another item\n"
                      "\"D\" to discard changes and exit"
                      )

        if choice == "s":  # Save and Exit (S)
            menu_file = temp_menu_file[:]  # Writes temp to menu_file
            break  # Breaks the while 
        elif choice == "r":  # Retry without saving changes (R)
            for index, el in enumerate(temp_menu_file, start=1):
                if index > new_index:
                    el_index = int(el[0])
                    el_index = el_index - 1
                    el[0] = str(el_index)
        elif choice == "a":  # Add another item (A)
            menu_file = temp_menu_file[:]  # Saves changes to menu_file
        else:  # Exits without saving changes (D)
            for index, el in enumerate(temp_menu_file, start=1):
                if index > new_index:
                    el_index = int(el[0])
                    el_index = el_index - 1
                    el[0] = str(el_index)
            break

    if choice == "s":  # Write changes to menu.txt
        with open("menu.txt", "w") as file:
            for item in menu_file:  # writes from menu_file
                file.write(f"{item[0]},{item[1]},{item[2]},{item[3]}\n")
    return menu_file


# Provides menu interface for user to choose to Add, edit or delete menu items
def editing_main_menu(menu_file):  # Credits to github.com/RoyceLWC for Menu. 
    while True:
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

        if index == 4:  # User wants to exit the menu 
            write_menu(menu_file)  # Saves the menu to menu.txt
            return menu_file
        else:
            menu_file = menu[str(index)][1](menu_file)



# Writes running totals to running_totals.txt
def write_order(total_price, total_quantity, quantity_dict, table_num):
    with open("running_totals.txt", "w") as file:  # Creates the file and writes default menu
        file.write(f"{total_price}\n")
        file.write(f"{total_quantity}\n")


# Displays the current order with the quantities of each menu item.
def display_order(total_price, total_quantity, quantity_dict, table_num):

    # By default the price doesn't display all 2 decimal points.
    # E.g. a price of "$2.50" would only display "$2.5"
    # These 3 lines below fix this issue.
    total_price = str(total_price)
    if total_price[-2] == ".":
        total_price += "0"

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
        full_item_tmp = f"{number}. {name} ${price}"
        length_of_full = len(full_item_tmp)
        period_num = max_len - length_of_full
        periods = period_num * "."
        full_item = f"{number}. {name} {periods} ${price}"
        real_output.append(full_item)

    # Sets values using kwargs to determine
    # which specfic lines to iterate over
    start_line = kwargs.get("start_line")
    final_line = kwargs.get("final_line")
    inserted_line = kwargs.get("inserted_line")
    single_line = kwargs.get("single_line")

    # Takes all categories in menu.txt and only
    # stores the category in an array: 'categories_in_file'

    categories_in_file = []
    for element in menu_file:  # Iterates over each element in menu.txt
        categories_in_file.append(element[3])

    # Finds how many of each category is in the file
    category_dict = get_quantity(categories_in_file)

    # Formats categories with separators for menu
    all_keys = []
    separator = "~"  # Define the separator for printing
    if start_line == None:  # No **kwargs provided
        for key in category_dict.keys():  # Iterates over each category
                full_item_tmp = f"{key} "
                length_of_full = len(full_item_tmp)
                separator_num = max_len - length_of_full
                separators = separator_num * separator
                full_item = f"\n{key.title()} {separators}"
                all_keys.append(full_item)
    else:  # **kwargs provided
        category = menu_file[start_line-1][3]
        full_item_tmp = f"{category} "
        length_of_full = len(full_item_tmp)
        separator_num = max_len - length_of_full
        separators = separator_num * separator
        full_item = f"\n{category.title()} {separators}"

    # Print if no **kwargs are provided
    if start_line == None and final_line == None and inserted_line == None:
        current_index = 0  # Current index of real_output
        for key in all_keys:
            print(key)

            # Loops for the amount of items there are for that key/category
            for i in range(category_dict[key.strip(f"{separator} \n").lower()]):
                print(f"\n{real_output[current_index]}")
                current_index += 1  # Changes to next key 

    # start_line and final_line are provided but inserted_line isn't as **kwargs
    elif (start_line != None and final_line != None) and inserted_line == None:
        print(full_item)
        for index, item in enumerate(real_output):
            if start_line <= index+1 <= final_line:  # Index is in correct printing range
                print(f"\n{item}")  # Prints all menu items formatted with perfect amount of periods.

    # start_line, final_line and inserted_line are all provided as **kwargs
    elif start_line != None or final_line != None or inserted_line != None:
        print(full_item)
        for index, item in enumerate(real_output):
            if start_line <= index+1 <= final_line:  # Index is in correct printing range
                if index+1 == inserted_line+1:
                    # Prints menu items formatted with perfect amount of periods.
                    print(f"\n{item} <--- YOUR NEW ITEM")
                else:
                    print(f"\n{item}")  # Prints all menu items formatted with perfect amount of periods.
    print("\n")


def get_order_input(menu_file):  # Validates Order
    print_menu(menu_file)
    while True:
        print("-" * 30)
        print("\nE.g. \"6,4,4,7,8,10,10\""
              " Would be an order from Table 6 for 2 Burgers, 1 Fries, 1 Salad and 2 Soft"
              " Drinks.")
        tmpData = input("\nType order here: ").split(",")

        # Removes spaces from each element in tmpData,
        # then adds elements to 'data'
        data = []
        for string in tmpData:  # Iterates over each value
            string = ''.join(string.split())  # Removes spaces from data
            data.append(string)

        tmp_last_item = menu_file[len(menu_file) -  1]  # Assigns Last entry's index
        last_item = tmp_last_item[0]                    # to "last_item"
        invalid = ""
        invalidTable = ""
        for index, element in enumerate(data):  # Takes each element in the array
            if index == 0:  # If the element is first (table number doesn't apply for these rules)
                if element.isnumeric() == False:  # If first element in data is NOT numeric:
                    invalid = True
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
            "2": [": Edit Menu Items", editing_main_menu],
            "3": [": Finalize Order", finalize_order],
            "4": [": Options", options],
            "5": [": Quit to Desktop"]
        }

        # Prints each menu index and its corresponding functions description
        for key in sorted(menu.keys()):
            print(key + menu[key][0])

        while True:  # Loop until a valid index is received
            print("-" * 30)
            index = input("Select an index: ")
            try:  # Try to convert to an integer
                index = int(index)  # Converts to an integer
                if 1 <= index <= 5:  # In range
                    break
                else:  # Out of range
                    print("Out of range try again!")
            except ValueError:  # If it can't be converted to an integer
                print("Invalid index")
        data = ""
        print("-" * 30)
        if index == 1:  # get_order_input() | Get all data about the order, e.g. price, quantity and table num.
            total_price, total_quantity, quantity_dict, table_num = menu[str(index)][1](menu_file)
            hasData = True
        elif index == 2 or index == 4:  # editing_main_menu or options()
            menu_file = menu[str(index)][1](menu_file)
        elif index == 3:  # finalize_order()
            if not hasData:  # No order data
                print("No current order! Go back and Input an order.")
            else:
                total_price, total_quantity, quantity_dict, table_num, hasData = menu[str(index)][1](total_price, total_quantity, quantity_dict, table_num, hasData)
        else:
            quit()


def check_file(DEFAULT_MENU):  # Checks for menu and Creates DEFAULT_MENU if doesn't exist.
    for i in range(2):  # Quick fix for the file not being read on first try idk.
        try:  # Check for existing file by trying to read the file
            with open("menu.txt", "r") as file:
                whole_file = file.readlines()  # Stores the menu in the file as "whole_file"
                menu_file = []
                for element in whole_file:
                    element = element.strip("\n")
                    element = element.split(",")
                    menu_file.append(element)
                return menu_file
        except IOError:  # If menu.txt is not found, make a new file
            with open("menu.txt", "w") as file:  # Creates the file and writes default menu
                for line in DEFAULT_MENU:
                    file.write(f"{line}\n")
            check_file(DEFAULT_MENU)


menu_file = check_file(DEFAULT_MENU)  # Checks for menu and Creates DEFAULT_MENU if doesn't exist.
main_menu(menu_file)  # Main Menu for most the program
