# All about strings

print('''
This,
Is an example of multi-line string
Thank You! 
''')
Name = input('Enter Name: ')
print("1: " + Name[0])  # use of string index
print("2: " + Name[-1])  # use of negative index (reverse from last char.)
print("3: " + Name[0:3])  # return chars. from  0 to 2
print("4: " + Name[1:])  # provide starting index for string
print("5: " + Name[:3])  # provide ending index
Name2 = Name[:]  # copies the string value
Age = 20
print(f'My name is [{Name}] and my age is ({Age})')
# this is example of formatted string. to use insert f before string and use {} to insert var. dynamically
print('Length of string is: ' + str(len(Name)))  # len() can be used to calc. no of char.
print(Name.upper())  # functions can be accessed by dot operator
print(Name.find('Pratik'))  # finds pos. of char in string CASE SENSITIVE( -1 IF NOT FOUND)
print(Name.replace('Pratik', 'Qwerty'))  # replaces string sequence with new seq.
print('Pratik' in Name)  # check existance of string seq. in var. returns bool value
print(Name.title())  # capitalize first letter
