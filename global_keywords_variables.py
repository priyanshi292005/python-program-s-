a=10
def display():
    a=15
    print(a)
display()


a=10
def display():
    print(a)
display()


a=10
def display():
    global a
    a=a+2
    print(a)
display()