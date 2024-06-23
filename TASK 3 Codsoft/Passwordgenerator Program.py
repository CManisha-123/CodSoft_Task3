import string
import random

length = int(input("Enter the desired length of the password: "))
valid_chars = string.ascii_letters + string.digits + string.punctuation
password = ''
for i in range(length):
    password += random.choice(valid_chars)
print("Password: "+password)