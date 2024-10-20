
Menu = {
    'Pizza' : 79,
    'Special Chay' :  20,
    'Coffee' :  20 ,
    'Pasta': 49,
    'Burger' : 59 ,
    'Salad' : 79,
    'Cold-Drink 200ml' : 25 ,
    
    
}

print('Welcome to PROGRAMMING Cafe' )
print('Special Chay : Rs.20\nCoffee : Rs.20\nPizza : Rs.79\nPasta : Rs.49\nBurger : Rs59\nSalad : Rs.79\nCold-Drink 200ml : Rs.25')

order_total = 0 

item_1 = input('Enter the name of Item you want to order :')

if item_1 in Menu :
    
    order_total += Menu[item_1]
    print(f'your order {item_1} has been added ')
    
else:
    print(f'Ordered item {item_1} is not availble yet.')
    
another_order = input(print('Do you want to order anything else from menu ? (Yes/No)'))

if another_order == 'Yes':
    item_2 = input('Enter your oreder = ')
    if item_2 in Menu:
        order_total += Menu[item_2]
        print('Your Ordered Item has been added ')
        
    else:
        print('Your ordered item {item_2} is not availble yet !')
        
        
print(f'The total amount you have to pay for your order is : {order_total}')
        

    
    
    