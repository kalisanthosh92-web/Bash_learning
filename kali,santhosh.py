import os
def clear_screen():
    if os.name == "nt":    
        os.system("cls")
    else:                  
        os.system("clear")


def bill():
    while True:
        name_of_customer = input('Please enter your name: ')
        if name_of_customer.isalpha() :
            break 
        else :
            print('Please input a valid name. ')

    while True:
        try :
            number_of_meals = int(input('Enter number of meals ordered: '))
            break 
        except :
            print('Please input a valid input. ')

            

    while True:
        try :
            price_of_each_meal = float(input('Enter price of each meal: '))
            break 
        except :
            print('Please input a valid input. ')

    total_amount = number_of_meals * price_of_each_meal

    clear_screen()
    print()


    print('RECIEPT'.center(30,'*'))
    print('\n')
    print('Name of the Customer:'.ljust(25),name_of_customer)
    print('Number of meals ordered:'.ljust(25),number_of_meals)
    print('Price of each meal:'.ljust(25),price_of_each_meal)

    print('total amount:'.ljust(25),total_amount)


    if total_amount >= 500 :
        Discount = total_amount * 0.1
        print('Discount'.ljust(25),Discount)
        
        final_amount = total_amount - Discount
        print('Final Amount:'.ljust(25),final_amount)
    else :
        final_amount = total_amount

    print()

    if number_of_meals >= 5 and final_amount >=400 :
        print('Qualified for Free Drinks.')
    else :
        print('Not Qualified for Free Drinks.')

    print()
    print('Thank You for dinning here.')
    print('Please visit again.')

    print()
    print()



while True:
    new_customer = input('Do you have a new customer?(Y/N) ').upper()
    if new_customer == 'Y':
        clear_screen()
        bill()
    else :
        print('Thank you for using.' )
        break