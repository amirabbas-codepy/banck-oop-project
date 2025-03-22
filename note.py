    bankaccount = None
    while True:
        
        menu = input('select menu : (1.bank account 2.go to the bank 3.checking the interest rate of the account 4.withdraw 5.deposit) : ')

        if menu not in ('1', '2', '3', '4'):
            print('menu not in (1, 2, 3, 4)')
            sleep(3)
            system('cls')
            continue
        else:
            match menu:
                case '1':
                    account_number = input('account_number : ')
                    holder_name = input('holder_name : ')
                    balance = input('balance : ')

                    if not account_number.isdecimal():
                        print('account number not a number')
                        sleep(3)
                        system('cls')
                        continue
                    if not holder_name:
                        print('holder name is empty')
                        sleep(3)
                        system('cls')
                        continue
                    if not balance.isdecimal():
                        print('balance not a number')
                        sleep(3)
                        system('cls')
                        continue
                    else:
                        balance = int(balance)
                    
                    bankaccount = BankAccount(account_number, holder_name, balance)
                    print('create bank account successfully')

                case '2':
                    if not bankaccount:
                        print('first create the bank account')
                        continue
                    savingsaccount = SavingsAccount(account_number, 
                                                    holder_name, 
                                                    balance, 
                                                        2.5)

                    interest = savingsaccount.applay_interest_proccess()
                    print(interest)
                    sleep(4)
                    system('cls')
                    
                case '3':
                    pass

                case '4':
                    break