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
print(f'Welcome to the vending machine!')
print(f'Here is the menu:')
print(f'Candy: ${candy:.2f}')
print(f'Soda: ${soda:.2f}')
print(f'Chips: ${chips:.2f}')

# Ask user for money
user_funds = float(input('Please insert money: '))
print(f'You have ${user_funds:.2f} available')
print('Please type the option you would like below')

# Loop to select an item and check funds after
inventory = ['Chips', 'Candy', 'Soda']
remaining_funds = user_funds

while True:
    itempre = input('What option would you like: ')
    item = itempre.capitalize() 
    if item not in inventory:
        print('ERROR this item does not exist. Select from menu')
        print(f'Candy: ${candy:.2f}')
        print(f'Soda: ${soda:.2f}')
        print(f'Chips: ${chips:.2f}')
        continue

    elif item == 'Chips':
        if remaining_funds >= chips:
            remaining_funds = remaining_funds - chips
            print(f'Enjoy your {item}, you have ${remaining_funds:.2f} left')
        else:
            print(f'Not enough funds for {item}, you have ${remaining_funds:.2f}.\n This item cost ${chips:.2f}')
            add_more = input('Would you like to insert more money? Y/N: ')
            if add_more.lower() in ('y' or 'yes'):
                more_money = float(input('How much more would you like to add: '))
                remaining_funds = remaining_funds + more_money
                print(f'Your new balance is {remaining_funds:.2f}')

    elif item == 'Candy':
        if remaining_funds >= candy:
            remaining_funds = remaining_funds - candy
            print(f'Enjoy your {item}, you have ${remaining_funds:.2f} left')
        else:
            print(f'Not enough funds for {item}, you have ${remaining_funds:.2f}.\n This item cost ${candy:.2f}')
            add_more = input('Would you like to insert more money? Y/N: ')
            if add_more.lower() in ('y' or 'yes'):
                more_money = float(input('How much more would you like to add: '))
                remaining_funds = remaining_funds + more_money
                print(f'Your new balance is {remaining_funds:.2f}')

    elif item == 'Soda':
        if remaining_funds >= soda:
            remaining_funds = remaining_funds - soda
            print(f'Enjoy your {item}, you have ${remaining_funds:.2f} left')
        else:
            print(f'Not enough funds for {item}, you have ${remaining_funds:.2f}.\n This item cost ${soda:.2f}')
            add_more = input('Would you like to insert more money? Y/N: ')
            if add_more.lower() in ('y' or 'yes'):
                more_money = float(input('How much more would you like to add: '))
                remaining_funds = remaining_funds + more_money
                print(f'Your new balance is {remaining_funds:.2f}')

    go_again = input('Would you like to buy another item? Y/N: ')
    print(f'Here is the menu:')
    print(f'Candy: ${candy:.2f}')
    print(f'Soda: ${soda:.2f}')
    print(f'Chips: ${chips:.2f}')
    if go_again.lower() in ('n', 'no'):
        print(f'Transaction ended. You will be refunded ${remaining_funds:.2f}')
        print('Thank you for using the vending machine!')
        break
    else:
        continue