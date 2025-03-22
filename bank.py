
from typing import Literal
from accountbank import BankAccount

class Bank:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Bank, cls).__new__(cls, *args, **kwargs)
            return cls._instance
        else:
            raise ValueError('Back sample is already made')
        
    def __init__(self):
        self.account_list = []
    
    def create_account(self, account_bank:BankAccount, type_account:Literal['regular account', 'Deposit account']='regular account'):
        for account in self.account_list:
            
            if account.account_number == account_bank.account_number:
                return False, 'Invalid BankAccount'
        
        account_bank.type_account = type_account
        self.account_list.append(account_bank)
        return True
    
    def remove_account(self, account_bank:BankAccount):
        for account in self.account_list:
            if account.account_number == account_bank.account_number:
                self.account_list.remove(account_bank)
                return True
        return False
    
    def money_transfer(self, account_bank_sender:BankAccount, account_number_reciver:str, amount:int, save_in_txt:Literal[True, False]=False):
        reciver = None
        for acc in self.account_list:
            if acc.account_number == account_number_reciver:
                reciver = acc
                break
        
        if reciver:
            if account_bank_sender.balance >= amount:
                account_bank_sender.balance -= amount
                reciver.balance += amount
                
                if save_in_txt:
                    
                    data = {'account_sender_name':account_bank_sender.holder_name, 
                            'account_sender_number':account_bank_sender.account_number, 
                            'amount':amount, 
                            'account_reciver_name':reciver.holder_name, 
                            'account_reciver_number':reciver.account_number
                            }
                            
                    
                    with open('Transactions.txt', 'a') as file:
                        file.write(f'{data}\n')

                        return True, 'Save in Transactions.txt'
                    
            else:
                return False, 'not balance'
        else:
            return False, 'none'

    def find_account(self, account_number:str):
        for acc in self.account_list:
            if acc.account_number == account_number:
                return f'{acc.account_number}, {acc.holder_name}, {acc.balance}, {acc.type_account}'
        
        return False, 'not fund'
