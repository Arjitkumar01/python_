# # encapsulation
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"{self.year} {self.make} {self.model}")  
        

# # inheritance

# class animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass

# class Dog(animal):
    
#     def display(self):
#         return self.name
    
#     def speak(self):
#         return "Woof!"

# class Cat(animal):
#     def speak(self):
#         return "Meow!"
    
    

# d1 = Dog("max")
# print(d1.speak())
# print(d1.display())

# # polymorphism
# class Shape:
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

def checkOddEven(x):
    if x%2==0:
        print("Even")
    else:
        print("Odd")
    
x =int(input())  
checkOddEven(x)
    
