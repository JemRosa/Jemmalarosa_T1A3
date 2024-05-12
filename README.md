# T1A3

Mindset Terminal Application

The Mindset Terminal Application is a Python-based program designed to provide users with motivational quotes, allowing them to manage quotes and categories, add their own quotes, search for specific quotes, and more, all from the comfort of their terminal.

Features

1. Generate Random Quote
Generate Random Quote function selects a random quote from the quote.txt file. It first reads the content of a file containing quotes, selects a random line from that file, then extracts and prints the quote from that line. This function helps users discover new quotes or find inspiration by presenting them with a random quote each time it's called.
Logic Walkthrough:
The function opens the quote.txt file and reads its content.
It then picks a random line from the file.
After splitting the line into the quote text and category, it prints the quote.
Variables and Scope: lines, random_line, quote_text, and category are used within the function.
Loops and Conditional Control Structures: The function doesn't use loops but includes error handling using try-except blocks for file-related errors.
Error Handling: Handles FileNotFoundError, IOError, and generic Exception errors that may occur during file reading.

2. Get Quote from Preference
The Get Quote from Preference function allows users to request a quote from a specific category. It reads a file containing quotes, filters the quotes based on the user's specified category, and then randomly selects and prints a quote from that category. If the specified category does not exist in the collection, it notifies the user that the category is unavailable. This function enables users to receive quotes tailored to their preferences, promoting a more personalised experience with the application.
Logic Walkthrough:
Similar to the random quote feature, this function reads quote.txt and filters lines based on the specified category.
If quotes are found in the specified category, it selects a random quote and prints it.
If the category is not found, it informs the user accordingly.
Variables and Scope: lines, filter_lines, random_line, quote_text, and category are used within the function.
Loops and Conditional Control Structures: Uses list comprehensions to filter lines based on the specified category.
Error Handling: Includes error handling for file-related errors.

3. Get Categories
The Get Categories function retrieves all unique categories from the quote database. It reads through the quote.txt file, identifies and separates the categories associated with each quote, and then presents them to the user. These categories are categorised into ‘base’ categories, which are predefined, and user-added categories. This feature provides users with insight into the available categories, helping them navigate and explore the diverse range of quotes stored in the application.
Logic Walkthrough:
Opens quote.txt and reads its content.
Collects categories from each line, distinguishing between base categories and user-added ones.
Prints all base and user-added categories.
Variables and Scope: lines, base_categories, user_categories, and category are used within the function.
Loops and Conditional Control Structures: Uses loops to iterate over lines and conditional statements to differentiate categories.
Error Handling: Includes error handling for file-related errors.

4. Print All from Category
The Print All from Category function allows users to view all quotes stored under a specific category. It begins by presenting the user with a list of available categories to choose from. After the user selects a category, the function reads the quote.txt file, filters the lines based on the chosen category, and then prints all the quotes belonging to that category. This feature provides users with the ability to explore quotes within a particular theme or subject, facilitating focused reflection or inspiration.
Logic Walkthrough:
Displays available categories.
Prompts the user to enter a category.
Filters lines based on the category and prints all quotes under it.
Variables and Scope: lines, category, and category_quotes are used within the function.
Loops and Conditional Control Structures: Uses loops to iterate over lines and conditional statements to filter quotes.
Error Handling: Includes error handling for file-related errors.

5. Remove Category
The Remove Category function enables users to delete categories that they have previously added to the Mindset Application. First, it displays all categories available, distinguishing between base categories and user-added ones. Then, it prompts the user to select a category to remove. If the chosen category is a user-added one, it removes it from the quote.txt file. This feature offers users control over the categories present in the application, allowing them to customise their experience according to their preferences and interests.
Logic Walkthrough:
Displays all categories.
Prompts the user to choose a category to remove.
Removes the chosen category from quote.txt.
Variables and Scope: base_categories, user_choice, category_choice, and update_lines are used within the function.
Loops and Conditional Control Structures: Uses conditional statements to determine user choices.
Error Handling: Includes error handling for file-related errors.

6. Edit Categories
The Edit Categories function provides users with the capability to manage categories within the Mindset Application. It presents users with options to either view existing categories or edit them. If users choose to edit, they can add a new category or remove an existing one. This feature enhances the flexibility of the application, empowering users to tailor their experience by organising and customising categories based on their interests and preferences.
Logic Walkthrough:
Prompts the user to view or edit categories.
Based on the choice, displays categories or proceeds to edit.
Editing options include adding or removing categories.
Variables and Scope: user_choice, category, confirm, and update_lines are used within the function.
Loops and Conditional Control Structures: Uses conditional statements to determine user choices and perform actions accordingly.
Error Handling: Includes error handling for file-related errors and invalid inputs.

7. Add Own Quote
Add Own Quote function enables users to contribute their own quotes to the Mindset Application. Users are prompted to input a new quote along with its corresponding category. The function then validates the input and, if it meets the criteria, appends the new quote to the quote.txt file. This feature encourages user engagement and allows for the expansion of the application's quote database with personalised contributions from users.
Logic Walkthrough:
Prompts the user to enter a new quote and its category.
Validates input and appends the new quote to quote.txt.
Variables and Scope: new_quote and category are used within the function.
Loops and Conditional Control Structures: Includes conditional statements to validate user input.
Error Handling: Ensures both quote and category inputs are provided.

