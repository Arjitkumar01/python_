# Q1.  Create a class Person with private attributes __name and __age.
#      Add getter methods get_name() and get_age() to access them.
#      Create an object and print both values using getters.

class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    
p1 = Person("abhi",20)

print(p1.get_name())
print(p1.get_age())
