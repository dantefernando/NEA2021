# Input Example: 6, 4, 4, 7, 8, 10, 1

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


def get_order_data():  # Validates Order 
    while True:
        data = input("\nType order here: ").split(",")
        hasAlpha = ""
        for element in data:  # Takes each element in the array
            if len(element) > 1:
                invalid = True
            for letter in element:  # Takes each letter in the element 
                if letter.isalpha() == True:  # If the letter is a letter
                    invalid = True           # then set hasAlpha to True
        if invalid:  # If there are letters or symbols in the input: 
            print("Your order has invalid characters, please try again.")
        else:
            return data


def main_menu():  # Main Menu, first menu that the user sees.
    print("--Main Menu--")
    menu = {
        "1": [": Input order data", get_order_data],
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
    if index == 1:  # Get Order data
        data = menu[str(index)][1]()
    elif index == 2:  # change_menu_items
        menu[str(index)][1]()
    else:
        menu[str(index)][1](data)


def check_file(default_menu):  # Checks for menu and Creates default_menu if doesn't exist.
    try:  # Check for existing file by trying to read the file
        with open("menu.txt", "r") as file:
            whole_file = file.readlines()  # Stores the menu in the file as "whole_file"
            menu_file = []
            for element in whole_file:
                element = element.strip("\n")
                menu_file.append(element)
            file.close()

    except IOError:  # If menu.txt is not found, make a new file
        with open("menu.txt", "w") as file:  # Creates the file and writes default menu
            for line in default_menu:
                file.write(f"{line}\n")
            file.close()


def main():
    check_file(default_menu)  # Checks for menu and Creates default_menu if doesn't exist.
    main_menu()


if __name__ == "__main__":
    main()
