# Write a program to print multiplication table of a given number using for loop??

# num = int(input("Enter a number:"))
# for i in range (1,11):
#     print(f"{num} x {i} = {num*i}")
    
    
    
# Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for i in l:
#     if i.startswith("S"):
#         print(f"Hello..{i}")

# Attempt problem 1 using while loop.
# num = int(input("Enter a number:"))
# i =1
# while i<=10:
#     print(f"{num} x {i} = {num*i}")
#     i+=1



# Write a program to find whether a given number is prime or not.

# a = int(input("Enter any number :"))

# if a <= 0:
#     print("not prime")
# else:
#     is_prime=True
    
#     for i in range(2,int(a**0.5)+1) :
#         if a % i == 0:
#             is_prime = False
#             break
        
#     if is_prime:
#         print("prime")
#     else:
#         print("not prime")
        
        
#  Write a program to find the sum of first n natural numbers using while loop   
            
            
# num = int(input("enter any number:"))

# for i in range(0,num+1):
#     sum= i + (i+1)
# print(sum)


# Write a program to calculate the factorial of a given number using for loop.

# factorial = 1

# for i in range(1,num+1):
#     factorial*=i
    
# print(factorial)

'''#  Write a program to print the following star pattern.
*
***
***** for n = 3 '''

# for i in range(1,6):
#     for j in range(2*i-1):
#         print("*", end="")
#     print("\n")
        
'''    
. Write a program to print the following star pattern:
*
**
*** for n = 3'''

# n = 3

# for i in range(1,n+1):
#     print("*" * i)
    
    
# for i in range(0,3):
#     print("*" * 3)
    
    
# num=5

# for i in range(10,0,-1):
#     print(f"{num} x {i} = {num*i}")


# -----------------------------------------------------------------------------------------------------------------------------------------------------

# _________FUNCTION QUESTION__________

# . Write a program using functions to find greatest of three numbers.

# def greatest(a,b,c): 
#     if a>b and a>c:
#         return f"{a} is greatest"
#     elif b>c:
#         return f"{b} is greatest"
#     else:
#         return f"{c} is greatest"
# g1 =greatest(208,47,9)
# print(g1)


# Write a python program using function to convert Celsius to Fahrenheit.


# def fahrenheit(calcius):
#     fah = (calcius * 9/5) +32
    
#     return fah

# print(fahrenheit(87))
    
    
# def sum(n):
#     if n == 1:
#         return 1
#     return n+sum(n-1)

# print(sum(5))

# How do you prevent a python print() function to print a new line at the end

# print("Hello", end="")
# print("World")

#  Write a python function which converts inches to cms

# def inches_to_cms(inches):
#     cms  = inches * 2.54
#     return cms


# print(inches_to_cms(2))

# Write a python function to remove a given word from a list and strip it at the same time.
# def remove(given_word,list):
#     if given_word in list:
#         list.remove(given_word)
#         return list
#     else:
#         return "word not found in list"
    
# l1= remove("apple",["banana","grapes","apple"]) 

# print(l1)

# def multipication_table(n):
#     for i in range(1,11):
#         print(f"{n} x {i} = {n*i}")
    

# multipication_table(5)


# import random


# choices = ["snake","water","gun"]

# computer = random.choice(choices)

# user=input("Enter snake,water or gun:")


# if user ==computer:
#     print(f"Game Draw both choose {user}")
    
# elif (user=="snake" and computer=="water") or (user=="water" and computer == "gun") or (user == "gun" and computer== "snake"):
#     print(f"user choose {user} and computer choose {computer}")
#     print("user wins")
    
# else:
#     print(f"user choose {user} and computer choose {computer}")
#     print("computer wins")



# selection sort

arr= [2,5,7,9,6]

for i in range(len(arr)):
    min_idx=i
    
    for j in range(i+1,len(arr)):
        if arr[i]> arr[j]:
            min_idx = j
    
        arr[i],arr[min_idx] = arr[min_idx],arr[i]

print(arr)

        
