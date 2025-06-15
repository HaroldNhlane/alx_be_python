# No import statement here for BankAccount itself
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
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self._account_balance = initial_balance  # Using a protected attribute for encapsulation

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be a positive number.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self._account_balance += amount
        print(f"Successfully deposited: ${amount:.2f}")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw. Must be a positive number.

        Returns:
            bool: True if the withdrawal was successful, False otherwise (insufficient funds).
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if amount > self._account_balance:
            print("Insufficient funds.")
            return False
        else:
            self._account_balance -= amount
            print(f"Successfully withdrew: ${amount:.2f}")
            return True

    def display_balance(self):
        """
        Displays the current balance of the account in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")