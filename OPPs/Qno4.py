# Q4.  Create a class Student with private __marks (a list).
#      Add:
#        add_mark(m)    → append to __marks
#        get_average()  → return average
#        get_highest()  → return highest mark
#      Access __marks only through these methods.

class Student:
    def __init__(self,marks=[]):
        self.__marks=marks
        
    def add_mark(self,m):
        self.__marks.append(m)
        
    def get_average(self):
        return f"Average: {sum(self.__marks)/len(self.__marks)}"
    def get_highest(self):
        return f"Highest: {max(self.__marks)}"

s1 = Student()
s1.add_mark(1)
s1.add_mark(2)
s1.add_mark(3)
s1.add_mark(4)
s1.add_mark(5)

print(s1.get_average())
print(s1.get_highest())