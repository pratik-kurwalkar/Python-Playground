# Lists continued & Tuples
matrix = [
    [1, 2, 3],
    [3, 4, 5],  # 2D matrix
    [5, 6, 7]
]

number_list = [3, 34, 35, 34, 1, 57, 12]
list2 = number_list.copy()
number_list.remove(1)
number_list.sort()
print(number_list)
print(number_list.index(34))
print(1 in number_list)
number_list.reverse()
print(number_list)
print(number_list.count(31))
number_list.clear()
print('------------')

# Program to remove duplicates from list
my_list = [1, 1, 2, 4, 4, 4, 6, 8, 9]
print(my_list)
for i in my_list:
    if my_list.count(i) > 1:
        my_list.remove(i)
print(my_list)

# Tuples function in the same way as list but, value in it cannot be changed
my_list2 = (1, 2, 4)
print(my_list2)
