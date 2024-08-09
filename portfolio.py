f = open("api.py", "r")  # Open the 'api.py' file in read mode

# Read the first line from the file and store it in the variable 'data'
data = f.readline()

# Store the first line from 'api.py' in the variable 'api'
api = data

# Import the get_stock_price function from the 'api.py' module
from api import get_stock_price

# In-memory storage for the stock portfolio, represented as a dictionary
portfolio = {}

def add_stock(symbol, quantity):
    """
    Adds a stock to the portfolio.

    Parameters:
        symbol (str): The stock ticker symbol (e.g., 'AAPL').
        quantity (int): The number of shares to add.

    Functionality:
        Fetches the current stock price using the get_stock_price function, then adds
        the stock to the portfolio dictionary with its symbol as the key, and stores
        the quantity and price as values.
    """
    price = get_stock_price(symbol)  # Get the current price of the stock
    portfolio[symbol] = {'quantity': quantity, 'price': price}  # Add stock details to the portfolio
    print(f"Added {quantity} of {symbol} at ${price:.2f} per share.")  # Display confirmation message

def remove_stock(symbol):
    """
    Removes a stock from the portfolio.

    Parameters:
        symbol (str): The stock ticker symbol to be removed.

    Functionality:
        If the stock symbol exists in the portfolio, it removes the stock and displays
        a confirmation message. Otherwise, it informs the user that the stock was not found.
    """
    if symbol in portfolio:  # Check if the stock is in the portfolio
        del portfolio[symbol]  # Remove the stock from the portfolio
        print(f"Removed {symbol} from portfolio.")  # Display confirmation message
    else:
        print(f"{symbol} not found in portfolio.")  # Inform the user that the stock was not found

def display_portfolio():
    """
    Displays the current portfolio with stock symbols, quantities, and current prices.

    Functionality:
        Iterates through the portfolio dictionary and fetches the latest price for each stock.
        Displays the stock symbol, quantity, current price, and the total value of the holdings.
        If the portfolio is empty, it informs the user.
    """
    if not portfolio:  # Check if the portfolio is empty
        print("Portfolio is empty.")  # Inform the user that the portfolio is empty
        return
    
    print("\nCurrent Portfolio:")  # Display header for the portfolio
    for symbol, details in portfolio.items():  # Loop through each stock in the portfolio
        price = get_stock_price(symbol)  # Get the latest price of the stock
        total_value = price * details['quantity']  # Calculate the total value of the holdings
        print(f"{symbol}: {details['quantity']} shares @ ${price:.2f} each | Total Value: ${total_value:.2f}")
