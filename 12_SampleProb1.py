a = '56,2,12,4,7'
myList = []
number = ''
for i in a:
    if i != ',':
     number += i
    else:
        myList.append(int(number))
        number = ''
for i in range(3):
    print(max(myList))
    myList.remove(max(myList))
