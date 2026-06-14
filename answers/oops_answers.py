# ============================================================
#       PYTHON OOP - ANSWERS
#    Topics: Classes, Objects, Inheritance, Polymorphism,
#            Encapsulation, Abstraction, Magic Methods
#                  (Easy → Medium → Hard)
# ============================================================

import math
from abc import ABC, abstractmethod
from math import gcd
import json
import time


# ─────────────────────────────────────────────
#  LEVEL 1 : EASY
# ─────────────────────────────────────────────

# Q1. Dog class
class Dog:
    def __init__(self, name, breed):
        self.name  = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

d1 = Dog("Bruno", "Labrador")
d2 = Dog("Max", "Beagle")
d1.bark()   # Bruno says: Woof!
d2.bark()   # Max says: Woof!


# Q2. Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r = Rectangle(5, 3)
print(r.area())       # 15
print(r.perimeter())  # 16


# Q3. Student class
class Student:
    def __init__(self, name, age, grade):
        self.name  = name
        self.age   = age
        self.grade = grade

    def display(self):
        print(f"Name: {self.name} | Age: {self.age} | Grade: {self.grade}")

s1 = Student("Arjit",  20, "A")
s2 = Student("Rahul",  21, "B")
s3 = Student("Priya",  19, "A+")
s1.display()
s2.display()
s3.display()


# Q4. Counter class
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count

c = Counter()
c.increment()
c.increment()
c.increment()
c.decrement()
print(c.get_count())  # 2
c.reset()
print(c.get_count())  # 0


# Q5. Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

ci = Circle(7)
print(round(ci.area(), 2))           # 153.94
print(round(ci.circumference(), 2))  # 43.98


# Q6. BankAccount class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner   = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}. Balance: ₹{self.balance}")

    def get_balance(self):
        return self.balance

acc = BankAccount("Arjit", 1000)
acc.deposit(500)       # Balance: 1500
acc.withdraw(200)      # Balance: 1300
acc.withdraw(2000)     # Error: Insufficient balance!


# Q7. Temperature class
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

t = Temperature(100)
print(t.to_fahrenheit())  # 212.0
print(t.to_kelvin())      # 373.15


# Q8. Person with class method from_birth_year
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    @classmethod
    def from_birth_year(cls, name, year):
        age = 2025 - year
        return cls(name, age)

    def display(self):
        print(f"{self.name}, Age: {self.age}")

p1 = Person("Arjit", 20)
p2 = Person.from_birth_year("Rahul", 2000)
p1.display()   # Arjit, Age: 20
p2.display()   # Rahul, Age: 25


# Q9. MathUtils with static methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

print(MathUtils.add(5, 3))       # 8
print(MathUtils.divide(10, 2))   # 5.0
print(MathUtils.divide(5, 0))    # Error: Division by zero


# Q10. Laptop class
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def is_affordable(self):
        return self.price < 50000

l1 = Laptop("HP", "Pavilion", 45000)
l2 = Laptop("Apple", "MacBook Pro", 150000)
print(l1.is_affordable())   # True
print(l2.is_affordable())   # False


# ─────────────────────────────────────────────
#  LEVEL 2 : MEDIUM
# ─────────────────────────────────────────────

# Q11. Inheritance + Polymorphism
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some generic sound")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

