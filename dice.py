# welcome to game
# dice the roll (y/n)
# invalid syntex
# print the number
import random
while True:
    user_guess = input("Roll the dice (y/n): ").lower()
    if user_guess == "y":
        guess_1 = random.randint(1,6)
        guess_2 = random.randint(1,6)
        print(f"{guess_1},{guess_2} you choose")
    elif user_guess == "n":
        print("Thank you!")
        break
    else:
        print("Invalid Syntex")
