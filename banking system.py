class Bank:
    def __init__(self):
        self.accounts = {}


    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            if initial_balance >= 0:
                self.accounts[account_number] = initial_balance
                print(f"Account {account_number} created with an initial balance of ${initial_balance:.2f}")
            else:
                print("Initial balance cannot be negative.")
        else:
            print("Account already exists.")
 

    def get_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found.")
            return None 

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            if amount > 0:
                self.accounts[account_number] += amount
                print(f"Deposited ${amount:.2f} into account {account_number}.")
            else:
                print("Deposit amount must be positive.")
        else:
            print("Account not found.") 

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount > 0:
                if self.accounts[account_number] >= amount:
                    self.accounts[account_number] -= amount
                    print(f"Withdrew ${amount:.2f} from account {account_number}.")
                else:
                    print("Insufficient funds.")
            else:
                print("Withdrawal amount must be positive.")
        else:
            print("Account not found.")


bank = Bank()

bank.create_account("23454625", 1000)
bank.create_account("45235467")

print("Balance of account 23454625:", bank.get_balance("23454625"))
print("Balance of account 45235467:", bank.get_balance("45235467"))

 

bank.deposit("12345", 500)
bank.withdraw("12345", 200)
bank.withdraw("67890", 100)

 

print("Final balance of account 12345:", bank.get_balance("12345"))