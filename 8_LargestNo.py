# Program to find largest no. in list

number_list = []
num = int(input('Enter the number of inputs: '))
for i in range(num):
    number_list.append(input('> '))
print(f'Entered no. are: {number_list}')
largest = 0
for i in number_list:
    if int(i) > largest:
        largest = int(i)
print(f'The largest no. is: {largest}')
