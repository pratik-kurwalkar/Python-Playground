# import re
#
# test = input('> ')
# rawString = r'\tTab'
# pattern1 = re.compile(r'abc')
# print(pattern1.finditer(test))

# def password(string):
#     regex=re.compile([a-z])
#     if len(string) >= 8 and re.search([a-z], string) != None
#         return True
#     else:
#         return False
#
# print(password("abcd1234"))

# myList = [[45, 12],[55,21],[19, -2],[104, 20]]
# somelist = []
# for i, j in myList:
#     somelist.append('Senior') if i >= 55 and j > 7 else somelist.append('Open')
# print(somelist)

copy = [5,2,1,4,1,7,1,9]
print(copy)
numbers = copy[:]
print('=====')
# copy = numbers
# if copy == []:
#     print(copy)
# mini = min(numbers)
# if (numbers.count(mini) > 0):
#     copy.remove(mini)
# print(copy)

print(numbers) if numbers == [] else numbers.remove(min(numbers)), print(numbers) if numbers.count(min(numbers)) > 0 else print(numbers)
print('=====')
print(copy)



