📊 Stock Portfolio Tracker

A simple Python-based Stock Portfolio Tracker that calculates the total investment value based on manually defined stock prices and the quantity of shares entered by the user.

🚀 Features
📈 Uses a predefined dictionary of stock prices.
💰 Accepts stock symbols and quantities from the user.
🧮 Calculates the value of each stock holding.
📊 Calculates the total portfolio investment.
📄 Automatically saves the portfolio summary to a text file.
❌ Validates invalid stock names and quantities.
🖥️ Uses a simple console-based interface.
🛠️ Technologies Used
Python 3
Dictionaries
Functions
input() / output
Arithmetic operations
while loops
Conditional statements
Exception handling
File handling
📋 Available Stocks

The project uses manually defined stock prices:

Stock	Price
AAPL	$180
TSLA	$250
MSFT	$420
GOOGL	$170
AMZN	$190

Note: These are hardcoded sample prices for the internship task and are not live market prices.

📂 Project Structure
Task2_Stock_Portfolio_Tracker/
│
├── stock_tracker.py
├── portfolio_report.txt
└── README.md
▶️ How to Run
Step 1: Install Python

Make sure Python 3 is installed on your computer.

Step 2: Open the project

Open the Task2_Stock_Portfolio_Tracker folder in VS Code.

Step 3: Run the program

Open the terminal and execute:

python stock_tracker.py
💻 Example
Available Stocks:
AAPL - $180
TSLA - $250
MSFT - $420
GOOGL - $170
AMZN - $190

Enter stock symbol (or 'done' to finish): AAPL
Enter quantity of AAPL: 5

Enter stock symbol (or 'done' to finish): TSLA
Enter quantity of TSLA: 2

Enter stock symbol (or 'done' to finish): done

PORTFOLIO SUMMARY

AAPL: 5 shares × $180 = $900.00
TSLA: 2 shares × $250 = $500.00

TOTAL INVESTMENT: $1400.00

Report saved as portfolio_report.txt
📄 Output File

After completing the portfolio, the program automatically creates:

portfolio_report.txt

The file contains the stock details and total investment amount.

🎯 Learning Outcomes

This project demonstrates practical use of:

Python dictionaries
User input and output
Loops and conditions
Functions
Basic arithmetic
Input validation
File handling
