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


