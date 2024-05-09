import random
import quote_manager

def menu():
    """
    _summary_
    """
    try:
        while True:
            print("Mindset Application")
            print("Boost your mood, mindest or motivation!")
            print("1. Suprise me with a quote!")
            print("2. Choose a quote from a category!")
            print("3. Create your own quote!")
            print("4. Search all quotes!")
            print("5. Category Options - View, create or remove your own category!")
            print("6. View all quotes by category!")
            print("7. Exit Application")

            choice = input("Choose a number: ").strip()

            if choice == "1":
                quote_manager.get_random_quote()
                print("Need another boost? or head back to the Menu!")
                option = input("Enter 'Suprise' or 'Menu' : ").strip().capitalize()
                while option == "Suprise":
                    quote_manager.get_random_quote()
                    print("Need another boost? or head back to the Menu!")
                    option = input("Enter 'Suprise' or 'Menu' : ").strip().capitalize()
                    
            elif choice == "2":
                quote_manager.get_categories()
                preference = input("Please enter a category: ").capitalize()
                quote_manager.get_quote_from_preference(preference)
                print("Want to choose another category? or head back to the Menu!")
                option = input("Enter 'Another' or 'Menu' : ")
                while option == "Another":
                    quote_manager.get_categories()
                    preference = input("Please enter a category: ").capitalize()
                    quote_manager.get_quote_from_preference(preference)
                    print("Want to choose another category? or head back to the Menu!")
                    option = input("Enter 'Another' or 'Menu' : ")

            elif choice == "3":
                quote_manager.add_my_own_quote()
                print("Want to add another quote? or head back to the Menu!")
                option = input("Enter 'Add' or 'Menu' : ")
                while option == "Add":
                    quote_manager.add_my_own_quote()
                    print("Want to add another quote? or head back to the Menu!")
                    option = input("Enter 'Add' or 'Menu' : ")

            elif choice == "4":
                quote_manager.search_quotes()
            elif choice == "5":
                quote_manager.edit_categories()
            elif choice == "6":
                quote_manager.print_all_from_category()
            elif choice == "7":
                print("Thank you for using the Mindset Application!")
                break
            else:
                print(f"{choice} is invlaid. Please try again and choose from the avaliable options!")
    except Exception as e:
        print(f"An error occurred : {e} Please double check input is correct, and try again!")

menu()
