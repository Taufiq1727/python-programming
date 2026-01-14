class Animal :
    location = "Australia"
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("generic animal sound")

class dog(Animal):
    def speak(self):
        super().speak()#this prints the speak function called by parent class
        print("woof!")

d = dog("bruno")
d.speak()
print(d.location)