"""
  This module contains main functions that relate to the Motivational Application. 
  It defines functions that allow the user to interact with, add, remove and search 
  for quotes from a file named 'quote.txt' located in the src directory.
"""

from random import choice


# Defining method to generate random quote
def get_random_quote():
    """
    Selects and prints a random quote from the 'quote.txt' file.

    Raises:
        FileNotFoundError: If the 'quote.txt' file is not found in the expected location.
        IOError: If there is an issue reading the 'quote.txt' file.
        Exception: For any other unexpected errors that may occur during the process.

    Returns:
        None

    Example:
        >>> get_random_quote()
        "Believe you can and you're halfway there. - Theodore Roosevelt"
    """
    try:
        with open("src/quote.txt", "r", encoding="utf-8") as file:
            # Opening txt file (quotes.txt) and reading lines
            lines = file.readlines()
            # Using random to generate random quote (line) and saving it into random line variable
            random_line = choice(lines)
            # Printing random quote
            quote_text, category = random_line.strip().split(" : ")
            print(quote_text)
    # Exception Errors.
    except (FileNotFoundError, IOError):
        print("Error occured retrieving a quote from the file.")
    except Exception as e:
        print(f"An error occurred while generating random quote from file: {e}")


def get_quote_from_preference(category):
    """
    Selects and prints a random quote from the specified category.

    Args:
        category (str): The category of quotes from which to select a random quote.
                        This parameter specifies the user preference for the type of quote.

    Raises:
        FileNotFoundError: If the 'quote.txt' file is not found in the expected location.
        IOError: If there is an issue reading the 'quote.txt' file.
        Exception: For any other unexpected errors that may occur during the process.

    Returns:
        None

    Note:
        If the specified category is not found in the 'quote.txt' file, it prints a message
        indicating that the category is not available.

    Example:
        >>> get_quote_from_preference('Motivation')
        "Believe you can and you're halfway there. - Theodore Roosevelt"
    """
    category = category.strip().capitalize()
    try:
        with open("src/quote.txt", "r", encoding="utf-8") as file:
            # Opening txt file (quotes.txt) and reading lines (quotes)
            lines = file.readlines()
            # Filter lines (quotes) to find those that match specified category (preference)
            filter_lines = [
                line
                for line in lines
                if len(line.strip().split(" : ")) == 2
                and line.strip().split(" : ")[1].capitalize() == category
            ]
            # Making sure filter_lines returns correctly
            if filter_lines:
                # Using random to generate a random quote from filter list
                random_line = choice(filter_lines)
                # Printing the quote from filter lines list (category)
                quote_text, category = random_line.strip().split(" : ")
                print(quote_text)
            else:
                print("Sorry, that is not an avalaible category! Please check the spelling is correct or enter an avaliable category!")
    except (FileNotFoundError, IOError):
        print("Error occured retrieving a quote from the file.")
    except Exception as e:
        print(f"An error occurred while generating random quote from file: {e}")


