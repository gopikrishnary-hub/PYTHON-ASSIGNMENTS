#password generator shuffled version
import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
    '}', '~' ]
print("Welcome to password generator!!!")
pass_letters = int(input("How many letters would you like to include in your password?\n"))
pass_symbols = int(input("How many symbols would you like to include in your password?\n"))
pass_numbers = int(input("How many numbers would you like to include in your password?\n"))
password = []
for i in range(pass_letters):
    password.append(random.choice(letters))

for i in range(pass_symbols):
    password.append(random.choice(symbols))

for i in range(pass_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
print(password)
#
password_shuffle = ""
for i in password:
    password_shuffle += i


print("Your password is:", password_shuffle)



