class Human:
    def eat(self):
        print("I can eat")

class Male(Human):
    def sleep(self):
        print("I can sleep whole day")
class Boy(Male):
    pass
boy_1=Boy()
boy_1.eat()
boy_1.eat()
boy_1.eat()
