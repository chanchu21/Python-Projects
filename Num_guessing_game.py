# Using Random module

import random
num=random.randrange(1,101)
user_input=int(input("Enter any number"))
if(user_input<num):
    print("Computer num is:",num)
    print("your number is smaller than computer number")
elif(user_input>num):
    print("Computer num is:", num)
    print("Your num is greater than computer num")
else:
    print("Computer num is:", num)
    print("Congrats! you guess the exact num")