import random
l = ['Rock', 'Paper', 'Scissor']
'''
rock vs paper -> paper wins
paper vs scissor -> scissor wins
rock vs scissor -> rock wins
'''
keep_playing="true"
while keep_playing=="true":
   # computer choice by using random.choice()
   c_choice=random.choice(l)
   # user will enter his move
   u_choice=(input('''
   Enter your move:
   1. Rock
   2. Paper
   3. Scissor
   '''))
   print("computer chose:- ",c_choice)
   print("user chose:- ",u_choice)

   # now the logical part starts- write all possible outcomes
   if c_choice==u_choice:
      print("Tie")
   elif u_choice=="Rock" and c_choice=="Paper":
      print("Compuer wins")
   elif u_choice=="Rock" and c_choice=="Scissor":
      print("User wins")
   elif u_choice=="Paper" and c_choice=="Rock":
      print("Computer wins")
   elif u_choice=="Paper" and c_choice=="Scissor":
      print("Computer wins")
   elif u_choice=="Scissor" and c_choice=="Paper":
      print("User wins")
   elif u_choice=="Scissor" and c_choice=="Rock":
      print("Computer wins")
   else:
      print("invalid input")







