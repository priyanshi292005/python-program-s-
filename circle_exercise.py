class circle:
    pi = 3.14  # class object attribute
    def __init__(self,radius):
        self.radius = radius
    def get_circumference(self):
        return 2 * self.pi * self.radius
circle_1=circle(4)
print(f"The circumfrance of circle is{circle_1.get_circumference()}")
