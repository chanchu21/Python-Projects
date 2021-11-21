print("BOLLYWOOD GAME")
Movie_name = "shershaah"
guess_count = 0  # keeps track of how many times user have guessed the word
guess_limit = 3  # how many times user can guess the word = total 3 trials-0,1,2
out_of_guesses = False # whether or not the user is out of guesses, if its true that means user has no more guess chance
print("""s_e___aa_""")
guess = ""
while guess != Movie_name and not(out_of_guesses):
    if guess_count < guess_limit:  # do they have guess left? if they do then it will ask the input.
        guess = input("Guess Movie name"+ " :- ")
        guess_count += 1
    else:
        out_of_guesses = True  # guess limit reached
if out_of_guesses:
    print("Out of guesses, you LOST the GAME!")
else:
    print("You WIN the GAME!")

