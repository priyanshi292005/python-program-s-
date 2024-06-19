
#count=1
#while count<=10:
#    print(count)
#    count+=1
#    if count==5:
#        break
#    print("hello")
#print("out from loop ")


list1= ["hi","hello","welcom"]
names=["priya","monika","priyanshi"]
for item in list1:
    for name in names:
        print(item,name)
        if item == "hello" and name =="monika":
            break
    print("out from inner loop")
print("out from outer loop")
