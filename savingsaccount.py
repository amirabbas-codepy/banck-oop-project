
from accountbank import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, interest_rate=0.025):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate
    
    def applay_interest_proccess(self):
        if self.balance > 0:
            data = self.balance * self.interest_rate
            return f' your profit per month : {data}'
        else:
            return False, 'balance = 0'