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
print('-'*47)

cashier_name = input('Enter the cashier name:')
customer_name = input('Enter the customer name:')
i = 1 
subtotal = 0

while i<= 3:
    item = int(input('Enter item number(1 - 5):'))
    
    #order.append([item,quantity])
    #i += 1

    if item == 0 :
        pass
    elif item in range(1,6):
        quantity = int(input('Enter quantity:'))
        subtotal = menu_and_price[item - 1 ][1] *quantity
    else:
        print('Enter valid item number.')
    
    i += 1


if subtotal >= 100 :
    subtotal = round(subtotal,2) - round(subtotal/10,2)


amount = int(input('Amount the customer is paying:'))
if amount < subtotal:
    print('The amount is not enough.')
else:
    print('Amount paid is enough.')
    print(f'change the customer gets = ₱{amount - subtotal}')


