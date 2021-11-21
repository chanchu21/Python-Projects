# CALCULATOR with if-elif

print('''
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVISION
''')
a=eval(input("Enter 1st number"))
b=eval(input("Enter 2nd number"))
c=input("Select operation to perform(+,-,*,/)")
if c=="+":
    print("Result is:-", a+b)
elif c=="-":
    print("Result is:-", a-b)
elif c=="*":
    print("Result is:-", a*b)
elif c=="/":
    print("Result is:-", a/b)
else:
    print("operator is invalid")