class DogAnimal(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")

animals = [Cat("Whiskers"), DogAnimal("Bruno"), Cat("Luna")]
for animal in animals:
    animal.speak()


# Q12. Shape hierarchy with area()
class Shape:
    def area(self):
        return 0

class Triangle(Shape):
    def __init__(self, base, height):
        self.base   = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class RectangleShape(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def area(self):
        return self.length * self.width

class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

def print_areas(shapes):
    for shape in shapes:
        print(f"{shape.__class__.__name__}: Area = {round(shape.area(), 2)}")

shapes = [Triangle(5, 4), RectangleShape(6, 3), CircleShape(7)]
print_areas(shapes)


# Q13. Vehicle and Car with super()
class Vehicle:
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def description(self):
        base = super().description()
        return f"{base} ({self.num_doors} doors)"

v = Vehicle("Toyota", "Innova", 2022)
c = Car("Honda", "City", 2023, 4)
print(v.description())   # 2022 Toyota Innova
print(c.description())   # 2023 Honda City (4 doors)


# Q14. Employee and Manager
class Employee:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def annual_salary(self):
        return (self.salary * 12) + self.bonus

emp = Employee("Rahul", 30000)
mgr = Manager("Arjit", 50000, 100000)
print(emp.annual_salary())   # 360000
print(mgr.annual_salary())   # 700000


# Q15. Encapsulation with private attributes
class PersonPrivate:
    def __init__(self, name, age):
        self.__name = name
        self.__age  = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.__age = age

p = PersonPrivate("Arjit", 20)
print(p.get_name())   # Arjit
p.set_age(21)
print(p.get_age())    # 21
# p.set_age(-5)       # raises ValueError


# Q16. Student with private marks
class StudentMarks:
    def __init__(self):
        self.__marks = []

    def add_mark(self, mark):
        self.__marks.append(mark)

    def get_average(self):
        return sum(self.__marks) / len(self.__marks)

    def get_highest(self):
        return max(self.__marks)

    def get_lowest(self):
        return min(self.__marks)

sm = StudentMarks()
for mark in [85, 92, 78, 95, 88]:
    sm.add_mark(mark)
print(sm.get_average())   # 87.6
print(sm.get_highest())   # 95
print(sm.get_lowest())    # 78


# Q17. Book with magic methods
class Book:
    def __init__(self, title, author, pages):
        self.title  = title
        self.author = author
        self.pages  = pages

    def __str__(self):
        return f"{self.title} by {self.author} ({self.pages} pages)"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        return self.pages

b = Book("Python Crash Course", "Eric Matthes", 544)
print(str(b))    # Python Crash Course by Eric Matthes (544 pages)
print(repr(b))   # Book('Python Crash Course', 'Eric Matthes', 544)
print(len(b))    # 544


# Q18. Vector with operator overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)   # Vector(4, 6)
print(v2 - v1)   # Vector(2, 2)


# Q19. Fraction with __add__ and __eq__
class Fraction:
    def __init__(self, numerator, denominator):
        common = gcd(abs(numerator), abs(denominator))
        self.numerator   = numerator   // common
        self.denominator = denominator // common

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
print(f1 + f2)           # 5/6
print(Fraction(2, 4) == Fraction(1, 2))   # True


# Q20. ShoppingCart with magic methods
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def __len__(self):
        return len(self.items)

    def __str__(self):
        lines = [f"  {item['name']:20s} ₹{item['price']}" for item in self.items]
        return "Shopping Cart:\n" + "\n".join(lines)

    def total(self):
        return sum(item["price"] for item in self.items)

cart = ShoppingCart()
cart.add_item("Laptop",  75000)
cart.add_item("Mouse",   1500)
cart.add_item("Keyboard", 2500)
print(cart)
print(f"Items : {len(cart)}")
print(f"Total : ₹{cart.total()}")


# ─────────────────────────────────────────────
#  LEVEL 3 : HARD
# ─────────────────────────────────────────────

# Q21. Abstract class Payment
class Payment(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CreditCard(Payment):
    def process(self, amount):
        print(f"Paid ₹{amount} via Credit Card")

class UPI(Payment):
    def process(self, amount):
        print(f"Paid ₹{amount} via UPI")

class NetBanking(Payment):
    def process(self, amount):
        print(f"Paid ₹{amount} via Net Banking")

payments = [CreditCard(), UPI(), NetBanking()]
for p in payments:
    p.process(1000)


# Q22. Abstract Notification
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def __init__(self, to, subject):
        self.to      = to
        self.subject = subject

    def send(self):
        print(f"Email sent to {self.to} | Subject: {self.subject}")

class SMSNotification(Notification):
    def __init__(self, phone, message):
        self.phone   = phone
        self.message = message

    def send(self):
        print(f"SMS sent to {self.phone} | Message: {self.message}")

notifications = [
    EmailNotification("arjit@gmail.com", "Welcome!"),
    SMSNotification("+91-9999999999", "Your OTP is 4321")
]
for n in notifications:
    n.send()


# Q23. Multiple Inheritance — Duck
class Flyable:
    def fly(self):
        print("I can fly!")

class Swimmable:
    def swim(self):
        print("I can swim!")

class Duck(Flyable, Swimmable):
    def quack(self):
        print("Quack Quack!")

duck = Duck()
duck.fly()    # I can fly!
duck.swim()   # I can swim!
duck.quack()  # Quack Quack!


# Q24. MRO — Diamond Problem
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass

d = D()
d.greet()            # Hello from B  (MRO: D → B → C → A)
print(D.__mro__)     # (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)


# Q25. Circle using @property
class CircleProperty:
    def __init__(self, radius):
        self.radius = radius   # calls setter

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = value

    @property
    def area(self):
        return math.pi * self.__radius ** 2

    @property
    def circumference(self):
        return 2 * math.pi * self.__radius

cp = CircleProperty(5)
print(round(cp.area, 2))           # 78.54
print(round(cp.circumference, 2))  # 31.42
# cp.radius = -1                   # raises ValueError


# Q26. Employee with @property salary
class EmployeeProperty:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary   # calls setter

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = value

    @property
    def annual(self):
        return self.__salary * 12

    @staticmethod
    def department():
        return "Engineering"

emp = EmployeeProperty("Arjit", 50000)
print(emp.salary)              # 50000
print(emp.annual)              # 600000
print(EmployeeProperty.department())   # Engineering


# Q27. Singleton Pattern
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.value = 42

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)    # True — same instance
print(id(s1) == id(s2))   # True


# Q28. Matrix class
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __mul__(self, other):
        result = [[0] * other.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def transpose(self):
        result = [
            [self.data[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ]
        return Matrix(result)

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
print("Addition:")
print(m1 + m2)
print("Multiplication:")
print(m1 * m2)
print("Transpose:")
print(m1.transpose())


# Q29. Custom iterator — yields only even numbers
class NumberRange:
    def __init__(self, start, stop):
        self.current = start
        self.stop    = stop

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < self.stop:
            value = self.current
            self.current += 1
            if value % 2 == 0:
                return value
        raise StopIteration

print(list(NumberRange(1, 10)))   # [2, 4, 6, 8]


# Q30. Observer Pattern — EventSystem
class EventSystem:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event, listener):
        if event not in self.listeners:
            self.listeners[event] = []
        self.listeners[event].append(listener)

    def unsubscribe(self, event, listener):
        if event in self.listeners:
            self.listeners[event].remove(listener)

    def emit(self, event, data=None):
        for listener in self.listeners.get(event, []):
            listener(data)

# Demo
def on_login(data):
    print(f"[LOG]   User logged in: {data}")

def on_login_email(data):
    print(f"[EMAIL] Welcome email sent to: {data}")

def on_purchase(data):
    print(f"[LOG]   Purchase made: ₹{data}")

es = EventSystem()
es.subscribe("login",    on_login)
es.subscribe("login",    on_login_email)
es.subscribe("purchase", on_purchase)

es.emit("login",    "arjit@gmail.com")
es.emit("purchase", 4999)
es.unsubscribe("login", on_login_email)
es.emit("login",    "rahul@gmail.com")   # only LOG fires now


# ─────────────────────────────────────────────
#  BONUS CHALLENGES
# ─────────────────────────────────────────────

# B1. @timer decorator for class methods
def timer(func):
    def wrapper(*args, **kwargs):
        start  = time.time()
        result = func(*args, **kwargs)
        end    = time.time()
        print(f"{func.__name__} took {round(end - start, 6)}s")
        return result
    return wrapper

class DataProcessor:
    @timer
    def process(self, n):
        total = sum(range(n))
        return total

dp = DataProcessor()
dp.process(1000000)


# B2. Stack with __len__, __iter__, __contains__
class IterableStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(reversed(self.items))   # top to bottom

    def __contains__(self, item):
        return item in self.items

st = IterableStack()
for i in [1, 2, 3, 4, 5]:
    st.push(i)

print(len(st))          # 5
print(3 in st)          # True
print(9 in st)          # False
for item in st:
    print(item, end=" ")  # 5 4 3 2 1
print()


# B3. Metaclass that uppercases all method names
class UpperCaseMeta(type):
    def __new__(mcs, name, bases, namespace):
        upper_namespace = {}
        for key, value in namespace.items():
            if not key.startswith("__") and callable(value):
                upper_namespace[key.upper()] = value
            else:
                upper_namespace[key] = value
        return super().__new__(mcs, name, bases, upper_namespace)

class MyClass(metaclass=UpperCaseMeta):
    def hello(self):
        return "Hello!"

    def greet(self):
        return "Hi there!"

obj = MyClass()
print(obj.HELLO())   # Hello!
print(obj.GREET())   # Hi there!


# B4. JSONSerializable class
class JSONSerializable:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

    def __str__(self):
        return str(self.__dict__)

obj = JSONSerializable(name="Arjit", age=20, city="Delhi")
json_str = obj.to_json()
print(json_str)                            # {"name": "Arjit", "age": 20, "city": "Delhi"}
restored = JSONSerializable.from_json(json_str)
print(restored)                            # {'name': 'Arjit', 'age': 20, 'city': 'Delhi'}


# B5. Method Chaining
class Chain:
    def __init__(self):
        self.name = None
        self.age  = None
        self.city = None

    def set_name(self, name):
        self.name = name
        return self        # return self for chaining

    def set_age(self, age):
        self.age = age
        return self

    def set_city(self, city):
        self.city = city
        return self

    def display(self):
        print(f"Name: {self.name} | Age: {self.age} | City: {self.city}")
        return self

Chain().set_name("Arjit").set_age(20).set_city("Delhi").display()
# Name: Arjit | Age: 20 | City: Delhi
