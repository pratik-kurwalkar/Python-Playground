# While Loop

lines = int(input('Enter no. of lines: '))
i = 1
while i <= lines:
    print("*"*i),   # use , to print without newline
    i += 1
    
enteredNo = 0
count = 0
while count < 3:
    if enteredNo != 9:
        enteredNo = int(input('Guess the number? '))
    else:    
        print('Wow you win!')
        break
    count += 1
else:#else block executed if while loop executed without any interruptions.
    print('You Lost!')
