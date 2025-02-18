class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds or invalid amount.")

    def display_balance(self):
        print(f"Account balance: ${self.balance}")

    def transfer(self, amount, recipient_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            print(f"Transferred: ${amount} to Account {recipient_account.account_number}")
        else:
            print("Insufficient funds or invalid amount.")


def main():
    # Create a bank account
    account = BankAccount("123456789", "John Doe", 500)

    while True:
        # Display menu
        print("\n--- Bank Account Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. Transfer Money")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":  # Deposit money
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "2":  # Withdraw money
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "3":  # View balance
            account.display_balance()

        elif choice == "4":  # Transfer money
            recipient_account_number = input("Enter recipient account number: ")
            recipient_account = BankAccount(recipient_account_number, "Recipient", 0)  # Dummy recipient account
            amount = float(input("Enter transfer amount: "))
            account.transfer(amount, recipient_account)

        elif choice == "5":  # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
