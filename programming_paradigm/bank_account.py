class BankAccount:
    """
    A class to represent a simple bank account.
    Encapsulates account balance and provides methods for banking operations.
    """
    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float, optional): The starting balance for the account. Defaults to 0.
        """
        # Input validation for initial_balance
        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Initial balance must be a number.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._account_balance = float(initial_balance) # Ensure it's stored as a float

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be a positive number.
        """
        # Input validation for deposit amount
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self._account_balance += amount
        # Removed the print statement from here.
        # The main script will handle printing the "Deposited" message.

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw. Must be a positive number.

        Returns:
            bool: True if the withdrawal was successful, False otherwise (insufficient funds).
        """
        # Input validation for withdrawal amount
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")

        if amount > self._account_balance:
            return False # Indicate insufficient funds without printing here
        else:
            self._account_balance -= amount
            return True # Indicate successful withdrawal

    def display_balance(self):
        """
        Displays the current balance of the account in a user-friendly format.
        """
        # Ensure consistent formatting with 2 decimal places
        print(f"Current Balance: ${self._account_balance:.2f}")