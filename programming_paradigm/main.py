import sys
from bank_account import BankAccount

def main():
    """
    Main function to handle command-line interactions with the BankAccount.
    """
    # Initialize the account with an example starting balance.
    # You can change this balance as needed for testing different scenarios.
    try:
        account = BankAccount(100.00)
    except (TypeError, ValueError) as e:
        print(f"Error initializing account: {e}")
        sys.exit(1)

    # Check if enough command-line arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>[:<amount>]")
        print("Commands:")
        print("  deposit:<amount>   - Deposit funds into the account (e.g., deposit:50)")
        print("  withdraw:<amount>  - Withdraw funds from the account (e.g., withdraw:20)")
        print("  display            - Display the current account balance")
        sys.exit(1) # Exit with an error code

    # Parse the command and optional amount from the command-line argument
    command_input = sys.argv[1]
    command_parts = command_input.split(':')
    command = command_parts[0].lower() # Convert command to lowercase for case-insensitivity

    amount = None
    if len(command_parts) > 1:
        try:
            amount = float(command_parts[1])
        except ValueError:
            print(f"Error: Invalid amount '{command_parts[1]}'. Amount must be a number.")
            sys.exit(1)

    # Execute the appropriate bank operation based on the command
    if command == "deposit":
        if amount is not None:
            try:
                account.deposit(amount)
                # This is the single print statement for successful deposit
                print(f"Deposited: ${amount:.1f}") # Changed to .1f for "67.0" format
            except (TypeError, ValueError) as e:
                print(f"Error depositing: {e}")
        else:
            print("Error: Deposit command requires an amount (e.g., deposit:50).")
    elif command == "withdraw":
        if amount is not None:
            try:
                if account.withdraw(amount):
                    # This is the single print statement for successful withdrawal
                    print(f"Withdrew: ${amount:.1f}") # Changed to .1f for "20.0" format
                else:
                    print("Insufficient funds.") # Already handled in withdraw method, but good to reinforce
            except (TypeError, ValueError) as e:
                print(f"Error withdrawing: {e}")
        else:
            print("Error: Withdraw command requires an amount (e.g., withdraw:20).")
    elif command == "display":
        if amount is None: # Ensure no extra arguments for display command
            account.display_balance()
        else:
            print("Error: Display command does not take an amount.")
    else:
        print(f"Error: Invalid command '{command}'.")
        print("Commands: deposit, withdraw, display")

if __name__ == "__main__":
    main()