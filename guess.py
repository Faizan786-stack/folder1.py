# comp ask import a number
# user give the no.
# the number is Big
# try lower
# you guess the right no.
import random
com_guees = random.randint(1,100)
while True:
    
    try:  
        uer_guess = int(input("Guess the Random Number: "))
        
        if uer_guess > com_guees:
            print("Try a lower Number!")
        elif uer_guess < com_guees:
            print("Try a Higher Number!")
        elif uer_guess == com_guees:
            print("Well done! You guess the right number")
            break
        
    except ValueError:
        print("Is not a valid Number")
