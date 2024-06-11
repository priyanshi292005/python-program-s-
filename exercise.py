import random

#name = input("Enter everybody's name separated by comma: ")
#name_list = name.split(',')
#print(name_list)
#length = len(name_list)
#random_choice=random.randint(0, length-1)
#print(f"{name_list[random_choice]} will pay the bill")


name = input("Enter everybody's name separated by comma: ")
name_list = name.split(',')
reson_selection=random.choice(name_list)
print(f"{random.choice(name_list)} will pay the bill")