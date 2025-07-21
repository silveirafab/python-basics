# Summative Assesment Python Mini Project
# 1. Start/Welcome - greet user 
# 2. Create function that identifies and returns letter grade
# 3. Create function that gets name, and num score and adds to list with grade
# 4. Create a function that saves this information to a text file.
# 5. Create a function that prints this list
# 6. Use loop to keep asking for more student info
# 7. Create a function that adds this list to text file.
# 8. When user is done, offer a way to end program. 

from datetime import datetime
def welcome():
    '''the welcome function greets user, explains how to use program and what info user needs.
    Upon pressing enter, user will begin the program.'''

    print('Welcome to the Student Grade Tracker!')
    print('-' * 35)
    print('My name is Cortana. I will be helping you today.')
    user_name = input('Please introduce yourself, \nWhat is your name? ')
    print(' ' * 35)
    print(f'>>>Excellent! \nNice to meet you {user_name}.')
    print(' ' * 35)
    print('To begin, you will need student names and scores (0-100).')
    print('Once you have this information we will begin.')
    print('-' * 35)
    ready = input('Press ENTER when you are ready to start')
    print('-' * 35)


def get_letter_grade(num_score):
        '''This function determines what letter grade is given, depending on numerical score.
        grade is passed into this function, it returns a letter depending on the value
        of grade. '''

        if num_score >= 90:
            return 'A'
        elif num_score >= 80:
            return 'B'
        elif num_score >= 70:
            return 'C'
        elif num_score >= 60:
            return 'D'
        else:
            return 'F'

student_list = [] # This creates an empty list named student_list. We store the info here. 

def add_student_name_score():
    ''' This function will ask user for name, score, and uses the get_letter_grade function
    to determine grade. It adds to our empty list, turning it into a dictionary with these values.
    Lastly, a confirmation is printd.'''
    while True:
        name = input('Enter student name: ').strip().title()
        if name:
             break
        else:
             print('Name cannot be blank. Please Try again')
    while True:
        score_input = input('Enter score (0-100): ').strip()
        if score_input.replace('.', '', 1).isdigit(): # allow decimal point, be replacing it before input check
            score = round(float(score_input), 1)
            if 0 <= score <= 100:
                 break
            else:
                 print('Score invalid. Score must be between 0 and 100. Try again.')
        else:
             print('That\'s not a number. Score must be between 0-100. Try again')
    grade = get_letter_grade(score)
    student_list.append({'name': name, 'score': score, 'grade': grade})
    print(f'Added: {name:<20}{score:<8}{grade:<5}')



def print_summary(student_list):
     '''This function prints a summary with nice formatting lines of the students that
     were added. Name, score and grade are printed. It loops thorugh student_list and prints every
     entry. At the bottom it prints total students added.'''
     student_list.sort(key=lambda x: x['score'])#lambda defines the key and x: assigns it
     print('\nStudent Summary:')
     print('-' * 35)
     print(f'{"Name":<20}{"Score":<8}{"Grade":<5}')
     print('-' * 35)
     for student in student_list:
          print(f'{student['name']:<20}{student['score']:<8.1f}{student['grade']:<5}')
     print('-' * 35)
     print(f'Total students: {len(student_list)}')



def save_to_file(student_list):
     '''This function saves the data to a text file. It creats columns to organize it,
     and writes the data for name, score, and data'''
     with open('grades.txt', 'w') as f:
          f.write(f'Student Grade Report - Generated on: {datetime.now().strftime('%D %H:%M:%S')}\n')
          f.write('-' * 40 + '\n')
          f.write(f'{'Name':<20}{'Score':<8}{'Grade':<5}\n')
          f.write('-' * 40 + '\n')
          for student in student_list:
               f.write(f'{student['name']:<20}: {student['score']:<8.1f} -> {student['grade']:<5}\n')
          f.write('-' * 40 + '\n')
          f.write(f'Total Students: {len(student_list)}\n')
     print('Student data saved to grades.txt')



def main():
     '''This is the main function. This puts all other functions together to run the program.
     It calls the welcome function, and loops allowing the user to add as many entries as they want.
     When user is done, it prints the data and saves it to a text file.'''
     welcome()
     while True:
          add_student_name_score()
          another = input('>>> Add another student? (yes/no): ').lower()
          if another == 'no':
               break
     print_summary(student_list)
     save_to_file(student_list)
     print('\nThank you for using the Student Grade Tracker! Goodbye.')
     
main()
