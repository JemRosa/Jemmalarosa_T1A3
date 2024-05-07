"""
  imorting random
"""
import random

# Opening tquote.txt and saving it into file variable
file = open("src/quote.txt", "r")


"""defining function to generate random quote
"""
# Defining method to generate random quote
def get_random_quote():
    try:
        with open("src/quote.txt", "r") as file:
           # Opening txt file (quotes.txt) and reading lines
            lines = file.readlines()
           # Using random to generate random quote (line) and saving it into random line variable
            random_line = random.choice(lines)
           # printing random quote
            quote_text, category = random_line.strip().split(" : ")
            print(quote_text)

    except IOError as e:
        print(f"An error occurred while generating random quote: {e}")
        return None


def get_categories():
    try:
        category = {'Motivation', 'Inspiration', 'Mindfulness', 'Positivity', 'Happiness'}
        a, b, c, d, e = category
        print(f"These are the categories avaliable: {a}, {b}, {c}, {d}, {e}.")          
    except (IOError, ValueError) as e:
        print(f"An error occurred while generating a quote: {e}")
        return None
    

def get_quote_from_preference(category):
    try:
        with open("src/quote.txt", "r") as file:
            # Opening txt file (quotes.txt) and reading lines (quotes)
            lines = file.readlines()
            # Filter lines (quotes) to find those that match specified category (preference)
            filter_lines = [line for line in lines if line.strip().endswith(f" : {category}")]
            # Making sure filter_lines returns correctly
            if filter_lines:
                # Using random to generate a random quote from filter list
                random_line = random.choice(filter_lines)
                # Printing the quote from filter lines list (category)
                quote_text, category = random_line.strip().split(" : ")
                print(quote_text)
            else:
                print("Sorry, that is not an avalaible category! Please check the spelling is correct or enter an avaliable category!")
    except IOError as e:
        print(f"An error occurred while generating random quote: {e}")
        return None
    
def display_quote():
    try:
        categories = get_categories()
        print("Choose an avaliable category to recieve a quote, or we can surprise you!")
        preference = input("Enter 'category' or 'surprise' to get a quote:  ").strip().capitalize()

        if preference == "Surprise" :
            get_random_quote()
        elif preference == "Motivation" or "Inspiration" or "Mindfulness" or "Positivity" or "Happiness":
            get_quote_from_preference(preference)
        else:
            print(f"{preference} is not an avaliable category. Please choose a category from the list or type 'suprise' for a random quote")
    except Exception as e:
        print(f"An error occurred : {e}")

def print_all_from_category():
    try:
        # Prints all the quote categories avliable
        print("Print all quotes in category")
        get_categories()
        # Prompt for user to input a category
        category = input("Please enter a category to display all quotes: ").strip().capitalize()
        # Open the txt file (quotes.txt) in read mode to read all existing lines (quotes)
        with open("src/quote.txt", "r") as file:
            lines = file.readlines()
        # Searching quotes line by line to the specified category
        category_quotes = [line.strip() for line in lines if line.strip().endswith(f" : {category}")]
        # Printing all the quotes under the specified category
        if category_quotes:
            print(f"All quotes under the category : {category} : ")
            for quote in category_quotes:
                print(quote.split(" : ")[0])
        # Message to catch an error of invalid category
        else:
            print(f"No quotes under the category : {category} : ")
    except Exception as e:
        print(f"An error occurred : {e} Please double check input is correct, and try again!")


def add_my_own_quote():
    try:
        quote_text = input("Enter your quote here:  ").strip()
        category = input("Enter a category for the quote:  ").strip().capitalize()
        # Open the txt file (quote.txt) in append mode and add the new quote into it
        with open("src/quote.txt", "a") as file:
            file.write(f"{quote_text} : {category}\n")
        print("Your quote has been added!")
    except Exception as e:
     print(f"An error occurred : {e} Please double check input is correct, and try again!")
        
def remove_quote():
    try:
        # Ask the user input the quote they want to remove
        quote_text = input("Enter the quote you would like to remove:  ").strip().capitalize()
        # Open the txt file (quotes.txt) in read more to read all existing lines (quotes)
        with open("src/quote.txt", "r") as file:
            lines = file.readlines()
        # Filter (find) the quote to be removed
        filtered_lines = [line for line in lines if line.strip().split(" : ")[0].capitalize() != quote_text]
        # Confirming that the quote has been removed
        if len(lines) ==len(filtered_lines):
            print("Sorry, the entered quote does not exist! Please double check you entered an existing quote!")
        # Remaining quotes back to the text file (quotes.txt)
        else:
            with open("src/quote.txt", "w") as file:
                file.writelines(filtered_lines)
                print("Your quote has been removed!")
    except Exception as e:
        print(f"An error occurred while removing quote : {e} Please double check input is correct, and try again!")

def edit_quote():
    try:
        print("Edit Quote Options")
        print("Would you like to add or remove a quote?")
        choice = input("Please enter 'Add' or 'Remove' :   ").strip().capitalize()

        if choice == "Add":
            add_my_own_quote()
        elif choice == "Remove":
            print("Do you know what quote you want to remove?")
            decision = input("Enter 'Yes' or 'No' : ").strip().capitalize()
            if decision == "Yes":
                remove_quote()
            elif decision == "No":
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
            print(f"{choice} is invlaid. Please try again and choose from the avaliable options!")
    except Exception as e:
        print(f"An error occurred : {e} Please double check input is correct, and try again!")

edit_quote()
