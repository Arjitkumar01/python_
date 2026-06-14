# ============================================================
#       PYTHON OOP - PRACTICE QUESTIONS
#    Topics: Classes, Objects, Inheritance, Polymorphism,
#            Encapsulation, Abstraction, Magic Methods
#                  (Easy → Medium → Hard)
# ============================================================


# ─────────────────────────────────────────────
#  LEVEL 1 : EASY
# ─────────────────────────────────────────────

# --- CLASSES & OBJECTS ---

# Q1.  Create a class Dog with attributes name and breed.
#      Add a method bark() that prints "<name> says: Woof!"
#      Create two Dog objects and call bark() on both.


class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed = breed
        
    def bark(self):
        print(f"{self.name} says: Woof!")
    
    
d1=Dog("max","labra")
d2=Dog("pluto","german")

d1.bark()
d2.bark()



# Q2.  Create a class Rectangle with attributes length and width.
#      Add methods:
#      - area()      → returns length * width
#      - perimeter() → returns 2 * (length + width)


class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print( f"Area of rectangle : {self.length * self.width}")
    
    def perimeter(self):
        print(f"Perimeter of rectangle: {2*(self.length + self.width)}")
    

r1 = rectangle(5, 2)
r1.area()
r1.perimeter()
   
# Q3.  Create a class Student with attributes name, age, and grade.
#      Add a method display() that prints all three attributes.
#      Create 3 student objects and call display() on each.

class student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
        
    def display(self):
        print(f"Student Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Grade : {self.grade}")
        
s1=student("Arjit",20,"A")
s2=student("Priya",20,"A")
s3=student("abhi",20,"A")
s4=student("ishu",20,"A")

s1.display()
s2.display()
s3.display()
s4.display()
# Q4.  Create a class Counter with an attribute count = 0.
#      Add methods:
#      - increment() → increases count by 1
#      - decrement() → decreases count by 1
#      - reset()     → sets count back to 0
#      - get_count() → returns current count


class Counter:
    def  __init__(self,count=0):
        self.count=count
    
    def increment(self):
        self.count+=1
        print(self.count)
    def decrement(self):
        self.count-=1
        print(self.count)
    def reset(self):
        self.count=0
        print(self.count)
    def get_count(self):
        print(self.count)
        
c1 = Counter(25)
c1.increment()
c1.decrement()
c1.get_count()
c1.reset()
        
# Q5.  Create a class Circle with attribute radius.
#      Add methods:
#      - area()         → returns π * r²   (use math.pi)
#      - circumference() → returns 2 * π * r

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f"Area : {3.14 * (self.radius**2)}")
        
    def circumference(self):
        print(f"circumference : {3.14*2*self.radius}")
        
c1 = Circle(5)
c1.area()
c1.circumference()

# Q6.  Create a class BankAccount with attributes owner and balance.
#      Add methods:
#      - deposit(amount)  → adds amount to balance
#      - withdraw(amount) → deducts amount (print error if insufficient)
#      - get_balance()    → returns current balance


class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        
    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} is deposited in your account,Totalbalance :{self.balance}")
        
    def withdraw(self,amount):
        if amount > self.balance:
            print(f"insufficient Balance, Balance:{self.balance}")
        else:
            self.balance-=amount
            print(f"{amount} is debited , current balance : {self.balance}")
    def get_balance(self):
        print(f"balance  : {self.balance}")
            
b1=BankAccount("Arjit kumar")
b1.deposit(2000)
b1.withdraw(100)
b1.get_balance()
        

# Q7.  Create a class Temperature with attribute celsius.
#      Add methods:
#      - to_fahrenheit() → returns (celsius * 9/5) + 32
#      - to_kelvin()     → returns celsius + 273.15

class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    
    def to_fahrenheit(self):
        return (self.celsius * 9/5) +32
    
    def to_kelvin(self):
        return self.celsius + 273.15
    
