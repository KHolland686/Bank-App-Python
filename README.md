# Bank-App-Python
# Banking Application
Version 1 of a Python-based banking application for basic financial transactions.

## Features
- Account Management: Open, close, and inquire about account details.
- Transaction Operations: Deposit, withdraw, transfer money, simulate ATM withdrawals.
- Interest Calculation: Monthly interest added based on the provided annual interest rate.
- Change Deposits: Ability to deposit coins, with automatic balance calculation.

## Usage
1. Clone this repository
2. Run the application BankManager.py
  ```bash
  python BankManager.py
  ```
3. Follow the on-screen prompts to perform various banking transactions.

## Code Organization
The code is structured using classes for modularity and readability:
  `BankUtility`: Helper methods for user input and common tasks.  
  `CoinCollector`: Class for simulating coin deposits.  
  `Account`: Represents an individual bank account.  
  `Bank`: Manages a collection of accounts.  
  `BankManager`: Orchestrates user interactions and serves as the main program.  
