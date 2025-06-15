class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number=account_number # 
        self.balance=0 # 
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount 
            return f"Deposited: ${amount:.2f}"
        return false
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance  -= amount
            return f"Withdrew: ${amount:.2f}"
        return f"Insufficient funds"
    def display_balance(self):
        return f"Current balance ${self.balance:.2f}"
if __name__ == "__main__":