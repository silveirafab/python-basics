# Flow control in python
# 1. Display menu
# 2. Prompt user to insert money
# 3. Allow user to select an item
# 4. CHeck if the user has enough funds to purchase the selected item
# 5 'Dispense' the item. Success message and subtract funds from user
# 6. Offer the user the opportunity to make additional purchasel or exit

# Welcome and menu display
candy = 1.50
soda = 2.00
chips = 1.00
print('='*31)
print(f'Welcome to the vending machine!')
print('='*31)
print(f'Here is the menu:'.center(30))
print('-'*31)
print(f'Candy: ${candy:.2f}'.center(15))
print(f'Soda:  ${soda:.2f}'.center(15))
print(f'Chips: ${chips:.2f}'.center(15))
print('-'*31)

# Ask user for money
user_funds = float(input('Please insert money: '))
print('-'*31)
print(f'You have ${user_funds:.2f} available')
print(' '*31)
print('Please type the option you would like below')

# Loop to select an item and check funds after
inventory = ['Chips', 'Candy', 'Soda']
remaining_funds = user_funds

while True:
    itempre = input('What option would you like: ')
    item = itempre.capitalize() 
    if item not in inventory:
        print('ERROR this item does not exist. Select from menu')
        print('='*31)
        print(f'Here is the menu:'.center(30))
        print('-'*31)
        print(f'Candy: ${candy:.2f}'.center(15))
        print(f'Soda:  ${soda:.2f}'.center(15))
        print(f'Chips: ${chips:.2f}'.center(15))
        print('-'*31)
        continue

    elif item == 'Chips':
        if remaining_funds >= chips:
            remaining_funds = remaining_funds - chips
            print(' '*31)
            print(f'Enjoy your {item}, you have ${remaining_funds:.2f} left')
        else:
            print('!'*31)
            print(f'Not enough funds for {item}, you have ${remaining_funds:.2f}.\nThis item cost ${chips:.2f}')
            print(' '*31)
            add_more = input('Would you like to insert more money? Y/N: ')
            if add_more.lower() in ('y' or 'yes'):
                more_money = float(input('How much more would you like to add: '))
                remaining_funds = remaining_funds + more_money
                print(f'Your new balance is {remaining_funds:.2f}')

    elif item == 'Candy':
        if remaining_funds >= candy:
            remaining_funds = remaining_funds - candy
            print(' '*31)
            print(f'Enjoy your {item}, you have ${remaining_funds:.2f} left')
        else:
            print('!'*31)
            print(f'Not enough funds for {item}, you have ${remaining_funds:.2f}.\nThis item cost ${candy:.2f}')
            print(' '*31)
            add_more = input('Would you like to insert more money? Y/N: ')
            if add_more.lower() in ('y' or 'yes'):
                more_money = float(input('How much more would you like to add: '))
                remaining_funds = remaining_funds + more_money
                print(f'Your new balance is {remaining_funds:.2f}')

    elif item == 'Soda':
        if remaining_funds >= soda:
            remaining_funds = remaining_funds - soda
            print(' '*31)
            print(f'Enjoy your {item}, you have ${remaining_funds:.2f} left')
        else:
            print('!'*31)
            print(f'Not enough funds for {item}, you have ${remaining_funds:.2f}.\nThis item cost ${soda:.2f}')
            print(' '*31)
            add_more = input('Would you like to insert more money? Y/N: ')
            if add_more.lower() in ('y' or 'yes'):
                more_money = float(input('How much more would you like to add: '))
                remaining_funds = remaining_funds + more_money
                print(f'Your new balance is {remaining_funds:.2f}')

    go_again = input('Would you like to buy another item? Y/N: ')
    print('='*31)
    print(f'Here is the menu:'.center(30))
    print('-'*31)
    print(f'Candy: ${candy:.2f}'.center(15))
    print(f'Soda:  ${soda:.2f}'.center(15))
    print(f'Chips: ${chips:.2f}'.center(15))
    print('-'*31)
    if go_again.lower() in ('n', 'no'):
        print(' '*31)
        print(f'Transaction ended. \nYou will be refunded ${remaining_funds:.2f}')
        print('='*31)
        print('Thank you for using the vending machine!')
        break
    else:
        continue
