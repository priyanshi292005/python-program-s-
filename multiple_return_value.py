
#import statistics
#def mean_mediam_mode(list1):
#    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)

#print(mean_mediam_mode([4,9,85,7,0,92,3,18]))

#result=(mean_mediam_mode([4,9,85,7,0,92,3,18]))
#print(result)

#a,b,c=(mean_mediam_mode([4,9,85,7,0,92,3,18]))
#print(f"mean is {a}\nmedian is {b}\nmode is {c}")



def add(a,b):
    if a==0 & b==0:
        return
    else:
        return a+b

var1=int(input("enter the first variable"))
var2=int(input("enter the second variable"))
result=add(var1,var2)
print(result)
