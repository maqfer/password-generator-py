import string
import random

def generate_password(length=12):
    # Define the character sets to use
    chars = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))

    return password

password = generate_password()
print(password)