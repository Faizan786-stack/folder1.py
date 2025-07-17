# import random

# num = random.randrange(1000, 10000)
# n = int(input("Enter your 4 digits number: "))

# if n == num:
#     print("Greate! you choice the number in 1 try. you'ar awesome")
# else:
#     count = 1

#     while n != num:
#         correct_count = 0
#         num_str = str(num)
#         n_str = str(num)

#         for i in range(4):
#             n_str[i] == num_str[i]
#             correct_count += 1
        

#         if correct_count > 0:
#             print(f"Not quite the number. But you did get {correct_count} digit(s) correct!\n")
#         else:
#             print("None of the numbers in your input match.\n")
#         guess = int(input("Enter your next choice of numbers: "))
#         count += 1

#     print("You've become a Mastermind!")
#     print(f"It took you only {count} tries.")

import random

# Generate a random 4-digit number
num = random.randrange(1, 99)

# Prompt user for initial guess
guess = int(input("Guess the 2 digit number: "))

# If the guess is correct on the first try
if guess == num:
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    attempts = 1  # First guess already taken

    while guess != num:
        correct_count = 0
        num_str = str(num)
        guess_str = str(guess)

        # Compare each digit and count correct ones
        for i in range(2):
            if guess_str[i] == num_str[i]:
                correct_count += 1

        # Give feedback based on correctness
        if correct_count > 0:
            print(f"Not quite the number. But you did get {correct_count} digit(s) correct!\n")
        else:
            print("None of the numbers in your input match.\n")

        # Take the next guess
        guess = int(input("Enter your next choice of numbers: "))
        attempts += 1

    # If the number is guessed correctly
    print("You've become a Mastermind!")
    print(f"It took you only {attempts} tries.")

