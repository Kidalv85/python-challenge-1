# Menu dictionary
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

        for item in order_details:
            print(" ")
            print(item["Item name"] + " "*(len(item_name_text)-len(item["Item name"])) + "|" + "  $" + str(item["Price"]) + " "*2 +  "|" + " "*2 + str(item["Quantity"]))

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
                    print(item_in_orders)
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
    
    

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to view different sections of the menu, so let's create a 
# continuous loop
while True:
    # Ask the customer which menu category they want to view
    print("Which menu would you like to view? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval 
    menu_items = {}

    # Print the options to choose from menu headings (all the first level 
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number to view or q to quit: ")

    # Exit the loop if user typed 'q'
    if menu_category == 'q':
        printReciept()
        break
    # Check if the customer's input is a number
    elif menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Display the heading for the sub-menu
            printHeadingForSubMenu()

            # Initialize a menu item counter
            item_counter = 1
            # Print out the menu options from the menu_category_name
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    # Iterate through the dictionary items
                    for key2, value2 in value.items():
                        # Print the menu item
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{item_counter}      | "
                              + f"{key} - {key2}{item_spaces} | "
                              + f"${value2}")
                        # Add 1 to the item_counter
                        item_counter += 1
                else:
                    # Print the menu item
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{item_counter}      | "
                          + f"{key}{item_spaces} | ${value}")
                    # Add 1 to the item_counter
                    item_counter += 1
            
            print(menu_dashes)
            addItemToTheOrder()

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")


