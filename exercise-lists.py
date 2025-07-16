# play with for loops

# create a list
device_list = []
device_list.append('PC1')
device_list.append('PC2')
device_list.append('PC3')
device_list.append('Laptop1')
device_list.append('switch1')
device_list.insert(5, 'router2')
print(device_list)

# while true loop forces user to stay in loop until router1 is input
while True:
    print('This device name is incorrect, please name the device correctly:', device_list[5])
    correct_device = input('Please enter correct device name: ')
    if correct_device == 'router1':
        device_list[-1] = correct_device 
        break
    else:
        print('That is also incorrect, try again')
print(device_list)

# use a for loop to iterate through the list
print('Here are the devices connected:')
count = 1
for items in device_list:
    print(f'#{count}. {items}')
    count += 1

# add or remove devices, 1 - add, 2 - remove, 3 - quit
print('Would you like to add or remove any other devices?')
new_device = input('Enter "1" for yes. Enter "2" to remove. Enter "3" to quit: ')
if new_device == '1':
    add_device = input('Please enter device name: ')
    device_list.append(add_device)
    print(device_list)
    print('Have a nice day')
#elif: new_device == '2':
#    remove_item = device_list(input('Select from index')2)
else:
    print('Have a nice day')
#else:
#    print('Invalid choice, enter 1, 2, or 3')
