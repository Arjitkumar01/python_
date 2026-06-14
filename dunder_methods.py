#1  __init__

class Student:
    def __init__(self,name):
        self.name=name
    
    def display(self):
        return self.name
s1=Student("Arjit")
print(s1.display())


#2 __str__  and __repr__

# Dono same work karta hai ,__repr__ is used by the developer to debug
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    
    def __str__(self):
        return f"name : {self.name} & roll : {self.roll}"
         
    def __repr__(self):
        return f"name : {self.name} & roll : {self.roll}"
    
    
#3  __len__
    def __len__(self):
        return len(self.name)
    
s1=Student("Arjit","2025btcs050")
print(len(s1))
print(str(s1))
print(repr(s1))



class maths:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return maths(self.value + other.value)
    def __sub__(self,other):
        return maths(self.value - other.value)
    def __mul__(self,other):
        return maths(self.value * other.value)
    
    def __truediv__(self,other):
        return maths(self.value / other.value)
    
    
a = maths(4)
b = maths(4)

c = a + b
d = a - b
e = a * b
f = a / b
print(c.value)
print(d.value)
print(e.value)
print(f.value)

#  __eq__ OR __ne__ OR __lt__ OR __gt__

class Student:
    def __init__(self,value):
        self.value=value
        
    def __eq__(self, other):
        return Student(self.value == other.value)
    def __ne__(self, other):
        return Student(self.value != other.value)
    def __gt__(self, other):
        return Student(self.value > other.value)
    def __lt__(self, other):
        return Student(self.value < other.value)
    
a=Student(5)
b=Student(4)

c = a==b
d = a!=b
e = a>b
f = a<b
print(c.value)
print(d.value)
print(e.value)
print(f.value)