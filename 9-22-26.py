class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0):
        # Private attributes
        self.__account_number = account_number
        self.__holder_name = holder_name

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.__balance = initial_balance

    # Read-only account number
    @property
    def account_number(self):
        return self.__account_number

    # Holder name (getter + setter with validation)
    @property
    def holder_name(self):
        return self.__holder_name

    @holder_name.setter
    def holder_name(self, new_name):
        if not isinstance(new_name, str) or not new_name.strip():
            raise ValueError("Holder name must be a non-empty string")
        self.__holder_name = new_name

    # Balance (getter + setter with validation)
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = new_balance

    # Deposit method
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        print(f"Withdrawn {amount}. New balance: {self.__balance}")

    # Transfer method
    def transfer(self, target_account, amount):
        if not isinstance(target_account, BankAccount):
            raise ValueError("Target must be a BankAccount instance")
        try:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"Transferred {amount} to {target_account.account_number}")
        except ValueError as e:
            print(f"Transfer failed: {e}")


class Bank:
    def __init__(self):
        self.__accounts = []  # Private list

    # Add account (no duplicates)
    def add_account(self, account):
        if any(acc.account_number == account.account_number for acc in self.__accounts):
            raise ValueError("Account with this number already exists")
        self.__accounts.append(account)
        print(f"Account {account.account_number} added successfully")

    # Retrieve account by account number
    def get_account(self, account_number):
        for acc in self.__accounts:
            if acc.account_number == account_number:
                return acc
        return None

    # List all accounts (only number and name)
    def list_accounts(self):
        print("Accounts List:")
        for acc in self.__accounts:
            print(f"Account Number: {acc.account_number}, Holder Name: {acc.holder_name}")


# =========================
# Testing the Classes
# =========================
if __name__ == "__main__":
    bank = Bank()

    # Create accounts
    acc1 = BankAccount(101, "Yateesh", 5000)
    acc2 = BankAccount(102, "Rahul", 3000)

    # Add accounts to bank
    bank.add_account(acc1)
    bank.add_account(acc2)

    # List accounts
    bank.list_accounts()

    # Deposit
    acc1.deposit(2000)

    # Withdraw
    acc2.withdraw(1000)

    # Transfer
    acc1.transfer(acc2, 1500)

    # Change holder name
    acc1.holder_name = "Yateesh Chandra"

    # Final state
    bank.list_accounts()