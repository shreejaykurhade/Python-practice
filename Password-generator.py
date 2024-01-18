import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("Enter number of letters you would like ?\n"))
nr_numbers = int(input("Enter number of numbers you would like ?\n"))
nr_symbols = int(input("Enter number of symbols you would like ?\n"))

nr = nr_letters + nr_numbers + nr_symbols
password_list=[]
password=""

for i1 in range(1,nr_letters+1,1):
    password_list.append(random.choice(letters))

for i2 in range(1,nr_numbers+1,1):
    password_list.append(random.choice(numbers))

for i3 in range(1,nr_symbols+1,1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password="".join(password_list)

print("\nYour password is " + password)

    
