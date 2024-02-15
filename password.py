import re

def is_strong_password(password):
    # Define the regular expression pattern
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$')

    # Check if the password matches the pattern
    if pattern.match(password):
        return True
    else:
        return False

# Test the function with different passwords
passwords = [
    "Abcdefg1",   # Strong password
    "password",   # Weak password (no uppercase, no digit, short)
    "PAS12@SwORD", # Strong password 
    "12345678",   # Weak password (no uppercase, no lowercase)
    "AbCdEfGh",   # Weak password (no digit, short)
    "abcdefgh"    # Weak password (no uppercase, no digit, short)
]

for password in passwords:
    if is_strong_password(password):
        print(f"{password}: Strong password")
    else:
        print(f"{password}: Weak password")

