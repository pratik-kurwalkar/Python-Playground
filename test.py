list_qwe = ['kalpesh', 'Pratik']
print(list_qwe)
list_qwe.append('zxc')
list_qwe[0] = 'asd'
print(list_qwe)
list2 = ('qwe', 'fgh')
if 'qwe' in list2:
    print("Exists in tuple!")

# tocheck = input()
# if tocheck in list_qwe:
#     print('Exists in list!')
# else:
#     print('Does not exist in list!')
a = [i for i in range(0, 200, 5)]


def testMethod():
    print('I am in the test file!')


ip = 'WUBAWUBWUBWUBBWUBWUBWUBC'
a = ip.replace('WUB', 'WUB,')
t = a.split(',')
print(t)
while (t.count('WUB') != 0):
    t.remove('WUB')
print(t)
# for i, j in enumerate(t):
#     t.remove(j)
final = ''
for i in t:
    final += i
final = final.replace('WUB',' ').strip()
print(final)
# print(ip.replace('WUB', ' ').split())
# print("0".join(['a','b']))
#
# print(" ".join(ip.replace('WUB', ' ').split()))

# if a[0] == '0':
#     a = a[1:]
# if a[len(a)-1] == '0':
#     a = a[:len(a)-1]
#
# # a.strip()
# '''
# for i in range(1,len(a)-2):
#     if a[i] == ' ':
#         if  a[i+1] == ' ':
#             a = a[:i]+a[i+1:]
# print(a)'''
#
# k=a.find('0')
# l=k+1
# while(a[l]=='0'):
#     l+=1
# else:
#     a = a[:l]+a[l+1:]
# print(a)


# index along with value
# for i,j in enumerate(a):
#     print(i,j)

for i in range(10):
    print(i, end='')
