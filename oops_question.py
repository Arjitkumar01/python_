# question 1

class car:
    def drive(self):
        print("Car is moving")
car1=car()
car1.drive()

# question 2
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display(self):
        
        print(self.name)
        print(self.age)
        
first=Person("Arjit",20)
first.display()
        
        
# 2nd way
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        
first=Person("Arjit",20)
print(first.name,first.age)
        

# question 3

class Animal:
    def Sound(self):
        print("some sound!")

class Dog(Animal):
    def Sound(self):
        print("Bark!!")
        
d1=Dog()
d1.Sound()