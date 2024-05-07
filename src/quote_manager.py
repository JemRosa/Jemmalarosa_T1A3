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
    categories = set() #To avoid duplicate categories
    try:
        with open("src/quote.txt", "r") as file:
            for line in file:
                quote_text, category = line.strip().split(" : ")
                categories.add(category)
                print(categories)
                        
    except (IOError, ValueError) as e:
        print(f"An error occurred while generating random quote: {e}")
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
                print(f"No quotes found for category: {category}")
    except IOError as e:
        print(f"An error occurred while generating random quote: {e}")
        return None
    
get_quote_from_preference('Happiness')
get_categories()
