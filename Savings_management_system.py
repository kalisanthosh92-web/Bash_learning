import random as rd
import os

def dec_line():
    print('=' * 50)
    print('SAVINGS MANAGEMENT SYSTEM'.center(50))
    print('=' * 50)


options = ['Create Account', 'Check Balance', 'Deposit Funds', 'Withdraw Funds', 'View Transaction History', 'Exit']


def listing():
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}") 
        print()


def header():
    dec_line()
    listing()

def file_check(in_name):
    try:
        with open(in_name + '.txt', 'r') as file:
            file.close()
            return True
    except :
        
        return False
         

def clear_screen():
    """
    Clears the terminal screen.
    This keeps the menu looking neat and readable instead of piling text 
    on top of older text every time the user makes a choice.
    """
    os.system("cls" if os.name == "nt" else "clear")




def create_acc(name):
    rand_num = rd.choices(range(1,100),k = 4)
    num = ''.join(str(i) for i in rand_num) 
    unique_num = int(num)
    uniqueAccount_num = = name + '_' + str(unique_num)
    file_name = name +  '_' + str(unique_num) + '.txt'
    with open(file_name, 'w') as file:
        print('account created')
        file.close()





while True:
    header()
    choice = input('Enter your choice (1-5): ')
    if choice.isdigit() :
        choice = int(choice)
        if choice > 0 and choice <= len(options):
            if choice == 1:
                fname = input('Enter your first name: ')
                lname = input('Enter your last name: ')
                name = fname + '_' + lname
                if file_check(name) == False :
                    create_acc(name)
                    print(f'your acc num is {unique_acc} ')


            elif choice == 2:
                print('selected to view balance.')
                exiting_option = input('Enter "N" to go back to main menu.')
                
                if  exiting_option != 'N' :
                    clear_screen()
                    input_name = input('Enter your unique givenname: ')
                    
                    if file_check(input_name) == True:
                        file = open(input_name + '.txt', 'r')
                        file_content = file.read().splitlines()
                        if len(file_content) == 0:
                            print('Checking Balance...')
                            print('Your balance is 0')
                        else:
                            print('Checking Balance...')
                            for line in file_content:
                                if line.startswith('Balance :'):
                                    balance = line.split(':')[1].strip()
                                    print(f'Your balance is {balance}')
                        file.close()
                    
                    else: 
                        print('Invalid name. ')
                else: 
                    clear_screen()         
                    

            elif choice == 3:
                print('selected to deposit funds.')
                exiting_option = input('Enter "N" to go back to main menu, or press any key to continue.  ').upper()
                
                if  exiting_option != 'N' :
                    clear_screen()
                    input_name = input('Enter your unique givenname: ')
                    file_check(input_name)
                    if file_check(input_name) == True:
                        file = open(input_name + '.txt', 'r+')
                        file_content = file.read().splitlines()
                        while True:
                            dep_amount = input('Enter amount to deposit: ')
                            if  dep_amount.isdigit() and 0 < int(dep_amount) :
                                
                                update = f'deposited ${dep_amount}.'
                                file_content.append(update) 
                                for line in file_content:
                                    if line.startswith('Balance :'):
                                        balance = line.split(':')[1].strip()
                                        balance += dep_amount
                                        balance_str = line.pop()
                                file_content.append(balance_str)
                                file.write(file_content)
                                file.flush()
                                file.close()
                                break
                    else:
                        print('invalid file name.')
                elif exiting_option == 'N':        
                    print('Exiting. ')
                else:
                    print('Invalid input. ')

            