# Q2.  Extend Q1 — add setter methods set_name() and set_age().
#      The setter for age should print an error if age < 0.
class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    
    def get_name(self):
        return self.__name
    def get_age(self):
        if self.__age <0:
            return "Error"
        else:
            return self.__age
    def set_name(self,new_name):
        self.__name=new_name
    def set_age(self,new_age):
        self.__age = new_age
        
    
    
p1 = Person("abhi",20)

print(p1.get_name())
print(p1.get_age())
p1.set_age(-2)
print(p1.get_age())