def get_categories():
    """
    Defining function to output the unqiue subject categories from the quote.txt file
    to the user while distinguishing between 'base' and user added categories.
    Displays all available categories of quotes from the 'quote.txt' file.

    Raises:
        FileNotFoundError: If the 'quote.txt' file is not found in the expected location.
        IOError: If there is an issue reading the 'quote.txt' file.
        ValueError: If there is an issue processing the content of the 'quote.txt' file.

    Returns:
        None
    """
    base_categories = {
        "Happiness",
        "Inspiration",
        "Mindfulness",
        "Motivation",
        "Positivity",
    }
    user_categories = (
        set()
    )  # Creating an empty set to store unique user added categories
    try:
        with open("src/quote.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        # Collecting categories from each line and adding them to correct the set
        for line in lines:
            seperate = line.strip().split(" : ")
            if len(seperate) == 2:
                category = seperate[1].capitalize()
                if category not in base_categories:
                    user_categories.add(category)
        # Print all 'base' categories and user added categories
        print("Quote Categories :")
        for category in base_categories:
            print(category)
        # Prints user-added categories.
        for category in user_categories:
            if category in user_categories:
                print("Quote Categories You Created! : ")
                print(category in user_categories)
    except (IOError, ValueError) as e:
        print(f"An error occurred while generating a quote: {e}")


def display_quote():
    """
    Allows the user to choose a category or get a random quote, combined function use of
    (get_categories) and (get_quote_from_preference)

    Displays a quote based on user input category preference or a random quote.

    Raises:
        FileNotFoundError: If the 'quote.txt' file is not found in the expected location.
        IOError: If there is an issue reading the 'quote.txt' file.
        Exception: For any other unexpected errors that may occur during the process.

    Returns:
        None
    """
    try:
        # Calling the get_categories function to displaty all categories to the user.
        get_categories()
        print("Choose an avaliable category to recieve a quote, or we can surprise you!")
        preference = (
            input("Enter 'Category' or 'Surprise' to get a quote:  ")
            .strip()
            .capitalize()
        )
        # Checking user input to options below.
        if preference == "Surprise":
            get_random_quote()
        else:
            get_quote_from_preference(preference)
    except Exception as e:
        print(f"An error occurred : {e}")


def print_all_from_category():
    """
    Prints all quotes under a specified category.

    Raises:
        FileNotFoundError: If the 'quote.txt' file is not found in the expected location.
        IOError: If there is an issue reading the 'quote.txt' file.
        Exception: For any other unexpected errors that may occur during the process.

    Returns:
        None
    """
    try:
        # Prints all the quote categories avliable
        print("Print all quotes in category")
        get_categories()
        # Prompt for user to input a category
        category = (
            input("Please enter a category to display all quotes: ")
            .strip()
            .capitalize()
        )
        # Open the txt file (quotes.txt) in read mode to read all existing lines (quotes)
        with open("src/quote.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        # Searching quotes line by line to the specified category
        category_quotes = [
            line.strip() for line in lines if line.strip().endswith(f" : {category}")
        ]
        # Printing all the quotes under the specified category
        if category_quotes:
            print(f"All quotes under the category : {category} : ")
            for quote in category_quotes:
                print(quote.split(" : ")[0])
        # Message to catch an error of invalid category
        else:
            print(f"No quotes under the category : {category} : ")
    except Exception as e:
        print(
            f"An error occurred : {e} Please double check input is correct, and try again!"
        )


def remove_category():
    """
    A function to remove categories only created by the user.

    Raises:
        FileNotFoundError: If the 'quote.txt' file is not found in the expected location.
        IOError: If there is an issue reading or writing to the 'quote.txt' file.
        Exception: For any other unexpected errors that may occur during the process.

    Returns:
        None
    """
    try:
        # Defining a variable to store the 'base' categories.
        base_categories = {
            "Motivation",
            "Inspiration",
            "Mindfulness",
            "Positivity",
            "Happiness",
        }
        # Printing a message to the user to warn them that cahnges cannot be undone.
        print("Please note - YOU CAN ONLY REMOVE CATEGORIES YOU HAVE CREATED AND ONCE REMOVED CANNOT BE UNDONE")
        # Allowing the user to input a 'Yes' or 'No', incase they do not want to remove entirely.
        user_choice = (
            input("Would you still like to remove a category? 'Yes' or 'No' : ")
            .strip()
            .capitalize()
        )
        # Commencing removal if chosen 'Yes' by user.
        if user_choice == "Yes":
            get_categories()
            category_choice = (
                input("Please enter a category to be removed : ").strip().capitalize()
            )
            with open("src/quote.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
                if category_choice.capitalize() not in base_categories:
                    update_lines = [
                        line
                        for line in lines
                        if not line.strip().endswith(f": {category_choice}")
                    ]
                    with open("src/quote.txt", "w", encoding="utf-8") as file:
                        file.writelines(update_lines)
                        print(f"The category '{category_choice}' has been removed!")
                else:
                    print(f"The category '{category_choice}' is a base category and cannot be removed!")
        # Commencing no removal if chosen by the user.
        elif user_choice == "No":
            print("Have a think about it and come back!")
            return
        else:
            print("Invalid option! Make sure to enter an avaliable option 'Yes' or 'No'.")
    except Exception as e:
        print(f"An error occurred : {e} Please double check input is correct, and try again!")


def edit_categories():
    """
    A function to edit categories of quotes

    Raises:
        FileNotFoundError: If the 'quote.txt' file is not found in the expected location.
        IOError: If there is an issue reading or writing to the 'quote.txt' file.
        Exception: For any other unexpected errors that may occur during the process.

    Returns:
        None
    """
    try:
        # Printing more information to user.
        print("You can VIEW existing categories or EDIT 'add/remove' categories!")
        print("Would you like to : VIEW categories? or EDIT categories?")
        # Prompting input from user.
        user_choice = input("Please enter 'View' or 'Edit' : ").strip().capitalize()
        # Commencing sequence based on user input.
        if user_choice == "View":
            get_categories()
        elif user_choice == "Edit":
            print("Would you like to ADD a new category or REMOVE an existing category?")
            user_choice = (
                input("Please enter 'Add' or 'Remove' : ").strip().capitalize()
            )
            if user_choice == "Add":
                category = (
                    input("Please enter the name of the new category: ")
                    .strip()
                    .capitalize()
                )
                quote_text = ("You can do it!").strip()
                with open("src/quote.txt", "a", encoding="utf-8") as file:
                    file.write(f"\n{quote_text} : {category}\n")
                    print(f"The category '{category}' has been added!")
            elif user_choice == "Remove":
                remove_category()
            else:
                print("Invalid option! Make sure to enter an avaliable option 'Add' or 'Remove'.")
        else:
            print("Invalid option! Make sure to enter an avaliable option 'View' or 'Edit'.")
    except Exception as e:
        print(f"An error occurred : {e} Please double check input is correct, and try again!")


def add_my_own_quote():
    """
    A function that allows users to create thier own quotes and add them into the quote.txt file.
    If the category is not already created user is prmpoted to create a new category or exit.
    Raises:
        FileNotFoundError: If the 'quote.txt' file is not found in the expected location.
        IOError: If there is an issue reading or writing to the 'quote.txt' file.
        Exception: For any other unexpected errors that may occur during the process.

    Returns:
        None
    """
    try:
        print("Create a new quote below!")
        quote_text = input("Enter your quote here: ").strip().capitalize()
        category = input("Enter a category for the quote: ").strip().capitalize()
        # Checking if the category the user entered already exists
        with open("src/quote.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            categories = {
                line.strip().split(" : ")[1] for line in lines if line.strip()
            }
        if category not in categories:
            print(f"The category you have entered '{category}', does not exist.")
            # Ask the user for input to create a new category
            confirm = (
                input("Do you want to create a new category? 'Yes' or 'No' : ")
                .strip()
                .capitalize()
            )
            if confirm == "Yes":
                categories.add(category)
                with open("src/quote.txt", "a", encoding="utf-8") as file:
                    file.write(f"\n{quote_text} : {category}\n")
                    print(f"The category '{category}' has been added!")
            elif confirm == "No":
                print("Category creation CANCELLED. New quote has NOT been added.")
        else:
            # If category entered already exists, add quote to file
            # Open the txt file (quote.txt) in append mode and add the new quote into it
            with open("src/quote.txt", "a", encoding="utf-8") as file:
                file.write(f"{quote_text} : {category}\n")
                print("Your quote has been added!")
    except Exception as e:
        print(f"An error occurred : {e} Please double check input is correct, and try again!")


def remove_quote():
    """
    A function to remove a quote from the quote.txt file.

    Raises:
        FileNotFoundError: If the 'quote.txt' file is not found in the expected location.
        IOError: If there is an issue reading or writing to the 'quote.txt' file.
        Exception: For any other unexpected errors that may occur during the process.

    Returns:
        None
    """
    try:
        # Ask the user input the quote they want to remove
        quote_text = (
            input("Enter the quote you would like to remove:  ").strip().capitalize()
        )
        # Open the txt file (quotes.txt) in read more to read all existing lines (quotes)
        with open("src/quote.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        # Filter (find) the quote to be removed
        filtered_lines = [
            line
            for line in lines
            if line.strip().split(" : ")[0].capitalize() != quote_text
        ]
        # Confirming that the quote has been removed
        if len(lines) == len(filtered_lines):
            print("Sorry, the entered quote does not exist! Please double check you entered an existing quote!")
        # Remaining quotes back to the text file (quotes.txt)
        else:
            with open("src/quote.txt", "w", encoding="utf-8") as file:
                file.writelines(filtered_lines)
                print("Your quote has been removed!")
    except Exception as e:
        print(f"An error occurred while removing quote : {e} Please double check input is correct, and try again!")


def edit_quote():
    """
    A function that allows you to edit a quote, either adding or removing.
    It incorperated other functions (add_my_own_quote), (remove_quote) and (print_all_from_category).
    Allowing dynamic edditing options and choice to the user.

    Raises:
        FileNotFoundError: If the 'quote.txt' file is not found in the expected location.
        IOError: If there is an issue reading or writing to the 'quote.txt' file.
        Exception: For any other unexpected errors that may occur during the process.

    Returns:
        None
    """
    try:
        # Providing more information to the user.
        print("Edit Quote Options")
        print("Would you like to add or remove a quote?")
        # Prompting user input
        user_choice = input("Please enter 'Add' or 'Remove' :   ").strip().capitalize()
        # Commencing sequence based on user input.
        if user_choice == "Add":
            add_my_own_quote()
        elif user_choice == "Remove":
            print("Do you know what quote you want to remove?")
            decision = input("Enter 'Yes' or 'No' : ").strip().capitalize()
            if decision == "Yes":
                remove_quote()
            elif decision == "No":
                # Offering the user more relevant information to help them decide.
                print("Would you like to view all quotes from a category to help you decide?")
                decide = input("Enter 'Yes' or 'No' : ").strip().capitalize()
                if decide == "Yes":
                    print_all_from_category()
                    print("Would you like to remove a quote?")
                    decide = input("Enter 'Yes' or 'No' : ").strip().capitalize()
                    if decide == "Yes":
                        remove_quote()
                    elif decide == "No":
                        print("Have a think about it and come back!")
                elif decide == "No":
                    print("Have a think about it and come back!")
                else:
                    print("Invalid input! Try again and choose from the avaliable options!")
        else:
            print(f"{user_choice} is invlaid. Please try again and choose from the avaliable options!")
    except Exception as e:
        print(f"An error occurred : {e} Please double check input is correct, and try again!")


def search_quotes():
    """
    A function that allows the user to input 'keywords', can be serveral or one. The keywords are
    matched to quotes in the quote.txt file and displayed back to the user.
    The function will loop until the user decides to exit.

    Raises:
        FileNotFoundError: If the 'quote.txt' file is not found in the expected location.
        IOError: If there is an issue reading the 'quote.txt' file.
        Exception: For any other unexpected errors that may occur during the process.

    Returns:
        None
    """
    try:
        while True:
            print("Search for a quote by entering 'keywords'")
            search_keywords = input("Enter keywords : ").strip().lower().split()
            # Open the txt file (quote.txt) file and read all lines
            with open("src/quote.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
            # Create a list to store matched quotes
            matched_quotes = []
            # Iterate through each line to check for any matches
            for line in lines:
                quote_text = line.strip().split(" : ")[
                    0
                ]  # Make sure quote 'text' only not 'category'
                if all(keyword in quote_text.lower() for keyword in search_keywords):
                    matched_quotes.append(quote_text)
            # Display any quotes that have matched to keyowrds searched by user
            if matched_quotes:
                print("Here are the quotes with matching keywords : ")
                for quote in matched_quotes:
                    print(quote)
            else:
                print("Sorry, we cannot find any quotes matching the keywords you entered!")
            # Allowing the user to search again
            user_choice = (
                input("Would you like to search again? 'Yes' or 'No' : ")
                .strip()
                .capitalize()
            )
            if user_choice == "No":
                break
    except Exception as e:
        print(f"An error occurred : {e} Please double check input is correct, and try again!")


def display_help():
    """
    Displays 'help' information from the help.txt file back to the user.
    Providing some more information about the Mindset application the the user and also more inforamtion about each feature.

    Raises:
        FileNotFoundError: If the 'help.txt' file is not found in the expected location.
        IOError: If there is an issue reading the 'help.txt' file.
        Exception: For any other unexpected errors that may occur during the process.

    Returns:
        None
    """
    try:
        # Opening the help.txt file and displaying the further information to the user.
        with open("src/help.txt", "r", encoding="utf-8") as file:
            help_text = file.read()
            print(help_text)
    except FileNotFoundError:
        print("Error: Help file not found.")


def menu_options():
    """
    A function that solely prints the 'Menu' options to the user.
    Added to reduce the code on the (main.py) moddule.
    """
    # Prints 'Menu' options, allowing multiple lines to be stored in a function and called.
    print("Welcome to the Mindest Application")
    print("1. Surprise me with a random quote")
    print("2. Boost your mood, get a quote based on your need!")
    print("3. Quote Options (Create or Remove Quotes)")
    print("4. Search Quotes")
    print("5. Category Options (View all, Create or Remove)")
    print("6. Help")
    print("7. Exit")