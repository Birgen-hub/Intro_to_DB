import sys
# Import the BankAccount class from the bank_account module
try:
    from bank_account import BankAccount
except ImportError:
    # Handle case where bank_account.py might not be in the direct path
    # Assuming run from the root directory for this setup
    # For submission, modules must be importable by the checker.
    print("Error: Could not import BankAccount class. Ensure bank_account.py is accessible.")
    sys.exit(1)


def main():
    """
    Handles command line arguments to perform banking operations 
    using the BankAccount class.
    """

    # Initialize account with a starting balance of 100 for testing purposes
    account = BankAccount(100)  

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount/None>")
        print("Commands: deposit:<amount>, withdraw:<amount>, display")
        sys.exit(1)

    # Parse command and optional parameters
    # Example sys.argv[1] can be "deposit:50" or "display"
    try:
        command_parts = sys.argv[1].split(':')
        command = command_parts[0].lower()

        # Check for amount parameter and convert it
        amount = None
        if len(command_parts) > 1 and command_parts[1].strip():
            try:
                amount = float(command_parts[1])
            except ValueError:
                print("Error: Amount must be a valid number.")
                sys.exit(1)

    except IndexError:
        print("Error: Invalid command format.")
        sys.exit(1)

    # Execute commands
    if command == "deposit" and amount is not None:
        if amount > 0:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Error: Deposit amount must be positive.")

    elif command == "withdraw" and amount is not None:
        if amount > 0:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Error: Withdrawal amount must be positive.")

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command or missing amount.")
        print("Usage: python main-0.py <command>:<amount/None>")
cat << EOF > programming_paradigm/main-0.py
import sys
# Import the BankAccount class from the bank_account module
try:
    from bank_account import BankAccount
except ImportError:
    # Handle case where bank_account.py might not be in the direct path
    # Assuming run from the root directory for this setup
    # For submission, modules must be importable by the checker.
    print("Error: Could not import BankAccount class. Ensure bank_account.py is accessible.")
    sys.exit(1)


def main():
    """
    Handles command line arguments to perform banking operations 
    using the BankAccount class.
    """

    # Initialize account with a starting balance of 100 for testing purposes
    account = BankAccount(100)  

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount/None>")
        print("Commands: deposit:<amount>, withdraw:<amount>, display")
        sys.exit(1)

    # Parse command and optional parameters
    # Example sys.argv[1] can be "deposit:50" or "display"
    try:
        command_parts = sys.argv[1].split(':')
        command = command_parts[0].lower()

        # Check for amount parameter and convert it
        amount = None
        if len(command_parts) > 1 and command_parts[1].strip():
            try:
                amount = float(command_parts[1])
            except ValueError:
                print("Error: Amount must be a valid number.")
                sys.exit(1)

    except IndexError:
        print("Error: Invalid command format.")
        sys.exit(1)

    # Execute commands
    if command == "deposit" and amount is not None:
        if amount > 0:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Error: Deposit amount must be positive.")

    elif command == "withdraw" and amount is not None:
        if amount > 0:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Error: Withdrawal amount must be positive.")

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command or missing amount.")
        print("Usage: python main-0.py <command>:<amount/None>")


if __name__ == "__main__":
    main()
