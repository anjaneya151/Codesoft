# password_generator.py

import random
import string

def generate_password(length):
    if length < 4:
        return "Password should be at least 4 characters."

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

length = int(input("Enter desired password length: "))
print("Generated password:", generate_password(length))
