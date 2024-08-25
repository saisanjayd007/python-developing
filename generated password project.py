import random
import string

def generate_password():
    print("Password Generator by Sanjay")

    length = int(input("Enter the desired length of the password: 12"))

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    print(f"Generated Password: {password}")

generate_password()
