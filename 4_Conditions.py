#Conditions & logical op.

price = 100000
good_credit = True
high_income = True
existing_loan = True

if good_credit:
    downpay = int(price)*(10/100)
else:
    downpay = int(price)*(20/100)    
print(f'Down Payment: {downpay}')
if (good_credit or high_income) and not existing_loan:
    print('Eligible for loan')
if good_credit and high_income:
    print('Eligible for exta benifits!')
if downpay <= 10000:
    print('Low Downpayment!')
else:
    print('High downpayment!')

weight = int(input('Enter Weight: ')) #Take input directly as an integer
unit = input('(l)lbs or (k)kg?: ')
if unit.upper() == 'L':
    print(f'Weight in kilos is: {weight*0.45}')
elif unit.upper() == 'K':
    print(f'Weight in pounds is: {weight/0.45}')
else:
    print('Enter correct unit!')        


    