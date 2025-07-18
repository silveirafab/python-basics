def red_light():
    print(f'Stop! The light is Red.')

def yellow_light():
    print(f'Caution! The light is Yellow.')

def green_light():
    print(f'Go! The light is Green.')

def traffic_light():
    state = input('What is the color of the light? ')
    state = state.capitalize()
    return state

def main():
    function_state = traffic_light()
    if function_state == 'Red':
        red_light()
    elif function_state == 'Yellow':
        yellow_light()
    elif function_state == 'Green':
        green_light()
    else:
        print('That is not a real color! Pick again? or Stop? ')
        drive = input('Choice: ')
        drive = drive.capitalize()
        if drive == 'Stop':
            return 'stop'

while True:
    response = main()
    if response == 'stop':
        break

#while True:
#    main()
#    if main() == main('stop')
#    break


