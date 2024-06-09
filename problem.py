size=input("what size pizza you want (S/M/L): ")
bill=0
if size == "S" or size=='S':
    bill+=100
    print("small pizza price is 100 Rs.")
elif size == "M" or size=='M':
    bill+=200
    print(" medium pizza price is 200 Rs.")
else:
    bill+=300
    print(" large pizza price is 300 Rs.")

add_pepperoni =input("do you want pepperoni(y/n)?")
if add_pepperoni=="y" or add_pepperoni=="Y":
    if size == "S" or size=='S':
        bill+=30
    else:
        bill+=50

extra_cheese=input("do you want extra cheese(y/n)?")
if extra_cheese=="y" or extra_cheese=="Y":
    bill+=20
    print(f"your total bill is {bill}")