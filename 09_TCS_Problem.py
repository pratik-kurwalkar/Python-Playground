#tcs problem solution

var = input()
even = 0
odd = 0
for i in range(len(var)):
    test = int(var[i])
    if (test % 2) == 0:
        even += test
    else:
        odd += test
if even > odd:
    print(even - odd)
else:
    print(odd - even)