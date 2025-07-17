candy = 1.50
soda = 2.00
chips = 1.00

inventory = {
    'Chips': chips,
    'Candy': candy,
    'Soda': soda
}

def attempt_purchase(item_name, item_price, remaining_funds):
    if remaining_funds >= item_price:
        remaining_funds -= item_price
        print(f'Enjoy your {item_name}, you have ${remaining_funds:.2f} left')
    else:
        print(f'Not enough funds for {item_name}, you only have ${remaining_funds:.2f}. This item costs ${item_price:.2f}')
        add_more = input('Would you like to insert more money? Y/N: ')
        if add_more.lower() in ('y', 'yes'):
            more_money = float(input('How much more would you like to add: '))
            remaining_funds += more_money
            print(f'Your new balance is ${remaining_funds:.2f}')
        
            if remaining_funds >= item_price:
                remaining_funds -= item_price
                print(f'Enjoy your {item_name}, you have ${remaining_funds:.2f} left')
        else:
            print(f'Transaction ended. You will be refunded ${remaining_funds:.2f}')
            print('Thank you for using the vending machine!')
            exit()  
    return remaining_funds

print('Welcome to the vending machine!')
print('Here is the menu:')
for name, price in inventory.items():
    print(f'{name}: ${price:.2f}')

user_funds = float(input('Please insert money: '))
remaining_funds = user_funds
print(f'You have ${remaining_funds:.2f} available')
print('Please type the option you would like below')

while True:
    itempre = input('What option would you like: ')
    item = itempre.capitalize()

    
    if item not in inventory:
        print('ERROR this item does not exist. Select from menu')
        for name, price in inventory.items():
            print(f'{name}: ${price:.2f}')
        continue

    
    remaining_funds = attempt_purchase(item, inventory[item], remaining_funds)

    
    go_again = input('Would you like to buy another item? Y/N: ')
    if go_again.lower() in ('n', 'no'):
        print(f'Transaction ended. You will be refunded ${remaining_funds:.2f}')
        print('Thank you for using the vending machine!')
        break