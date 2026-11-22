###
# Bank account
#
class BankAccount:
    def __init__(self, number):
        self.number = number
        self.balance = 0

    def deposit(self, amount):
        self.balance = round(self.balance + amount, 2)

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds on the account')
        else:
            self.balance = round(self.balance - amount, 2)

    def show_info(self):
        balance_text = f'{self.balance:.2f}'.replace('.', ',')
        print(f'Bank Account No: {self.number}')
        print(f'Balance: PLN {balance_text}')

account = BankAccount('12 3456 5555 9090 1111 0000 7722')
account.show_info()
account.deposit(25.30)
account.show_info()
account.withdraw(31.70)
account.show_info()
account.withdraw(14)
account.show_info()
