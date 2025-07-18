# Functions are reusable pieces of code

def greet(name1, name2):
    name1 = name1.lower()
    name2 = name2.upper()
    print(f'Hello, {name1}, and {name2}!')

def user_input(prompt):
    name = input('What\'s yout name? ')
    input_value = input(prompt)

def main_menu():
    print('Welcome to the menu')
    print('1. Start')
    print('2. Exit')

    choice = input('Please choose an option')
    print(f'you chose option {choice}')
    return choice

print('Hello!')
print('My name is python')
greet('BOB', 'jane')

return_menu_choice = main_menu()
if return_menu_choice == '1':
    print('starting the program...')
else:
    print('Exiting the program. Goodbye!')