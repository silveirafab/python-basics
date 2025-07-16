# create an empty list

todo_list = []
print('Your todo list;', todo_list)

# append items to the list
todo_list.append('buy groceries')
todo_list.append('finish homework')
todo_list.append('call mom')

print('updated list;', todo_list)

# insert an item
todo_list.insert(0, 'pay bills')
print('After inserting an item;', todo_list)

# using indexes and slicing
print('first task;', todo_list[0])
print('second task;', todo_list[1])
print('last two tasks;', todo_list[-2:]) 
# colon means start from end work towards begining. so -2 from end.

# mark a task as done
done_task = todo_list.pop(2)
print('you completed;', done_task)
print('todo list after removal;', todo_list)

# update an existing task
print(todo_list[1])
todo_list[1] = 'read a book'
print(todo_list)
todo_list[1] = 'buy groceries and snacks'
print('updated to do lists:', todo_list)

# print a task list
print('Here\'s what you still need to do:')
for task in todo_list:
    print('- ', task)