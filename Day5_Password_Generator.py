#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter = ''
symbol = ''
num = ''
for _ in range(0,nr_letters):
  rl = random.randint(0, len(letters)-1)
  letter += letters[rl]
		# Could also use: 
		letter += random.choice(letters)

for _ in range(0,nr_symbols):
  rs = random.randint(0, len(symbols)-1)
  symbol += symbols[rs]

for _ in range(0,nr_numbers):
  rn = random.randint(0, len(numbers)-1)
  num += numbers[rn]

password = letter+symbol+num
print(f"Your password is: {password}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_password = ''.join(random.sample(password, len(password)))
print(f"Your randomized password is: {random_password}")