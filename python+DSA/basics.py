# a = 5
# b =6

# print("a equals to",a,"hi",b)


# lang=["python","java","c++","javascript"]


# uses={"python":"web development","java":"mobile app development","c++":"game development","javascript":"web development"}


# print("Languages:", lang)
# print("Uses of languages:", uses)


# combined = lang + list(uses.items())
# print("Combined:", combined)



# # types of operators

# # Arithmetic Operators: +, -, *, /, %, **, //
    
# a = 10
# b = 3

# print(a + b)   # Addition
# print(a - b)   # Subtraction
# print(a * b)   # Multiplication
# print(a / b)   # Division
# print(a % b)   # Modulus
# print(a // b)  # Floor Division
# print(a ** b)  # Exponentiation



# # Comparison Operators: ==, !=, >, <, >=, <=    
# a = 10
# b = 5

# print(a == b)  # Equal to
# print(a != b)  # Not equal to
# print(a > b)   # Greater than
# print(a < b)   # Less than
# print(a >= b)  # Greater than or equal to
# print(a <= b)  # Less than or equal to


# # Assignment Operators: =, +=, -=, *=, /=, %=, **=,

# a = 10

# a += 5
# print(a)

# a -= 2
# print(a)

# a *= 3
# print(a)

# a /= 2
# print(a)

# a %= 4
# print(a)

# a //= 2
# print(a)

# a **= 2
# print(a)


# # Logical Operators: and, or, not

# a = True
# b = False

# print(a and b)  
# print(a or b)   
# print(not a)    

# # membership Operators: in, not in

# name = "Arjit"

# print("A" in name)
# print("z" in name)

# print("A" not in name)
# print("z" not in name)

# # identity Operators: is, is not    


# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(a is b)
# print(a is c)

# print(a is not c)

# # loops

# for i in range(5):
#     print(i)        
    
    
# i = 0
# while i < 5:    
#     print(i)
#     i += 1

# order_queue = {"table1": "order1", "table2": "order2", "table3": "order3"}

# for table, order in order_queue.items():
#     print(f"Processing {order} for {table}")

# print(order_queue)


# row =[1,2,3,4,5]

# for row in row:
#     print("row:", row)
#     for seat in range(1, 6):
#         print("row:", row, "seat:", seat)

# functions

# def greet(name):
#     return (f"Hello, {name}!")


# print(greet("Arjit"))

# default parameters

# def greet(name, msg="Welcome"):
#     return (f"Hello, {name}! {msg}")


# print(greet("Arjit", "Good to see you!"))
# print(greet("Arjit"))


# # call by value and call by reference
# def modify_list(lst):
#     lst.append(4)
#     print("Inside function:", lst)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print("Outside function:", my_list)


# def add(a, b):
#     print(a + b)

# result = add(5, 3)
# print(result)





# def add(a, b):
#     return a + b

# result = add(5, 3)
# print(result)


# def add(a, b):

#     print(a + b)
    
    
# add(5, 3)
# # result = add(5, 3)
# # print(result)

# def area_of_rectangle(length, width):
#     return length * width

# print(area_of_rectangle(5, 3))



# def add(a, b):

#     print(a + b)


# sum = add(5, 3)

# print(sum) 

# --------------------------------------------------------------------------------------------------------------------------------
arr=[2,3,5,6,7,8,9,7,5]
target = 7

def linear_search(arr,target):
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
print(linear_search(arr,target))
    
        
        
    


