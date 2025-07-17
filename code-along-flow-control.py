'''
our_number = 42

is_guessed = False

# The while loop runs until a condition turns true
while is_guessed == False:

    # get input from the user
    guess = int(input('Enter your guess: '))

    # if statements - conditional statements to check the guess
    if guess == our_number:
        print('Hooray!')
        is_guessed = True
    elif guess > our_number:
        print('Too big!')
    else:
        print('Too low!')
'''
'''
# fizz buzz game
# continue goes back to beggining of the loop
# break exits the loop, skips the else in this scenario
counter = 1
while counter < 20:
    if counter %  3 == 0 and counter % 5 == 0:
        print(f'{counter}: Fizzbuzz')
    elif counter % 3 == 0:
        print(f'{counter}: Fizz')
    elif counter % 5 == 0:
        print(f'{counter}: Buzz')
    
    counter += 1  # counter = counter + 1
else:
    print('Done with while loop')
'''

# for loop example
loop_range = range(1, 11)
for i in loop_range:
    print(f'iteration {i}')

print(max(loop_range))

# for loop with a list
fruits = ['apple', 'bannana', 'cherry', 3, 4.5]

for iteration in fruits:
    print(f'Fruit: {iteration}')

favorite_movies = ['inception', 'The matrix', 'Interstellar']
for movie in favorite_movies:
    print(f'Movie: {movie}')

numbers = [1, 11, 23, 43, 23, 55, 1]
for value in numbers:
    if value > 10:
        print(f' The number {value} is greater then 10')

