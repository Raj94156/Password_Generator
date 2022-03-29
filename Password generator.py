import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
print('Do you want to have the "Easy" Or "Hard" password: Type "Hard" for Hard Password and "Easy" for Easy Password:')
choose = input("So,What you have decided").lower()
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
p=nr_letters
q=nr_symbols
r=nr_numbers
password = []
password_easy = ""
password_hard = ""

if choose== "easy":
    for  i in range(0,p):
        password_easy += random.choice(letters)
    for j in range(0,r):
        password_easy += random.choice(numbers)
   
    for k in range(0,q):
        password_easy += random.choice(symbols)
        
    print(password_easy)

if choose == "hard":
    for  i in range(0,p):
        password.append(random.choice(letters))
    for j in range(0,r):
        password.append(random.choice(numbers))
   
    for k in range(0,q):
        password.append(random.choice(symbols))
    
    random.shuffle(password)
    for char in password:
        password_hard+=char
    print(password_hard)
