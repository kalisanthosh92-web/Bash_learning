def newcustomer():
    menu_and_price = [
    ['Spaghetti',40],
    ['Palabok',35],
    ['Buko Juice',20],
    ['Pandesal w/ Palaman',15],
    ['Bottled water',15]
    ]

    print('-'*47)
    print(f'|{'#':^8}|{'Item':<25}|  {'Price':^8}|')
    print('-'*47)
    for i in range(len(menu_and_price)):
        print(f'|{i+1:^8}|{menu_and_price[i][0]:<25}| ₱{menu_and_price[i][1]:^8}|')
        print('-'*47)
    
    print()
    cashier_name = input('Enter the cashier name:').title()
    customer_name = input('Enter the customer name:').title()
    i = 1 
    subtotal = 0
    
    order = []
    qty = []
    while i<= 3:
        item = int(input('Enter item number(1 - 5):'))        
        if item == 0 :
            pass
        elif item in range(1,6):
            quantity = int(input('Enter quantity:'))
            order.insert(i+1,item)
            qty.insert(i+1,quantity)
            subtotal += menu_and_price[item - 1 ][1] *quantity
        else:
            print('Order taken as Null!')
            
        i += 1


    if subtotal >= 100 :
        discount= subtotal * 0.1
    else :
        discount = 0
    total = subtotal-discount


    amount = int(input('Amount the customer is paying:'))
    
    if amount < subtotal:
        print('The amount is not enough.')
        amount = int(input('Amount the customer is paying:'))
    if amount >= subtotal:
        print('\n\n')
        print(f'{'---FOOD STORE---':^34}')
        print('Cashier Name:',cashier_name)
        print('Customer Name:',customer_name,end = '\n')
        for i in range(len(order)):
            print(f'Order {i+1} : {menu_and_price[order[i] - 1][0]},qty {qty[i]}')
        print(f'\nSubtotal: ₱{subtotal:.2f}')
        print(f'Discount: ₱{discount:.2f}')
        print(f'Total: ₱{total:.2f}')
        print(f'Paid amount: ₱{amount:.2f}')
        print(f'Change: ₱{amount - total:.2f}\n\n')
        


while True:
    customer = input('Do you have a new customer?(Y/N): ').lower()
    if customer == 'y':
        newcustomer()
    else :
        break

