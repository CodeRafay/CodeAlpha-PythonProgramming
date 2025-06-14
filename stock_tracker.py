# Stock Portfolio Tracker
# A simple command-line stock portfolio tracker that allows users to input stock symbols and quantities, calculates the total investment value, and saves the portfolio to a CSV file.
import csv

# Hardcoded stock prices (USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 120,
    "MSFT": 310,
    "NFLX": 430
}


def get_portfolio():
    portfolio = {}
    print("Enter your stocks (type 'done' to finish):")
    while True:
        stock = input("Stock symbol (e.g., AAPL): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Stock not found in price list. Try again.")
            continue
        try:
            quantity = int(input(f"Quantity of {stock}: "))
            if quantity < 0:
                print("Quantity can't be negative.")
                continue
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("Please enter a valid number.")
    return portfolio


def calculate_total(portfolio):
    total = 0
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        print(f"{stock}: {qty} shares x ${price} = ${value}")
        total += value
    print(f"\nTotal Investment Value: ${total}")
    return total


def save_to_file(portfolio, total, filename="portfolio.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            writer.writerow([stock, qty, price, value])
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total])
    print(f"\nPortfolio saved to {filename}")


def main():
    print("📈 Stock Portfolio Tracker 📈")
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price}")
    print()

    portfolio = get_portfolio()
    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    total = calculate_total(portfolio)

    save_choice = input(
        "\nDo you want to save your portfolio to a file? (y/n): ").lower()
    if save_choice == 'y':
        save_to_file(portfolio, total)


if __name__ == "__main__":
    main()


# GUI + Live Stock Price Tracker
'''

import tkinter as tk
from tkinter import messagebox
import requests
import pandas as pd

# Alpha Vantage API key , get yours from https://www.alphavantage.co/support/#api-key
# Note: The API key should be kept secret and not hardcoded in production code.
# sample API key for testing purposes :   N4FZXSIAWYFNU07Q

API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key
#You can make up to 500 requests per day and 5 per minute with the free tier.
#If you exceed the limit, you'll get a Note or error in the API response.

# Function to fetch real-time stock price

def fetch_price(symbol):
    url = f'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '1min',
        'apikey': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    try:
        latest_time = list(data['Time Series (1min)'].keys())[0]
        latest_close = data['Time Series (1min)'][latest_time]['4. close']
        return float(latest_close)
    except KeyError:
        return None

# Function to add stock to portfolio


def add_stock():
    symbol = symbol_entry.get().upper()
    quantity = quantity_entry.get()
    if not symbol or not quantity.isdigit():
        messagebox.showerror(
            "Input Error", "Please enter valid symbol and quantity.")
        return
    quantity = int(quantity)
    price = fetch_price(symbol)
    if price is None:
        messagebox.showerror(
            "API Error", f"Failed to fetch data for {symbol}.")
        return
    portfolio[symbol] = {'quantity': quantity, 'price': price}
    update_display()

# Function to update the display


def update_display():
    for widget in frame.winfo_children():
        widget.destroy()
    total_value = 0
    for symbol, data in portfolio.items():
        current_value = data['quantity'] * data['price']
        total_value += current_value
        tk.Label(
            frame, text=f"{symbol}: {data['quantity']} shares @ ${data['price']} = ${current_value}").pack()
    total_label.config(text=f"Total Portfolio Value: ${total_value}")
    save_button.config(state=tk.NORMAL)

# Function to save portfolio to CSV


def save_to_csv():
    data = []
    for symbol, data_dict in portfolio.items():
        data.append([symbol, data_dict['quantity'], data_dict['price']])
    df = pd.DataFrame(data, columns=['Symbol', 'Quantity', 'Price'])
    df.to_csv('portfolio.csv', index=False)
    messagebox.showinfo("Saved", "Portfolio saved to portfolio.csv")


# Initialize main window
root = tk.Tk()
root.title("Stock Portfolio Tracker")

# Portfolio dictionary
portfolio = {}

# Input fields
symbol_label = tk.Label(root, text="Stock Symbol:")
symbol_label.pack()
symbol_entry = tk.Entry(root)
symbol_entry.pack()

quantity_label = tk.Label(root, text="Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

add_button = tk.Button(root, text="Add Stock", command=add_stock)
add_button.pack()

# Display frame
frame = tk.Frame(root)
frame.pack()

# Total value label
total_label = tk.Label(root, text="Total Portfolio Value: $0")
total_label.pack()

# Save button
save_button = tk.Button(root, text="Save Portfolio",
                        command=save_to_csv, state=tk.DISABLED)
save_button.pack()

# Run the application
root.mainloop()

'''
