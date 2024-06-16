import random

latters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
symbols=['!','@','$','#','%','^','&','*','(',')','~']
print("welcome to password generator!")
n_letters=int(input("How many letters would you want you like in your password?\n"))
n_symbols=int(input("How many symbols would you want you like in your password?\n"))
n_numbers=int(input("How many numbers would you want you like in your password?\n"))
password=""
for i in range(1,n_letters+1):
    char=random.choice(latters)
    password=password+char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password=password+char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password=password+char
print(password)