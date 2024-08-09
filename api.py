import requests

API_KEY = 'SBBSF3RLWB0PQ6E6'  # Your API key from Alpha Vantage
BASE_URL = 'https://www.alphavantage.co/query'  # Alpha Vantage base URL

def get_stock_price(symbol):
    """
    Fetches the current price of a stock given its symbol.

    Parameters:
        symbol (str): The stock ticker symbol (e.g., 'AAPL' for Apple Inc.).

    Returns:
        float: The latest stock price if available, otherwise None.
    """
    # Construct the URL for the API request
    url = f'{BASE_URL}?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={API_KEY}'
    
    # Send the request to the API
    response = requests.get(url)
    
    # Parse the JSON response
    data = response.json()
    
    # Extract the latest stock price from the response data
    try:
        # Get the most recent timestamp from the time series data
        latest_time = list(data['Time Series (1min)'].keys())[0]
        
        # Access the stock price data at the latest timestamp
        latest_data = data['Time Series (1min)'][latest_time]
        
        # Return the 'open' price as a float
        return float(latest_data['1. open'])
    
    except KeyError:
        # Handle errors, such as an invalid stock symbol or API response issues
        print("Error fetching data. Please check the stock symbol and try again.")
        return None
