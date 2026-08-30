# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 170,
    "AMZN": 190
}


def calculate_portfolio():
    portfolio = {}

    print("=" * 50)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 50)

    print("\nAvailable Stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock} - ${price}")

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("❌ Stock not available. Please select from the list.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))

            if quantity <= 0:
                print("❌ Quantity must be greater than 0.")
                continue

            portfolio[stock] = portfolio.get(stock, 0) + quantity

            print(f"✅ Added {quantity} shares of {stock}")

        except ValueError:
            print("❌ Please enter a valid number.")


    # Check if portfolio is empty
    if not portfolio:
        print("\nNo stocks were added.")
        return

    # Calculate total investment
    total_investment = 0

    print("\n" + "=" * 50)
    print("             PORTFOLIO SUMMARY")
    print("=" * 50)

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        value = price * quantity

        total_investment += value

        print(
            f"{stock}: {quantity} shares × "
            f"${price} = ${value:.2f}"
        )

    print("-" * 50)
    print(f"TOTAL INVESTMENT: ${total_investment:.2f}")
    print("=" * 50)

    # Save result to a text file
    with open("portfolio_report.txt", "w") as file:

        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 40 + "\n")

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]
            value = price * quantity

            file.write(
                f"{stock}: {quantity} shares × "
                f"${price} = ${value:.2f}\n"
            )

        file.write("-" * 40 + "\n")
        file.write(
            f"TOTAL INVESTMENT: ${total_investment:.2f}\n"
        )

    print("\n📄 Report saved as portfolio_report.txt")


# Start the program
if __name__ == "__main__":
    calculate_portfolio()