class Student:     #(for public instance variable)
    def __init__(self, name):  #useing inside
        self.name = name
    def display(self):
        print(f"Hi my self {self.name} from student class")
s1 = Student("Monika")      #useing outside
print(s1.name)
s1.display()






class Student:     #(protected instance variablr)
    def __init__(self, name,rollno):
        self.name = name
        self.rollno = rollno
    def display(self):
        print(f"Hi my self {self.name} from student class")
class Branch(Student):
    pass
b1=Branch("priya",4)
print(b1.name)
print(b1.rollno)
#s1 = Student("Monika")

#print(s1.name)
#s1.display()