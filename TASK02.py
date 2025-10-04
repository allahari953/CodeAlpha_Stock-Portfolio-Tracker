# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 310,
    "AMZN": 140
}

portfolio = {}
total_value = 0

print("📈 Welcome to Stock Portfolio Tracker")

# Input stock holdings
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock in stock_prices:
        try:
            qty = int(input(f"Enter quantity for {stock}: "))
            portfolio[stock] = qty
            total_value += stock_prices[stock] * qty
        except ValueError:
            print("❌ Invalid quantity. Please enter a number.")
    else:
        print("❌ Stock not found in price list.")

# Display result
print("\n📊 Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    print(f"{stock} - Qty: {qty} | Price: ${price} | Value: ${price * qty}")

print(f"\n💰 Total Investment Value: ${total_value}")

# Save to file (optional)
save = input("\nDo you want to save the summary to a file? (y/n): ").lower()
if save == 'y':
    filename = "portfolio_summary.txt"
    with open(filename, 'w') as file:
        file.write("Stock Portfolio Summary\n\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            file.write(f"{stock} - Qty: {qty} | Price: ${price} | Value: ${price * qty}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print(f"✅ Summary saved to {filename}")
