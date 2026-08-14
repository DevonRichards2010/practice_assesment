''''
Name: Devon Richards
Date: 10/08/26
Version: 1
Descroption: Heads Vs Tails
'''
#----------------------------------------------------------Libaries------------------------------------------------------------
import random
#---------------------------------------------------------Functions------------------------------------------------------------
def heads_and_tails(): # this does the heads vs tails code
    user_score=0
    computer_score=0
    options=["Heads","Tails"] # your selection of options for what you can pick
    while user_score!=2 and computer_score!=2:
        choice=random.randint(0,1)
        computer_guess=options[choice]
        user_guess=str(input("Type in Heads or Tails: ")) # where you get to input your choice
        if user_guess == computer_guess:
            print(f'the side that landed was {computer_guess} and you guessed {user_guess} you win one point')
            user_score +=1
        else:
            print(f'the side that landed was {computer_guess}, and you guesses {user_guess}, you do not gain a point')
            computer_score +=1
        if user_score==2: # winning / loosing conditions
            print(f'congratulations {first_name}, you win the game! CONGRATULATIONS')
        else:
            print(f'hahaha you lost')
#---------------------------------------------------------main_routine-------------------------------------------------------------
print("(heads or tails)") # where it displays the question to the user
first_name=str(input("what is your name: "))
age=int(input("what is your age: "))
heads_and_tails() # calls function