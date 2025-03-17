

class BankAccount:
    def __init__(self, account_number:str, holder_name:str, balance:int):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount:int):
        if isinstance(amount, int):
            self.balance += amount
            return True
        
        return False, 'type error' 

    def withdraw(self, amount:int):
        if isinstance(amount, int):
            if self.balance >= amount:
                self.balance -= amount
                return True
            else:
                return False, 'amount > balance'
            
        return False, 'type error' 
