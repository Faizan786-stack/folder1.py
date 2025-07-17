import random
import string

length = int(input("Enter a password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print(f"your password: {password}")