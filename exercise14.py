heights=input("enter all the height separatrd by a space =")
heights_list=heights.split()
count=0
for height in heights_list:
    count=count+1
print(count)
for i in range(count):
    heights_list[i]=int(heights_list[i])

total=0
for person in heights_list:
    total += person
avg = total/count
print("Average height is:",round(avg))
