# File I/O - Persistent data
import os
file_path = 'data.csv'
file_path2 = '/Volumes/SierraSSD/visaProjects/pythonBasics/python-basics/data/example2'

#print(file_path)

#file = open('data.csv', 'r')
#file = open(file_path, 'r') # open in read mode
#file = open(file_path, 'w') # open in write mode
#file = open(file_path, 'a') # open in append mode
#file = open(file_path, 'r+') # open in read/write mode


file = open('example.txt', 'w')
file.write('Hello World!\n')
file.write('This is line 2\n')
file.close

file2 = open(file_path2, 'w')
file2.write('Hello World!\n')
file2.write('This is line 2\n')
file2.close

# Open a file using 'with' keyword

'''with open('example-with.txt', 'w') as file:
          file.write('We wrote this file using the "with" keyword!\n')
          file.write('This is line two\n')
          file.write('This is line three \n')
'''
# read function to read the contents of a file

with open('example-with.txt', 'r') as file:
        contents = file.read()
        print(contents)

# Use for loop to read lines from a file

with open('example-with.txt', 'r') as file:
        for line in file:
                print(line.strip())

# Append to a file using 'with'
with open('example-with.txt', 'a') as file:
        file.write('This is an appended line!\n')

# delete a file

if os.path.exists('example2.txt'):
        os.remove('example2.txt')
        print('File delted')
else:
        print('The file does not exits')
                  