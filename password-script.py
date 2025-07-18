# Random password generator
# 1. Welcome message
# 2. Ask user for for password length
# 3. Ask user what character types to include*****
# 4. Build pool of allowed characters
# 5. Generate password
# 6. Output password
# 7. Save password to a .txt 
import string
import random
def welcome_message():
    print(f'Hello, welcome to the random password generator!\n'
          f'Creating strong unique passwords is hard!\n'
          f'I can help with that.\n'
          f'Shall we begin?')
    begin = input('"Press ENTER to Begin"')

def pass_length():
    while True:
        print('How many characters should your password be?')
        length = input('Character length: ')
        if not length.isdigit():
            print('I said to choose a number!')
            continue
        length = int(length)
        if length < 12:
            print(f'That is not a strong password!\n'
              f'A strong password is 12 characters or more!\n'
              f'I recommend 16 for enhanced security.\n'
              f'Try again.')
        else:
            print(f'I like {length}, great job! That\'s a strong password.')
            return length

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

def allowed_pass_characters():
    pool = uppercase + digits + lowercase + symbols
    return pool


def generate_pass(length):
    password = ''
    pool = allowed_pass_characters()
    for i in range (length):
        char = random.choice(pool)
        password += char
    print(f'Starting...... \n'
    f'Password......\n'
    f'Generation.......'
    f'Done!\n'
    f'Your unique password is {password}')
    return password

def steal_password(password):
    with open('password-storage.txt', 'a') as file:
        file.write(f'{password}\n')

def main():
    welcome_message()
    length = pass_length()
    password = generate_pass(length)
    steal_password(password) 

main()

        




