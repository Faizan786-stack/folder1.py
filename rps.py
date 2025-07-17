import random
choices = ('r','p','s')
while True:
    user_choice = input(r"guess your choice (r\p\s): ")

    if user_choice not in choices:
        print("Invalid syntex!")

    comp_choice = random.choice(choices)
    print(f"you chose {user_choice}")
    print(f"computer chose {comp_choice}")

    if (
    (user_choice == 'r' and comp_choice == 's') or
    (user_choice == 'p' and comp_choice == 'r') or
    (user_choice == 's' and comp_choice == 'p')):
        print("You Win!")

    elif user_choice != comp_choice:
        print("You Loss!")


    elif user_choice == comp_choice:
        print("Match Tie!")
        continue
    
    user_continue = input("If you want to play again (y/n): ")
    if user_continue == 'n':  
        break