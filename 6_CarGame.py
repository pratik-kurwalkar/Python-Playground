# Car Game

state = 'stopped'
while True:
    command = input('> ').lower()
    if command == 'help':
        print('''start - to start the car
stop - to stop the car
quit - to exit the game''')
    elif command == 'start':
        if state == 'started':
            print('Car already started!')
        else:
            print('Car Started!')
            state = 'started'
    elif command == 'stop':
        if state == 'stopped':
            print('Car already stopped!')
        else:
            print('Car Stopped!')
            state = 'stopped'
    elif command == 'quit':
        print('Quiting.......')
        break
    else:
        print("I don't understand the command..")
