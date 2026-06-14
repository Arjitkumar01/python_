# Encapsulation

class Car:
    def __init__(self):
        self.__speed = 0   # Private variable

    def accelerate(self):
        self.__speed += 10

    def show_speed(self):
        print("Speed:", self.__speed)


car = Car()

car.accelerate()
car.accelerate()
car.show_speed()


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero"
        
calc = Calculator(10, 5)
print("Addition:", calc.add())
print("Subtraction:", calc.subtract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())


class student:
    def __init__(self, name, age, grade, admission_number):
        self.name = name
        self.age = age
        self.grade = grade
        self.admission_number = admission_number

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Admission Number: {self.admission_number}")
        
        
student1 = student("Arjit", 20, "A", "2025BTCS050")
student1.display_info()








from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Bark")


d = Dog()
d.sound()


class vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.speed = 0  # Private attribute

    def set_speed(self, speed):
        if speed >= 0:
            self.speed = speed
        else:
            print("Speed cannot be negative")

    def get_speed(self):
        return self.speed

car = vehicle("Toyota", "Corolla")
car.set_speed(60)
print("Car Speed:", car.get_speed())

# inheritance
class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Parent Name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        super().display()
        print(f"Child Age: {self.age}")

p = Parent("Alice")
p.display()

c = Child("Bob", 10)
c.display() 

# polymorphism
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(4, 5)
print("Area of Rectangle:", rect.area())    
circ = Circle(3)
print("Area of Circle:", circ.area())        