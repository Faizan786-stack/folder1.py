from datetime import datetime


user_birth_year = (input("Enter your birth (YYYY-MM-DD): "))

user_birth = datetime.strptime(user_birth_year, "%Y-%m-%d")

current_year = datetime.today()



age = current_year.year - user_birth.year

if(current_year.month, current_year.day) < (user_birth.month,user_birth.day):
    age -= 1

print(f"Your age is {age}")


