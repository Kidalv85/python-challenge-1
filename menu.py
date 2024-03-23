
order_details =[]
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

menu_dashes = "-" * 42
def printHeadingForSubMenu():
        print(menu_dashes)
        print(f"This is the {menu_category_name} menu.")
        print(menu_dashes)
        print("Item # | Item name                | Price")
        print("-------|--------------------------|-------")

# method to print order reciept
def printReciept():
    print(" ")
    if len(order_details)>0:
        item_name_text = "Item name          "
        price_text = "  Price  "
        quantity_text = "  Quantity  "
        print("Here is your order summery")
        print(" ")
        print(f"{item_name_text}|{price_text}|{quantity_text}")
        print(" ")
        print ('-' * len(item_name_text) + "|" + '-' * len(price_text) + "|" + '-' * len(quantity_text))
        total = 0

        for item in order_details:
            print(" ")
            item_name = item["Item name"]
            price = item["Price"]
            quantity = item["Quantity"]
            total += price*quantity
            print(item_name + " "*(len(item_name_text)-len(item_name)) + "|" + "  $" + str(price) + " "*2 +  "|" + " "*2 + str(quantity))
        print(" ")
        print ('-' * len(item_name_text) + "|" + '-' * len(price_text) + "|" + '-' * len(quantity_text))
        print(f"Total ${total}")
        print()
        
    else :
        print("We are sorry, you did not like our menu...")
    print(" ")

# method to add selected item to customer order 
def addItemToTheOrder():
    menu_selection = input("Please make your selection ")
    quantity = input("How many? In case of invalid input system will add 1 item by default ")
   
    if quantity.isdigit() :
        if (int(quantity)<0):
            quantity = int(quantity)*-1
        else:
            quantity = int(quantity)
    else:
        quantity = 1

    if(menu_selection.isdigit()):
        menu_selection = int(menu_selection)
        #check if user's input is in menu items
        if menu_selection in menu_items.keys():
            # add selection to the order_details list
            print(menu_selection)
            print(menu[menu_items[menu_selection]])
            item_name_t = list(menu[menu_items[menu_selection]].keys())[menu_selection-1]
            price_t = menu[menu_items[menu_selection]][item_name_t]
            print(item_name_t)
            print(price_t)
            print(quantity)
            # check if order_list contains the item increase quantity, otherwise add it to the order_list
            if len(order_details) != 0:
                for item_in_orders in order_details:
                    if (item_name_t in item_in_orders.values()):
                        item_in_orders["Quantity"] +=1
                    else:
                        order_details.append(dict({"Item name" : item_name_t, "Price" : price_t, "Quantity" : quantity}))
            else :
                order_details.append(dict({"Item name" : item_name_t, "Price" : price_t, "Quantity" : quantity}))

            stil_shopping_submenu = True
            while stil_shopping_submenu:
                keep_ordering = input("Anything else from this page? (Y)es or (N)o ")
                match keep_ordering.lower():
                    case 'y':
                        stil_shopping_submenu = True
                        break
                    case 'n':
                        stil_shopping_submenu = False
                        break
                    case _:
                        print("I didn't understand your response. Please try again.")
        else:
            print("Select something from the menu")
        print(f"you have selected {order_details}")
    else :
        print("Please select item number ")

print("Welcome to the variety food truck.")

# print main menue
while True:
    print("Which menu would you like to view? ")
    i = 1
    menu_items = {}
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1
    menu_category = input("Type menu number to view or q to quit: ")
    if menu_category == 'q':
        printReciept()
        break
    elif menu_category.isdigit():
        if int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            print(f"You selected {menu_category_name}")
            printHeadingForSubMenu()
            item_counter = 1
            for key, value in menu[menu_category_name].items():
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{item_counter}      | "
                              + f"{key} - {key2}{item_spaces} | "
                              + f"${value2}")
                        item_counter += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{item_counter}      | "
                          + f"{key}{item_spaces} | ${value}")
                    item_counter += 1
            
            print(menu_dashes)
            addItemToTheOrder()
        else:
            print(f"{menu_category} was not a menu option.")
    else:
        print("You didn't select a number.")