t1 = Temperature(25)
print(t1.to_fahrenheit())
print(t1.to_kelvin())

# Q8.  Create a class Person with attributes name and age.
#      Add a class method from_birth_year(name, year) that creates
#      a Person object using birth year instead of age.
#      (Assume current year = 2025)


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def from_birth_year(self,name, year):
        self.age= 2025-year
        
        print(f"name : {self.name} and age : {self.age}")
p1=Person("Arjit",20)  
# p1.from_birth_year() 
p1.from_birth_year("ishu",2006)    
    
# Q9.  Create a class MathUtils with only static methods:
#      - add(a, b)
#      - subtract(a, b)
#      - multiply(a, b)
#      - divide(a, b)
#      (No instance needed to call these)

class MathUtils:
    
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def subtract(a,b):
        return a-b
    
    @staticmethod
    def product(a,b):
        return a*b
    
    @staticmethod
    def div(a,b):
        return a/b
    
print(MathUtils.add(5,3))
print(MathUtils.subtract(5,3))
print(MathUtils.product(5,3))
print(MathUtils.div(4,2))
    
        


# Q10. Create a class Laptop with attributes brand, model, and price.
#      Add a method is_affordable() that returns True if price < 50000,
#      False otherwise.

class laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        
    def is_affordable(self):
        if self.price < 50000:
            return True
        else:
            return False
        
l1=laptop("Acer","Nitro v",89999)
print(l1.is_affordable())
         


# ─────────────────────────────────────────────
#  LEVEL 2 : MEDIUM
# ─────────────────────────────────────────────

# --- INHERITANCE ---

# Q11. Create a base class Animal with:
#      - attribute: name
#      - method: speak() → prints "Some generic sound"
#      Create two subclasses:
#      - Cat  → speak() prints "<name> says: Meow!"
#      - Dog  → speak() prints "<name> says: Woof!"
#      Demonstrate polymorphism by calling speak() on a list
#      containing both Cat and Dog objects.


class Animal:
    def __init__(self,name):
        self.name=name
        
    def speak(self):
        print("Some generic sound")
        
class Cat(Animal):
    
    def speak(self):
        print(f"{self.name} says: Meow!")


class Dog(Animal):
    
    def speak(self):
        print(f"{self.name} says: Woof!")
        
dog=Dog("max")
dog.speak()
cat=Cat("pluto")
cat.speak()

# Q12. Create a class Shape with a method area() that returns 0.
#      Create subclasses:
#      - Triangle(base, height)  → area = 0.5 * base * height
#      - Rectangle(length, width) → area = length * width
#      - Circle(radius)          → area = π * r²
#      Write a function print_areas(shapes) that prints the area
#      of each shape in a list.

class Shape:
    
    def area(self):
        pass
    
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return f"Area : {0.5 * self.base * self.height}"

# Q13. Create a class Vehicle with attributes make, model, year.
#      Add a method description() that returns a formatted string.
#      Create a subclass Car with an extra attribute num_doors.
#      Override description() to include num_doors info.
#      Use super() to call the parent method.

class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def description(self):
        return f"{self.year}, {self.make},{self.model}"
    
class car(Vehicle):
    def __init__(self, make, model, year,num_doors):
        super().__init__(make, model, year)
        self.num_doors=num_doors
        
    def description(self):
        parent = super().description()
        return f" {parent},{self.num_doors}"
        
c1 = car("arjit","toyota",2001,6)
print(c1.description())
# Q14. Create a class Employee with attributes name and salary.
#      Add a method annual_salary() → returns salary * 12.
#      Create a subclass Manager that inherits Employee and adds
#      a bonus attribute.
#      Override annual_salary() → returns (salary * 12) + bonus.


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def annual_salary(self):
        return f"Annual salary: {self.salary*12}"
    
