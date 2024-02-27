# Practial No. 15
# Title Program Simple Inheritance

class Animal:  
    def speak(self):  
        print("This Is Animal Class")  

class Dog(Animal):  
    def bark(self):  
        print("This Is Dog Class")  
d = Dog()  
d.bark()  
d.speak()  