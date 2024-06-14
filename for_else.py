tuple1 = (1,2,3,4,5,6,7,8,9,10)
for i in tuple1:
    #print(i)
    if i%2 == 0:
        print(i)
        break
else:
    #print("loop successfully completed and we are in else block now!!!")
     print("there in no numner divisible by 2 in this sequence")