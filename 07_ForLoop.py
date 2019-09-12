# For loops & nested loops

# for each loop
# for item in 'String':
#     print(item)
# for item in ['item1', 'item2']:#[] is used to denote a list
#     print(item)
# for item in range(10):#Takes no. 0 to specified no.
#     print(item)
# for item in range(10,15):
#     print(item)
# for item in range(10,50,10):
#     print(item)

prices = [42, 70, 420]  # List of items
total = 0
for i in prices:
    total += i
print(f'Total cost: {total}')

numbers = [5, 2, 5, 2, 2]
for i in numbers:
    output = ''
    for x in range(i):
        output += 'x'
    print(output)


