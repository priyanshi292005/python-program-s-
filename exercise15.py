
number = input("enter list of number=")
number_list = number.split()
count=0
for number in number_list:
    count+=1
print(f"the length of the list is : {count}")

for i in range(0,count):
    number_list[i] = int(number_list[i])
maximum = max(number_list)
for number in number_list:
    if number > maximum:
        maximum_number = number
print(f"the maximum number is : {maximum}")


