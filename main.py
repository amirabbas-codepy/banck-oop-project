
from accountbank import BankAccount
from bank import Bank
from savingsaccount import SavingsAccount

# This program is an object orinted banking system simulation 
# program where each class has different.

if __name__ == '__main__':
    bank = Bank()

    bankaccount1 = BankAccount('121212', 'John Doe', 0)
    bankaccount2 = BankAccount('121211', 'John Wick', 0)

    proccess1_deposit = bankaccount1.deposit(1000)
    proccess2_deposit = bankaccount2.deposit(2000)

    print('Deposit proccess')

    print(proccess1_deposit)
    print(proccess2_deposit)

    print('-' * 50)

    print('Withdraw proccess')

    proccess1_witdraw = bankaccount1.withdraw(2000)
    proccess2_witdraw = bankaccount2.withdraw(200)

    print(proccess1_witdraw)
    print(proccess2_witdraw)

    print('-' * 50)
    print('create account proccess')

    proccess_create1 = bank.create_account(bankaccount1, 'Deposit account')
    proccess_create2 = bank.create_account(bankaccount2, 'regular account')

    print(proccess_create1)
    print(proccess_create2)

    print('-' * 50)

    selected = input('test the remove account (yes, no) : ')
    
    if selected == 'yes':
        res = bank.remove_account(bankaccount1)
        print(f'removed {res}')
    
    finder = input('test find account in bank (yes, no) : ')

    if finder == 'yes':
        account_number = input('account number : ')
        res = bank.find_account(account_number)
        print(res) 

    send_money = input('test money transfer (yes, no) : ')

    if send_money == 'yes':
        account_number = input('account number reciver : ')
        res = bank.money_transfer(bankaccount1, '121211', 20)
        print(res)
        print('-' * 50)
        print(bankaccount1.balance)
        print(bankaccount2.balance)

    rate = input('test interest rate (yes, no) : ')

    if rate == 'yes':
        res = SavingsAccount(bankaccount1.account_number, 
                       bankaccount1.holder_name, 
                       bankaccount1.balance)
        
        print(res.applay_interest_proccess())

    save_in_txt_transaction = input('test save transactions in txt (yes, no) : ')

    if save_in_txt_transaction == 'yes':
        account_number = input('account number reciver : ')
        res = bank.money_transfer(bankaccount1, '121211', 20, save_in_txt=True)
        print(res)
        print('-' * 50)
        print(bankaccount1.balance)
        print(bankaccount2.balance)