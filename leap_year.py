year=int(input("which year you wnant to check:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print(year," is Not leap year")
    else:
        print(year,"is a leap year")

else:
    print(year," is Not leap year")