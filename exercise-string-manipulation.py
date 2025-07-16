# 1
to_be_changed = 'John Glenn|Neil Armstrong|Sally Ride|Douglas Wheelock|Mae Jamison'
changed_values = to_be_changed.split('|')
print(changed_values)

# 2
lyrics = """Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "no,
I'll tell you what you can do:"
"""
lyrics_split = lyrics.split('\n')
print(lyrics_split)

# 3
line = lyrics.splitlines()
print(line)

# 4
long_village_name = 'Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch'
string_length = long_village_name
print(len(string_length))

# 5
my_path = "              /c/Users /instructor/ Downloads/Submit Relating the Nonrelational Assessment Download May 10, 2021 917 AM.         " 
my_folder = my_path.strip() 
print(my_folder)

# 6
composers = 'Beethoven,Ludwig von;Liszt,Franz;Mozart,Wolfgang;Copland,Aaron'
composers_split = composers.split(';')
third_composer = composers_split[2]
comma_position = third_composer.find(',')
last_name, first_name = third_composer.split(',')
third_composer_name = f'{first_name} {last_name}'
print(third_composer_name)

# 7
left_padded = '         Operators are standing by'
right_padded = 'Call now   ' 
message = f'{right_padded.strip()}! {left_padded.strip()}'
print(message)

# 8
student_name = 'Owen'
grade = 94.75
assignment_number = 12
print(f'\'Student name: {student_name}, Assignment ID: {assignment_number}, Grade: {grade}%\'')

# 9
employee_id = "30"
employee_id_padded = employee_id.zfill(6)
print(employee_id_padded)

# 10
print(r'\n represents a new line.')

# 11
i_want_to_yell = 'yeah'
I_NEED_TO_BE_QUIET = 'SHHHHH"' 
this_is_a_title = 'this is a title'
sWAPcASE = 'sWAPcASE'
capitalize_this = 'capitalize this'
print(i_want_to_yell.upper())
print(I_NEED_TO_BE_QUIET.lower())
print(this_is_a_title.title())
print(sWAPcASE.swapcase())
print(capitalize_this.capitalize())
