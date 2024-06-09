
Height=int(input("what is your height?"))

if Height>=3:
    print("can ride")
    age=int(input("w    hat is your age?"))
    if age<=12:
        bill=250
        print("ticket prize is 250$")
    elif age<=18:
        bill=450
        print("ticket prize is 450$")
    if age>20:
        bill=650
        print("ticket prize is 650$")

    want_photo = input(" Do you want to take photo(yes/ no  or YES/NO)?")
    if want_photo=="yes" or want_photo=="YES":
        bill=bill+50
        print(f"your total bill is {bill}")
    if want_photo=="no" or want_photo=="NO":
        bill=bill
        print(f"your total bill is {bill}")
else:
    print("can't ride")
    print('bye  bye tata')
