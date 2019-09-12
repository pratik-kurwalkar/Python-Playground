#  Exceptions
try:
    age = int(input('Age: '))
    print(age)
    print(f'Current year div. by age: {2019 / age}')
    #  Exit code 0 means program executed successfully and 1 means program crashed
except ValueError:
    print('Only enter int!')
except ZeroDivisionError:
    print("Don't enter age as 0!")
except Exception:
    print("Other Exception!")