class Manager(Employee):
    def __init__(self, name, salary,bonus):
        super().__init__(name, salary)
        self.bonus=bonus
    def annual_salary(self):
        return f"Annual Salary: {(self.salary * 12)+ self.bonus}"
    
m = Manager("arjit",60000,5000)
print(m.annual_salary())

# --- ENCAPSULATION ---

# Q15. Create a class Person with private attributes __name and __age.
#      Add getter and setter methods for both.
#      The setter for age should raise a ValueError if age < 0.

class Person :
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    
    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name
        
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age<0:
            print("raied a error (value can't be negative)")
        self.__age=age
        
p1=Person("Arjit",20)
print(p1.get_age())
print(p1.get_name())
p1.set_age(21)
p1.set_name("abhi")
print(p1.get_age())
print(p1.get_name())
        



# Q16. Create a class Student with a private attribute __marks (a list).
#      Add methods:
#      - add_mark(mark)   → appends to __marks
#      - get_average()    → returns average of marks
#      - get_highest()    → returns highest mark
#      - get_lowest()     → returns lowest mark

class Student:
    def __init__(self,marks:list):
        self.__marks=marks
    
    def add_mark(self,mark):
        self.__marks.append(mark)
    def get_average(self):
        return f"Avg : {sum(self.__marks)/len(self.__marks)}"
    def get_highest(self):
        return f"highest mark: {max(self.__marks)}"
    def get_lowest(self):
        return f"lowest mark : {min(self.__marks)}"
    
m1=Student([22,55,75,45,98])
m1.add_mark(99)
print(m1.get_average())
print(m1.get_highest())
print(m1.get_lowest())
    
    
        

# --- MAGIC / DUNDER METHODS ---

# Q17. Create a class Book with attributes title, author, and pages.
#      Implement:
#      - __str__()  → "Title by Author (X pages)"
#      - __repr__() → "Book('Title', 'Author', X)"
#      - __len__()  → returns number of pages

class Book:
    def __init__(self,title,aurthor,pages):
        self.title=title
        self.aurthor=aurthor
        self.pages=pages
        
    def __str__(self):
        return f"{self.title} by {self.aurthor},({self.pages}pages)"
    def __repr__(self):
        return f"Book('{self.title}','{self.aurthor}',{self.pages})"
    def __len__(self):
        return self.pages

b1=Book("Python","Harry",28)

print(str(b1))
print(repr(b1))
print(len(b1))

# Q18. Create a class Vector with attributes x and y.
#      Implement:
#      - __add__(other)  → adds two vectors
#      - __sub__(other)  → subtracts two vectors
#      - __str__()       → "Vector(x, y)"
#      Example: Vector(1,2) + Vector(3,4) → Vector(4,6)

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)  
print(v1 - v2)  

    

# Q19. Create a class Fraction with attributes numerator and denominator.
#      Implement:
#      - __str__()       → "num/den"
#      - __add__(other)  → adds two fractions (simplify using gcd)
#      - __eq__(other)   → checks if two fractions are equal

from math import gcd

class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    def __add__(self, other):
        num =self.numerator*other.denominator+other.numerator*self.denominator
        den =self.denominator*other.denominator

        common = gcd(num, den)
        return Fraction(num // common, den // common)

    def __eq__(self, other):
        return (self.numerator*other.denominator == other.numerator*self.denominator)


f1 =Fraction(1,2)
f2 =Fraction(1,3)

print(f1 + f2)      
print(f1 == f2)     
print(Fraction(2, 4) == Fraction(1, 2))  

# Q20. Create a class ShoppingCart with a list of items.
#      Implement:
#      - add_item(name, price)
#      - __len__()    → number of items in cart
#      - __str__()    → prints all items with prices
#      - total()      → returns total price of all items

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))

    def __len__(self):
        return len(self.items)

    def __str__(self):
        result = "Shopping Cart:\n"
        for name, price in self.items:
            result += f"{name}: ₹{price}\n"
        return result

    def total(self):
        return sum(price for name, price in self.items)


