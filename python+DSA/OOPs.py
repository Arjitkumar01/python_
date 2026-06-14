# class student():
    
#     def stu(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks = marks
        
#     def display(self):
#         print("Student name :", self.name)
#         print("Student age :", self.age)
#         print("Student marks :", self.marks)
        
# s1 = student()
# s1.stu("arjit",20,90)
# s1.display()

# print("\n")

# s2 = student()
# s2.stu("priya",20,90)
# s2.display()

# print("\n")

# s3 = student()
# s3.stu("ishu",20,90)
# s3.display()

# print("\n")

# s4 = student()
# s4.stu("abhi",20,90)
# s4.display()

# print("\n")







# # ------------------------------------------------------------------------------------------------------------------------------------------------------



# class student:
    
#     def stu_name(self,name):
#         self.name = name
#     def stu_age(self,age):
#         self.age = age
#     def stu_marks(self,marks):
#         self.marks = marks

#     def display(self):
#         print("Student Name",self.name)
#         print("Student Age",self.age)
#         print("Student Marks",self.marks)
        
# s1 = student()
# s1.stu_name("arjit")
# s1.stu_age(20)
# s1.stu_marks(98)

# s1.display()
# # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





# Recap


class Student:
    
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print(f"name : {self.name}, Age : {self.age} , marks : {self.marks} ")

s1 = Student("arjit",20,10)
s1.display()

s2 = Student("abhi",20,10)
s2.display()

s3 = Student("priya",20,10)
s3.display()

s4 = Student("ishu",20,10)
s4.display()

s5 = Student("Priyarjit",20,10)
s5.display()

s6 = Student("abhishu",20,10)
s6.display()



# inheritance

from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog barks")
    
    def eat(self):
        pass
        
class Cat(Animal):
    def speak(self):
        print("Cat meows")    
        
    def eat(self):
        pass  
        
dog = Dog()
dog.speak()     
cat = Cat()   
cat.speak()






