import sys
from bank_account import BankAccount
from robust_division_calculator import safe_divide


def main():
    """
    Main function to handle command-line interactions with BankAccount
    and perform division operations.
    """
    # Initialize the account with an example starting balance.
    # You can change this balance as needed for testing different scenarios.
    try:
        account = BankAccount(100.00)
    except (TypeError, ValueError) as e:
        print(f"Error initializing account: {e}")
        sys.exit(1)

    # --- Command Line Argument Handling ---
    # The first argument is always the command (e.g., 'deposit', 'withdraw', 'display', 'divide')
    if len(sys.argv) < 2:
        print("Usage:")
        print("  For Bank Account: python main.py <command>:<amount>")
        print("    Commands: deposit, withdraw, display")
        print("  For Division:     python main.py divide <numerator> <denominator>")
        sys.exit(1)

    command_full = sys.argv[1]
    command_parts = command_full.split(':')
    command = command_parts[0].lower() # Primary command (e.g., 'deposit', 'divide')

    # --- Bank Account Operations ---
    if command in ["deposit", "withdraw", "display"]:
        amount = None
        if len(command_parts) > 1:
            try:
                amount = float(command_parts[1])
            except ValueError:
                print(f"Error: Invalid amount '{command_parts[1]}'. Amount must be a number.")
                sys.exit(1)
        elif command != "display": # Deposit/withdraw without amount is an error
             print(f"Error: '{command}' command requires an amount (e.g., {command}:50).")
             sys.exit(1)

        if command == "deposit":
            try:
                account.deposit(amount)
                print(f"Deposited: ${amount:.1f}")
            except (TypeError, ValueError) as e:
                print(f"Error depositing: {e}")
        elif command == "withdraw":
            try:
                if account.withdraw(amount):
                    print(f"Withdrew: ${amount:.1f}")
                else:
                    print("Insufficient funds.")
            except (TypeError, ValueError) as e:
                print(f"Error withdrawing: {e}")
        elif command == "display":
            if amount is None: # Ensure no extra arguments for display command
                account.display_balance()
            else:
                print("Error: Display command does not take an amount.")

    # --- Division Calculator Operation ---
    elif command == "divide":
        # For 'divide', we expect 3 arguments in total: script_name, 'divide', numerator, denominator
        if len(sys.argv) != 4:
            print("Usage: python main.py divide <numerator> <denominator>")
            sys.exit(1)

        numerator = sys.argv[2]
        denominator = sys.argv[3]

        result = safe_divide(numerator, denominator)
        print(result)

    # --- Invalid Command ---
    else:
        print(f"Error: Invalid command '{command}'.")
        print("Please use 'deposit', 'withdraw', 'display' for banking, or 'divide' for calculations.")
        print("Usage examples:")
        print("  python main.py deposit:50")
        print("  python main.py display")
        print("  python main.py divide 10 5")


if __name__ == "__main__":
    main()