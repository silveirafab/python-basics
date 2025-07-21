# Summative Assesment Python Mini Project
# 1. Start/Welcome - greet user 
# 2. Create function that identifies and returns letter grade
# 3. Create function that prints student summary: name, score, and letter grade
# 4. Create a function that saves this information to a text file.
# 5. Use loop to keep asking for more student info
# 6. When user is done, offer a way to end program. 


def welcome():
    print('Welcome to the Student Grade Tracker!')
    print('My name is Cortana, I will be helping you today.')
    user_name = input('Please introduce yourself, what is your name? ')
    print(f'Excellent, nice to meet you {user_name}')
    print('To begin, please have the student names and their scores (0-100) ready.')
    print('Once you have this information please press enter and we will begin.')
    ready = input('Press ENTER when you are ready to start')
    return user_name 


def get_letter_grade(grade):
        if grade >= 90:
            return 'A'
        elif grade in range(80, 90):
            return 'B'
        elif grade in range(70,80):
            return 'C'
        elif grade in range(60, 70):
            return 'D'
        else:
            return 'F'

student_list = []
def add_student_name_score():
    name = input('Enter student name: ').title()
    score_input = input('Enter score (0-100): ')
    score = int(score_input)
    grade = get_letter_grade(score)
    student_list.append((name, score, grade))
    print(f'Added: {name} with score {score} -> {grade}')

def print_summary(student_list):
     print('\nStudent Summary:')
     for student in student_list:
          print(f'{student[0]}: {student[1]} -> {student[2]}')

def save_to_file(student_list):
     with open('grades.txt', 'w') as f:
          for student in student_list:
               f.write(f'{student[0]}: {student[1]} -> {student[2]}\n')
     print('Student data saved to grades.txt')

def main():
     welcome()
     while True:
          add_student_name_score()
          another = input('Add another student? (yes/no): ').lower()
          if another == 'no':
               break
     print_summary(student_list)
     save_to_file(student_list)
     
main()
