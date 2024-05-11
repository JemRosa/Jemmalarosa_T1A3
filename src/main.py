"""
    This module main.py  is the 'main' module of the Mindset Terminal Application. 
    Seperated to keep the code organised. 
    'Main Menu' for my Mindest Application. Allows users to interact with different 'features' 
    of the application. Such as genterating random quotes, managing quotes and categories, 
    adding their own, and the ability to search quotes etc.
"""
import quote_manager


def menu():
    """
    Main Menu for the Mindset Application.

    This function allows users to interact with different features of the application, including generating random quotes,
    managing quotes and categories, adding their own quotes, and searching quotes.

    Users are presented with a numbered menu and prompted to choose an option. Depending on the chosen option, 
    the user will be guided through various functionalities of the application until they decide to exit.

    Returns:
        None

    Raises:
        Exception: If an error occurs during the execution of the menu options.
    """
    running = True
    try:
        while running:
            # Display the 'Menu' options.
            quote_manager.menu_options()
            # Prompting the user to choose an option.
            user_choice = int(input("Please Choose a Number :  "))
            if user_choice == 1:
                # Displaying random quotes until the user chooses to return to the 'Menu'.
                while True:
                    quote_manager.get_random_quote()
                    option = input("Enter 'Menu' to go back or 'Surprise' to get another quote : ").strip().capitalize()
                    if option not in ["Menu", "Surprise"]:
                        print("Invalid Option, please enter valid input!")
                    elif option == "Menu":
                        break
            elif user_choice == 2:
                # Displaying quotes based on user preference until the user chooses to return to the 'Menu'.
                while True:
                    quote_manager.display_quote()
                    option = input("Enter 'Menu' to go back or 'Another' to get another quote : ").strip().capitalize()
                    if option == "Menu":
                        break
            elif user_choice == 3:
                # Allowing users to edit quotes until the user chooses to return to the 'Menu'.
                while True:
                    quote_manager.edit_quote()
                    option = input("Enter 'Menu' to go back or 'Edit' to see quote options again : ").strip().capitalize()
                    if option == "Menu":
                        break
                    elif option != "Edit":
                        print("Invalid input! Please try again and choose from the avaliable options!")
            elif user_choice == 4:
                # Allowing users to search quotes until the user chooses to return to the 'Menu'.
                while True:
                    quote_manager.search_quotes()
                    option = input("Enter 'Menu' to go back or 'Search' to search again : ").strip().capitalize()
                    if option == "Menu":
                        break
                    if option != "Search":
                        print("Invalid input! Please try again and choose from the avaliable options!")
            elif user_choice == 5:
                # Allowing users to edit categories until the user chooses to return to the 'Menu'.
                while True:
                    quote_manager.edit_categories()
                    option = input("Enter 'Menu' to go back or 'Options' to see category options again : ").strip().capitalize()
                    if option == "Menu":
                        break
                    if option != "Options":
                        print("Invalid input! Please try again and choose from the avaliable options!")
            elif user_choice == 6:
                # Displaying help information until the user chooses to return to the 'Menu'.
                while True:
                    quote_manager.display_help()
                    option = input("Please enter 'Menu' to return: ").strip().capitalize()
                    if option == "Menu":
                        break
            elif user_choice == 7:
                # This will EXIT the Mindest Application.
                print("Thankyou for using Mindset application!")
                running = False
            else:
                print(f"{user_choice} : Invalid Input. Please enter a number from the avliable options.") 
    except Exception as e:
        print(f"An error occurred : {e} Please double check input is correct, and try again!")

menu()
