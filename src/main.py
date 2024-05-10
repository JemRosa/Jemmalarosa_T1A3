import random
import quote_manager

def menu():
    """
    'Main Menu' for my Mindest Application. Allows users to interact with differennt 'features' of the application. 
    Such as genterating random quotes, managing quotes and categories, adding their own, and the ability to search quotes etc.
    """
    try: 
        while True:
            quote_manager.menu_options()
            choice = int(input("Please Choose a Number :  "))
            if choice == 1:
                while True:
                    quote_manager.get_random_quote()
                    option = input("Enter 'Menu' to go back or 'Surprise' to get another quote : ").strip().capitalize()
                    if option == "Menu":
                        menu()
                    elif option != "Surprise":
                       print("Invalid input! Please try again and choose from the avaliable options!")
            elif choice == 2:
                while True:
                    quote_manager.display_quote()
                    option = input("Enter 'Menu' to go back or 'Another' to get another quote : ").strip().capitalize()
                    if option == "Menu":
                        menu()
            elif choice == 3:
                while True:
                    quote_manager.edit_quote()
                    option = input("Enter 'Menu' to go back or 'Edit' to see quote options again : ").strip().capitalize()
                    if option == "Menu":
                        menu()
                    elif option != "Edit":
                        print("Invalid input! Please try again and choose from the avaliable options!")
            elif choice == 4:
                while True:
                    quote_manager.search_quotes()
                    option = input("Enter 'Menu' to go back or 'Search' to search again : ").strip().capitalize()
                    if option == "Menu":
                        menu()
                    elif option != "Search":
                        print("Invalid input! Please try again and choose from the avaliable options!")
            elif choice == 5:
                while True:
                    quote_manager.edit_categories()
                    option = input("Enter 'Menu' to go back or 'Options' to see category options again : ").strip().capitalize()
                    if option == "Menu":
                        menu()
                    elif option != "Options":
                        print("Invalid input! Please try again and choose from the avaliable options!")
            elif choice == 6:
                while True:
                    quote_manager.display_help()
                    choice = input("Please enter 'Menu' to return: ").strip().capitalize()
                    if choice == "Menu":
                        menu()
                    else:
                        menu()
            if choice == 7:
                print("Thank you for using the Mindest Application!")
                break
    except Exception as e:
        print(f"An error occurred : {e} Please double check input is correct, and try again!")

menu()
