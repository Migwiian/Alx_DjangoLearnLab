class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = float(balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: ${amount:.2f}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew: ${amount:.2f}"
        return "Insufficient funds."

    def display_balance(self):
        return f"Current Balance: ${self.balance:.2f}"

def main():
    account = BankAccount("TEST001", 100.00)

    print(account.display_balance())

    print(account.deposit(50.00))
    print(account.display_balance())

    print(account.withdraw(30.00))
    print(account.display_balance())

    print(account.withdraw(200.00))
    print(account.display_balance())

    print(account.deposit(-10.00))
    print(account.display_balance())

    print(account.withdraw(-5.00))
    print(account.display_balance())

    print(account.withdraw(account.balance))
    print(account.display_balance())

if __name__ == "__main__":
    main()