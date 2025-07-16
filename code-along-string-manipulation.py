string1 = 'This is a valid string'
string2 = "This is also a valid string"

palindrome = 'Go hand a salami, Im a lasagna hog'

#Use a qupte inside a string
string3 = "'Always look on the bright side of life' - Monty python"

# Use an escape charater to include quotes in strings
string4 = "\"Always look on the bright side of life\" - Monty Python"
print(string4)

print(len(string4))
# len() function outputs the amount of characters in the string
name = '     Fabrizzio     '
print(len(name))
print('Hello', name)
# The strip function removes spaces from strings
name_no_spaces = name.strip()
print(len(name_no_spaces))
print('Hello ', name_no_spaces)

# split() function
filepath = '/var/fabrizzio/here'
folders = filepath.split('/')
print(folders)
print(type(folders))
fullname = 'Fabrizzio,Silveira'
names = fullname.split(',')
print(names) # In split each string seperated by , holds a index number.
# In full name, Fabrizzio[0] and Silveira[1]
# This allows us to assign them to variables in a line of code.
firstName = names[0]
lastName = names[1]
print(f'First name: {firstName}')
print(f'Last name: {lastName}')
print(lastName, firstName)

# join() function
windowsPath = "\\".join(folders)
print(windowsPath)

# find()
reservation_name = 'Jon, Doe'
char_to_find = ','
# where is the comma?
char_location = reservation_name.find(char_to_find)
print(char_location)
# If there is no value to find, like you specified X, a negative number is returned.


# index()
char_location = reservation_name.index(char_to_find)
print(char_location)

# transformations
print(reservation_name.upper())#makes everything uppercase
print(reservation_name.lower())#makes everything lowercase
print(reservation_name.title())#Capitalizes first letter of words
print(reservation_name.swapcase())#makes lowercase upper and upper lower
print(reservation_name.capitalize())#capitalizes first character, thats all

# f-strings
name = 'Fabrizzio'
age = 30
print(f'my name is {name} and I am {age} years old')

a = 3
b = 9
print(f'{a*3}')
print(f'We can count to {b} by {a}: {a} {a*2} {a*3}')

# replacing
name = 'Fabrizzo Silveira'
name = name.replace('Fabrizzo', 'Fabrizzio')
print(name)

