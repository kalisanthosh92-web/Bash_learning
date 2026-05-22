Groceries = [
['Rice', 52.00],
['Eggs',110.00],
['Milk',105.00],
['Bread',72.00],
['Chicken',195.00],
['Sardines',20.00],
['Noodles',12.00],
['Coffee',9.00],
['Onions',170.00],
['Cooking Oil',85.00]]

print('='*37)
print(f'|{'Assad Grocey Store':^35}|')
print('='*37)

for i in range(len(Groceries)):
    print(f'|{i+1:^3}|{Groceries[i][0]:^20}|{Groceries[i][1]:^10}|')
    print('-'*37)



cashier_name = input('Enter the cashier name:')
customer_name = input('Enter the customer name:')
i = 1 
subtotal = 0
order = []

while i!= 0 and i>0:
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
