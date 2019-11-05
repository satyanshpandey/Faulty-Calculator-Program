d1={'+':'addition','-':'subtraction','*':'multiplication','/':'division'}
print('This is faulty calculator if you enter a=44 and b=55 then your answer is absolutley wrong...!')
print(d1.keys())
print('enter operator ')
op=input()
print(d1[op])
a=int(input('enter first number:'))
b=int(input('enter seceond number:'))
if op=='+':
    if a==44 and b==55:
        print('your addition is :',1000)
    else:
        print('your ddition is:',a+b)
elif op=='-':
    if a==44 and b==55:
        print('subtraction is',5000)
    else:
        print(a-b)
elif op=='*':
    if a==44 and b==55:
        print('multiplication is',4444)
    else:
        print('multiplication is ',a*b)
elif op=='/':
    if a==44 and b==55:
        print('division is ',4455)
    else:
        print(a/b)
else:
    print('Enter valid value...!!!')
input()
