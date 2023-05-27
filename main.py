import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Asking the user how he or she wants the password
letters_in_pass = int(input("How many letters do you want in your password: "))
numbers_in_pass = int(input("How many numbers do you want in your password: "))
symbols_in_pass = int(input("How many symbols do you want in your password: "))

list_of_password = []

# Looping through letters to randomly select the users choice

for _ in range(1, letters_in_pass + 1):
    selected_letters = random.choice(letters)
    list_of_password.append(selected_letters)

# Looping through numbers to randomly select the users choice

for _ in range(1, numbers_in_pass + 1):
    selected_numbers = random.choice(numbers)
    list_of_password.append(selected_numbers)

# Looping through symbols to randomly select the users choice

for _ in range(1, symbols_in_pass + 1):
    selected_symbols = random.choice(symbols)
    list_of_password.append(selected_symbols)

# Shuffling the generated password
shuffled_password = random.sample(list_of_password, len(list_of_password))
print(shuffled_password)

# Converting the generated password from list to string

password = ""
for char in shuffled_password:
    password += char

print(f"Your password is: {password}")


