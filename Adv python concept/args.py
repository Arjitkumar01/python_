# ARGS SARE VALUES KO EK TUPPLE MAI STORE KARWA DETA HAI
# SO WE CAN ACCESS THEM LIKE TUPLE



# SUM OF NUMBERS USING ARGS

def func1(*args):
    total = 0 
    for i in args:
        total += i
    return total

print(func1(1,2,3,4,5))


# PRINT ALL THE NAMES

def students(*args):
    for name in args:
        print(name)

students("Arjit", "Abhi")