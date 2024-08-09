f = open("portfolio.py", "r")  # Open the 'portfolio.py' file in read mode

data = f.readline()  # Read the first line from the file and store it in the variable 'data'

# Store the first line from 'portfolio.py' in the variable 'portfolio'
portfolio = data

# Import the functions add_stock, remove_stock, and display_portfolio from the 'portfolio.py' module
from portfolio import add_stock, remove_stock, display_portfolio

def menu():
    """
    Displays the menu and handles user input.

    Functionality:
        Provides a user interface for managing the stock portfolio. Users can choose to add a stock,
        remove a stock, display the portfolio, or exit the program. The appropriate functions are called
        based on the user's input.
    """
    while True:  # Start an infinite loop to continuously display the menu until the user exits
        # Display the menu options
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Exit")
        
        # Get the user's choice and strip any leading/trailing whitespace
        choice = input("Choose an option: ").strip()
        
        # Handle the user's choice
        if choice == '1':
            # If the user chooses to add a stock
            symbol = input("Enter stock symbol: ").strip().upper()  # Get the stock symbol and convert it to uppercase
            quantity = int(input("Enter quantity: ").strip())  # Get the quantity as an integer
            add_stock(symbol, quantity)  # Call the add_stock function to add the stock to the portfolio
        elif choice == '2':
            # If the user chooses to remove a stock
            symbol = input("Enter stock symbol to remove: ").strip().upper()  # Get the stock symbol to remove
            remove_stock(symbol)  # Call the remove_stock function to remove the stock from the portfolio
        elif choice == '3':
            # If the user chooses to display the portfolio
            display_portfolio()  # Call the display_portfolio function to show the current portfolio
        elif choice == '4':
            # If the user chooses to exit
            print("Exiting...")  # Display an exit message
            break  # Exit the loop and end the program
        else:
            # If the user enters an invalid option
            print("Invalid option. Please try again.")  # Display an error message

if __name__ == "__main__":
    menu()  # Call the menu function to start the program
