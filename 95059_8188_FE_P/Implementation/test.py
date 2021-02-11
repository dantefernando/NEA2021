
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


with open("menu.txt", "w") as file:  # Creates the file and adds date
    for line in default_menu:
        file.write(f"{line}\n")
    file.close()