# Create cart
cart = ShoppingCart()

# Add items
cart.add_item("Laptop", 50000)
cart.add_item("Mouse", 500)
cart.add_item("Keyboard", 1500)

# Print cart
print(cart)

# Number of items
print("Number of items:", len(cart))

# Total price
print("Total Price: ₹", cart.total())
# ─────────────────────────────────────────────
#  LEVEL 3 : HARD
# ─────────────────────────────────────────────

# --- ABSTRACTION ---

# Q21. Using the abc module, create an abstract class Payment with
#      an abstract method process(amount).
#      Create three concrete subclasses:
#      - CreditCard  → prints "Paid ₹X via Credit Card"
#      - UPI         → prints "Paid ₹X via UPI"
#      - NetBanking  → prints "Paid ₹X via Net Banking"

# Q22. Create an abstract class Notification with abstract method send().
#      Create subclasses:
#      - EmailNotification(to, subject)
#      - SMSNotification(phone, message)
#      Each should implement send() to display relevant info.

# --- MULTIPLE INHERITANCE ---

# Q23. Create classes Flyable and Swimmable each with methods fly()
#      and swim() respectively.
#      Create a class Duck that inherits from both and also adds
#      a method quack().
#      Demonstrate all three methods.

# Q24. Demonstrate Python's MRO (Method Resolution Order):
#      Create classes A, B, C where B and C both inherit from A,
#      and class D inherits from both B and C (Diamond problem).
#      Override a method greet() at each level and show which one
#      gets called. Print D.__mro__ to verify the order.

# --- PROPERTIES & DESCRIPTORS ---

# Q25. Create a class Circle using @property:
#      - radius property with getter and setter
#        (setter should raise ValueError if radius < 0)
#      - read-only property area  → π * r²
#      - read-only property circumference → 2 * π * r

# Q26. Create a class Employee with:
#      - @property salary → returns private __salary
#      - @salary.setter   → raises ValueError if salary < 0
#      - @property annual → returns salary * 12
#      - @staticmethod department() → returns "Engineering"

# --- ADVANCED OOP ---

# Q27. Implement a Singleton class where only ONE instance can
#      ever be created. If you try to create a second instance,
#      the same original instance is returned.
#      Hint: Override __new__()

# Q28. Create a class Matrix (2D list) with:
#      - __add__(other)    → matrix addition
#      - __mul__(other)    → matrix multiplication
#      - __str__()         → nicely formatted grid
#      - transpose()       → returns transposed matrix

# Q29. Implement a custom iterator class NumberRange that works
#      like range() but only yields even numbers between start and stop.
#      It must implement __iter__() and __next__().
#      Example: list(NumberRange(1, 10)) → [2, 4, 6, 8]

# Q30. Create a class EventSystem (Observer Pattern):
#      - subscribe(event, listener)   → register a listener function
#      - unsubscribe(event, listener) → remove a listener
#      - emit(event, data)            → call all listeners for that event
#      Demonstrate with at least 2 events and 3 listeners.


# ─────────────────────────────────────────────
#  BONUS CHALLENGES
# ─────────────────────────────────────────────

# B1. Create a decorator @timer that measures and prints the
#     execution time of any method inside a class.

# B2. Implement a class Stack using __len__, __iter__, __contains__
#     so it supports: len(stack), for x in stack, and x in stack.

# B3. Create a metaclass UpperCaseMeta that automatically converts
#     all method names defined in a class to uppercase.
#     Hint: Override __new__ in the metaclass.

# B4. Implement a class JSONSerializable with a method to_json()
#     that converts the object's __dict__ to a JSON string,
#     and a class method from_json(json_str) that recreates the object.

# B5. Create a class Chain where every method returns self,
#     allowing method chaining like:
#     Chain().set_name("Arjit").set_age(20).set_city("Delhi").display()