8. Remove Quote
The Remove Quote function allows users to delete a quote from the quote.txt file. Users first choose a category to display quotes from. Then, they select a specific quote from the displayed list to remove. Once the user confirms the deletion, the selected quote is removed from the file. This feature provides users with the ability to manage the content of the application by removing quotes they no longer wish to have included.
Logic Walkthrough:
Prompts the user to choose a category to display quotes.
Displays quotes under the chosen category.
User selects a quote to remove, and it's deleted from quote.txt.
Variables and Scope: category, quote_choice, and update_lines are used within the function.
Loops and Conditional Control Structures: Uses loops and conditionals to display quotes and handle user choices.
Error Handling: Handles file-related errors and invalid inputs.

9. Edit Quote
The Edit Quote function enables users to modify existing quotes by either removing them or adding new ones. Users start by choosing a category to display quotes from. After selecting a specific quote, they have the option to remove it from the file. Alternatively, they can choose to add a new quote to the selected category. This feature allows users to actively curate the content of the application, ensuring that it reflects their preferences and interests.
Logic Walkthrough:
Prompts the user to choose a category to display quotes.
Displays quotes under the chosen category.
User selects a quote to edit, and they can remove it or add a new one.
Variables and Scope: category, quote_choice, edit_choice, and update_lines are used within the function.
Loops and Conditional Control Structures: Uses loops and conditionals to display quotes and handle user choices.
Error Handling: Handles file-related errors and invalid inputs.

10. Search Quotes
The Search Quotes function empowers users to find specific quotes by entering keywords. Once prompted, users input the keywords they want to search for. The function then scans all the quotes stored in the application's database, filtering and displaying only those that contain the provided keywords. This feature offers users a convenient way to retrieve relevant quotes based on their interests or needs.
Logic Walkthrough:
Prompts the user to enter keywords to search for.
Searches quote.txt for quotes containing the provided keywords and prints matching quotes.
Variables and Scope: search_query and matching_quotes are used within the function.
Loops and Conditional Control Structures: Uses loops to iterate over quotes and conditionals to filter matching quotes.
Error Handling: Handles file-related errors.

11. Display Help
The Display Help function serves as a guide for users by presenting information stored in the help.txt file. It opens the help file, reads its content, and then displays this information to the user. This feature assists users in understanding how to navigate and utilise the Mindset Application effectively.
Logic Walkthrough:
Opens help.txt and reads its content.
Prints the help information to the user.
Variables and Scope: help_content is used within the function.
Loops and Conditional Control Structures: No loops used, includes error handling for file-related errors.
Error Handling: Handles FileNotFoundError and IOError while reading the help file.

12. Main Menu
The Main Menu function acts as the central hub for the Mindset Application, offering users a structured interface to access various features. It presents a numbered list of options to the user, prompting them to choose an action. Based on the user's selection, the function executes corresponding functionalities such as generating random quotes, managing quotes and categories, adding new quotes, searching quotes, displaying help information, or exiting the application. The function continues running in a loop until the user decides to exit the application. It incorporates error handling to manage any unexpected exceptions that may occur during the execution of menu options.
Logic Walkthrough:
Displays numbered menu options.
Prompts the user to choose an option and executes the corresponding functionality.
Continues until the user chooses to exit.
Variables and Scope: running and user_choice are used within the function.
Loops and Conditional Control Structures: Uses a while loop to keep the application running and conditionals to execute different functionalities based on user choices.
Error Handling: Includes error handling for any exceptions during menu option execution.

Resources and Style Guide
The application will adhere to the PEP8 (Python Enhancement Proposal 8) code style guide for Python projects.
PEP8 provides guidelines for writing clean, readable, and maintainable Python code.in PEP8: <https://pep8.org/>

Source Control Repository
<git@github.com>:JemRosa/Jemmalarosa_T1A3.git

Implementation Plan
Please see attached PDF file in docs folder. <Jemmalarosa_T1A3/docs/Implementation Plan for Mindset Application.pdf>

Installation
Please also see more installation information in <Jemmalarosa_T1A3/docs/help.md>

1. Clone the repository to your local machine
git clone <git@github.com>:JemRosa/Jemmalarosa_T1A3.git

2. Navigate to the project directory:
cd Jemmalarosa_T1A3

3. Install the required dependencies:
pip install -r requirements.txt

4. Run the application:
python main.py


For Windows Users:
Setup Script: Navigate to the extracted folder and double-click on setup_project.bat. This script creates a virtual environment and installs all necessary dependencies.

For macOS/Linux Users:
Setup Script: Open a terminal, navigate to the extracted folder, make the script executable with chmod +x setup_project.sh, and execute it by typing ./setup_project.sh.

Starting the Application:
Windows: Activate the virtual environment with myenv\Scripts\activate then start the application with python app.py.
macOS/Linux: Activate the virtual environment with source myenv/bin/activate then start the application with python app.py.

Dependencies:
Python 3.x
The application requires Python 3.x. It utilizes built-in Python modules,specifically 'random', hence no additional packages are necessary. Ensure Python 3.x is installed on your system.
You can download it from the official Python website: <https://www.python.org/downloads/>

Using Mindset Terminal Application
Upon running the application, you will be presented with a main menu where you can choose various options to interact with the application's features. Simply follow the prompts to navigate through the menu and utilize the desired functionalities.
More information reagarding application use is avaliable in -  <Jemmalarosa_T1A3/docs/help.md>

## Project Setup Scripts
This project includes two scripts to automate the setup process:

- **setup_application.bash** for Unix-based systems (macOS, Linux)
  - This script creates a Python virtual environment, activates it, and installs all required dependencies from the `requirements.txt` file.

- **setup_application.bat** for Windows
  - Similar to the Unix script, it sets up and activates a virtual environment and installs necessary dependencies.

To use these scripts, run the appropriate one for your operating system after cloning the project repository.
Breief instructions are avaliable above, or further information and instructions are avaliable in <Jemmalarosa_T1A3/docs/help.md>.
