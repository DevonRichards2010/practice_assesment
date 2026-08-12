''''
Name: Devon Richards
Date: 10/08/26
Version: 1
Descroption: Headsd Vs Tails
'''
#----------Libaries------------
import random
#---------Functions------------
def heads_and_tails():
    user_score=0
    computer_score=0
    options=["Heads","Tails"]
    while user_score!=2 and computer_score!=2:
        choice=random.randint(0,1)
        computer_guess=options[choice]
        user_guess=str(input("Type in Heads or Tails: "))
        if user_guess == computer_guess:
            print(f'the side that landed was {computer_guess} and you guessed {user_guess} you win one point')
            user_score +=1
        else:
            print(f'the side that landed was {computer_guess}, and you guesses {user_guess}, you do not gain a point')
            computer_score +=1
        if user_score==2:
            print(f'congratulations {first_name}, you win the game! CONGRATULATIONS')
        else:
            print(f'hahaha you lost')

#---------main_routine---------
print("(heads or tails)")
first_name=str(input("what is your name: "))
age=int(input("what is your age: "))
heads_and_tails() #calls function