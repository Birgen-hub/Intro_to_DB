class BankAccount:
    """
    A simple bank account class demonstrating OOP concepts.
    It encapsulates account balance and provides methods for deposit,
    withdrawal, and balance display.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with an optional starting balance.

        Args:
            initial_balance (float, optional): The starting balance. Defaults to 0.
        """
        # Use a private-like attribute (conventionally starts with _) for encapsulation
        if initial_balance < 0:
            print("Warning: Initial balance cannot be negative. Setting to 0.")
            self._account_balance = 0.0
        else:
            self._account_balance = float(initial_balance)

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts the amount from the balance if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        # Use .2f to format the currency nicely
        print(f"Current Balance: ${self._account_balance:.2f}")

if __name__ == "__main__":
    # Basic demonstration for direct execution test
    my_account = BankAccount(100.50)
    my_account.display_balance()
    my_account.deposit(50.0)
    my_account.display_balance()
    my_account.withdraw(25.0)
    my_account.display_balance()
    if not my_account.withdraw(500.0):
        print("Failed to withdraw 500.0 (Insufficient funds).")

