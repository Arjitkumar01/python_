# # # ============================================================
# # #           PYTHON ARRAYS - EASY PRACTICE QUESTIONS
# # #     (Using Python lists as arrays + array module basics)
# # # ============================================================

# # # ── WHAT IS AN ARRAY? ────────────────────────────────────────
# # # An array is a collection of items stored at contiguous memory
# # # locations. In Python, we use:
# # #   1. Lists        → built-in, can hold mixed types
# # #   2. array module → strict type, like C arrays
# # #   3. NumPy arrays → for scientific computing
# # #
# # # For these questions we'll use Python LISTS as arrays.
# # # ─────────────────────────────────────────────────────────────


# # # ── SECTION 1 : CREATING & ACCESSING ─────────────────────────

# # # Q1.  Create an array (list) of 5 integers and print it.

# list = [1,2,3,4,5]

# print(list)
# # print("---------------------------------------------")
# # # Q2.  Create an array of 5 fruits.
# # #      - Print the first element.
# # #      - Print the last element using negative indexing.
# # #      - Print the middle element.

# fruits = ["apple", "banana", "cherry", "mango", "grape"]
# print(fruits[0])
# print(fruits[-1])
# print(fruits[2])
# print("---------------------------------------------")
# # # Q3.  Create an array of numbers from 1 to 10 using range()
# # #      and print each element on a new line using a for loop.
# arr=[]
# for i in range(1,11):
#     arr.append(i)
    

# print(arr)
# for j in range(len(arr)):
#     print(arr[j] )
# print("---------------------------------------------")
# # # Q4.  Given the array below, print elements at index 0, 2, and 4.

# arr = [10, 20, 30, 40, 50]
# print(arr[0])
# print(arr[2])
# print(arr[4])
# print("---------------------------------------------")
# # Q5.  Given the array below, print the last 3 elements using slicing.
# arr = [5, 10, 15, 20, 25, 30]
# print(arr[-3:])
# print("---------------------------------------------")

# # # ── SECTION 2 : MODIFYING ARRAYS ─────────────────────────────

# # # Q6.  Create an array [1, 2, 3, 4, 5].
# # #      - Add 6 at the end using append().
# # #      - Add 0 at the beginning using insert().
# # #      - Print the final array.


# integers = [1, 2, 3, 4, 5]
# integers.append(6)
# integers.insert(0,0)
# print(integers)
# print("---------------------------------------------")
# # # Q7.  Given arr = [1, 2, 3, 4, 5]:
# # #      - Remove the element 3 using remove().
# # #      - Remove and print the last element using pop().
# # #      - Print the final array.

# arr = [1, 2, 3, 4, 5]

# arr.remove(3)
# arr.pop()
# print(arr)
# print("---------------------------------------------")

# # # Q8.  Given arr = [10, 20, 30, 40, 50]:
# # #      Change the element at index 2 to 99 and print the array.

# arr = [10, 20, 30, 40, 50]
# arr.remove(30)

# arr.insert(2,99)
# print(arr)
# print("---------------------------------------------")

# # # Q9.  Given arr = [3, 1, 4, 1, 5, 9, 2, 6]:
# # #      Sort the array in ascending order and print it.
# # #      Then sort it in descending order and print it.

# arr = [3, 1, 4, 1, 5, 9, 2, 6]
# arr.sort()
# print(arr)
# arr.reverse()
# print(arr)
# print("---------------------------------------------")
# # # Q10. Given arr = [1, 2, 3, 4, 5]:
# #      Reverse the array and print it.
# #      (Try two ways: using reverse() method and using slicing [::-1])

# arr = [1, 2, 3, 4, 5]

# print(arr[::-1])

# arr.reverse()
# print(arr)
# print("---------------------------------------------")



# # ── SECTION 3 : SEARCHING & COUNTING ─────────────────────────

# # Q11. Given arr = [10, 20, 30, 40, 50]:
# #      Check if 30 is in the array. Print True or False.


# arr = [10,20,30,40,50]
# to_find=30

# if to_find in arr:
#     print(True)
# else:
#     print(False) 
# print("---------------------------------------------")

    

        

# # Q12. Given arr = [5, 3, 8, 1, 9, 2, 7]:
# #      Find and print the maximum and minimum element
# #      using built-in functions.

# arr = [5, 3, 8, 1, 9, 2, 7]

# arr.sort()

# print(f"minimum value : {arr[0]}")
# print(f"maximum value : {arr[-1]}")

# print(max(arr))
# print(min(arr))
# print("---------------------------------------------")

# # Q13. Given arr = [4, 2, 7, 1, 9, 3]:
# #      Find the sum and average of all elements.

# arr = [4, 2, 7, 1, 9, 3]
# sum =0
# for i in arr:
#     sum+=i
# print(f"sum of all elements: {sum}")
# print(f"Average of all elements: {sum//len(arr)}")
# print("---------------------------------------------")
    


# # Q14. Given arr = [1, 2, 3, 2, 4, 2, 5]:
# #      Count how many times the number 2 appears using count().

# arr = [1, 2, 3, 2, 4, 2, 5]
# print(arr.count(2))
# print("---------------------------------------------")

# Q15. Given arr = [10, 20, 30, 40, 50]:
#      Find the index (position) of element 30 using index().

# arr = [10, 20, 30, 40, 50]
# print(arr.index(30))
# print("---------------------------------------------")

# ── SECTION 4 : LOOPING THROUGH ARRAYS ───────────────────────

# Q16. Given arr = [2, 4, 6, 8, 10]:
#      Print each element multiplied by 2.

# arr = [2, 4, 6, 8, 10]

# for i in arr:
#     print(i*2)
# print("---------------------------------------------")


# Q17. Given arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#      Print only the even numbers from the array.

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range(0,len(arr)):
#     if arr[i] %2==0:
#         print(arr[i],end=",")
#     else:
#         continue

# Q18. Given arr = ["apple", "banana", "cherry", "mango"]:
#      Print each fruit along with its index number.
#      Output format:  0 : apple
#                      1 : banana  ... etc
#      (Use enumerate())

# arr = ["apple", "banana", "cherry", "mango"]

# for i in range(len(arr)):
#     print(f" {i} : {arr[i]}")

# for index,fruits in enumerate(arr):
#     print(index,fruits)
    



# Q19. Given arr = [1, 2, 3, 4, 5]:
#      Calculate and print the sum of all elements
#      WITHOUT using the built-in sum() function.
# sum=0
# arr = [1, 2, 3, 4, 5]
# for i in range(len(arr)):
#     sum+=arr[i]
# print(sum)
    







# ── SECTION 5 : ARRAY OPERATIONS ─────────────────────────────

# Q21. Create two arrays:
#      arr1 = [1, 2, 3]
#      arr2 = [4, 5, 6]
#      Merge them into a single array and print it.
#      Expected: [1, 2, 3, 4, 5, 6]


# arr1 = [1, 2, 3]
# arr2 = [4, 5, 6]    
# arr3 = arr1 + arr2
# print(arr3)

# Q22. Given arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#      Create a new array containing only elements
#      greater than 5.
#      Expected: [6, 7, 8, 9, 10]

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_arr=[]
# for i in arr:
#     if i>5:
#         new_arr.append(i)
# print(new_arr)
        


# Q23. Given arr = [1, 2, 2, 3, 4, 4, 5]:
#      Remove all duplicate elements and print the unique array.
#      Expected: [1, 2, 3, 4, 5]

# arr = [1, 2, 2, 3, 4, 4, 5]

# new_arr = list(set(arr)) #yaha ye work nii karega kyuki list name se overwrite ho raha hai ,cause maine list name use kiys h dusre qno maii..
# print(new_arr)

# Q24. Given arr = [1, 2, 3, 4, 5]:
#      Create a new array where every element is squared.
#      Expected: [1, 4, 9, 16, 25]

# arr = [1, 2, 3, 4, 5]
# new_arr=[]

# for i in arr:
#     new_arr.append(i*i)
    
# print(new_arr)

# Q25. Given arr = [10, 20, 30, 40, 50]:
#      Write code to print the array in reverse order
#      WITHOUT using reverse() or [::-1].
#      (Use a loop with range)




# ── SECTION 6 : 2D ARRAYS (BONUS EASY) ───────────────────────

# Q26. Create a 2D array (3x3 matrix) like this:
#      [[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]]
#      Print each row on a separate line.

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# for row in matrix:
#     print(row)

# # Q27. Using the 3x3 matrix from Q26:
#      Access and print the element at row 1, column 2 (value = 6).

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[1][2])  


# Q28. Using the 3x3 matrix from Q26:
#      Print all elements one by one using a nested for loop.
# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])) :
#         print(matrix[i][j], end=",")
#     print()
   
        


# Q29. Create a 2D array of zeros with 3 rows and 4 columns.
#      Expected:
#      [[0, 0, 0, 0],
#       [0, 0, 0, 0],
#       [0, 0, 0, 0]]

# arr = [[0 for j in range(4)]for i in range(3)]
# for i in range(len(arr)):
#     print(arr[i])



# Q30. Given the 2D array:
#      matrix = [[1,2,3],[4,5,6],[7,8,9]]
#      Find and print the sum of all elements in the matrix.
#      Expected: 45
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# result=0
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         result+=matrix[i][j]
    
# print(result)
        


# ─────────────────────────────────────────────
#  QUICK REFERENCE — ARRAY METHODS
# ─────────────────────────────────────────────
# arr.append(x)       → add x at end
# arr.insert(i, x)    → add x at index i
# arr.remove(x)       → remove first occurrence of x
# arr.pop()           → remove & return last element
# arr.pop(i)          → remove & return element at index i
# arr.sort()          → sort in ascending order (in-place)
# arr.sort(reverse=True) → sort descending
# arr.reverse()       → reverse in-place
# arr.count(x)        → count occurrences of x
# arr.index(x)        → first index of x
# arr.clear()         → remove all elements
# len(arr)            → number of elements
# arr[i]              → access element at index i
# arr[start:end]      → slicing
# arr[::- 1]          → reversed copy


# ============================================================
#       SECTION 7 : Python's array MODULE (import array)
# ============================================================
#
# The built-in `array` module creates arrays that store only
# ONE type of data (like int, float, char).
# This is more memory-efficient than a regular list.
#
# HOW TO IMPORT:
#   from array import array
#   OR
#   import array
#
# SYNTAX:
#   arr = array('typecode', [values])
#
# COMMON TYPECODES:
#   'i'  → signed integer   (2 or 4 bytes)
#   'f'  → float            (4 bytes)
#   'd'  → double / float   (8 bytes)
#   'u'  → unicode char
#   'b'  → signed byte
#
# ─────────────────────────────────────────────────────────────


# Q31. Import the array module and create an integer array
#      with values [10, 20, 30, 40, 50].
#      Print the array and its type.

from array import array

# arr = array('i',[10, 20, 30, 40, 50])
# print(arr)

# Q32. Create a float array with values [1.5, 2.5, 3.5, 4.5].
#      Print each element using a for loop.

# arr = array('f',[1.5, 2.5, 3.5, 4.5])

# for i in range(len(arr)):
#     print(arr[i])

# Q33. Create an integer array arr = array('i', [1, 2, 3, 4, 5]).
#      - Append 6 to the array using append().
#      - Print the updated array.
# arr = array('i', [1, 2, 3, 4, 5])

# arr.append(6)
# print(arr)


# Q34. Create an integer array arr = array('i', [10, 20, 30, 40, 50]).
#      - Insert 99 at index 2.
#      - Print the updated array.
#      Expected: array('i', [10, 20, 99, 30, 40, 50])
# arr = array('i', [10, 20, 30, 40, 50])
# arr.insert(2,99)
# print(arr)


# Q35. Create an integer array arr = array('i', [5, 10, 15, 20, 25]).
#      - Remove the element 15 using remove().
#      - Pop the last element using pop().
#      - Print the final array.
# arr = array('i', [5, 10, 15, 20, 25])
# arr.remove(15)
# arr.pop()
# print(arr)
 
 


# Q36. Create an integer array arr = array('i', [3, 1, 4, 1, 5, 9]).
#      Access and print:
#      - First element
#      - Last element (using negative index)
#      - Element at index 3

# arr = array('i', [3, 1, 4, 1, 5, 9])
# print(arr[1])
# print(arr[-1])
# print(arr[3])


# Q37. Create an integer array arr = array('i', [10, 20, 30, 40, 50]).
#      - Slice and print elements from index 1 to 3.
#      Expected: array('i', [20, 30, 40])

# arr = array('i', [10, 20, 30, 40, 50])

# new_arr=array(arr.typecode,arr[1:4])
# print(new_arr)



# Q38. Create an integer array arr = array('i', [1, 2, 3, 2, 4, 2]).
#      - Find how many times 2 appears using count().
#      - Find the index of first occurrence of 3 using index().

# arr = array('i', [1, 2, 3, 2, 4, 2])
# count=0
# for i in range(len(arr)):
#     if arr[i]==2:
#         count+=1
#     else:
#         continue
# print(count)

# print(arr.index(3))

    

# Q39. Create two integer arrays:
#      arr1 = array('i', [1, 2, 3])
#      arr2 = array('i', [4, 5, 6])
#      Concatenate (merge) them using + operator and print the result.
#      Expected: array('i', [1, 2, 3, 4, 5, 6])
# arr1 = array('i', [1, 2, 3])
# arr2 = array('i', [4, 5, 6])
# arr3 = arr1 +arr2

# print(arr3)
# Q40. Create an integer array arr = array('i', [1, 2, 3, 4, 5]).
#      Convert it to a regular Python list using tolist()
#      and print both the array and the list.





# Q41. Try to add a float value to an integer array:
#      arr = array('i', [1, 2, 3])
#      arr.append(4.5)
#      What error do you get? Write it as a comment and explain why.
# arr = array('i', [1, 2, 3])
# arr.append(4.5)
# can't be added because the datatype is integer and and array only contain one datatype at a time
# Q42. Create a float array arr = array('f', [1.1, 2.2, 3.3, 4.4, 5.5]).
#      Find the sum of all elements using a for loop
#      (do NOT use the built-in sum()).
# arr = array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
# result=0
# for i in range(len(arr)):
#     result+=arr[i]
# print(result)
    

# Q43. Create an integer array arr = array('i', [5, 3, 8, 1, 9, 2]).
#      Convert it to a list, sort it, and convert back to an array.
#      Print the final sorted array.
# arr = array('i', [5, 3, 8, 1, 9, 2])
# lst =list(arr)
# lst.sort()
# arr=array('i',lst)
# print(arr)




# Q44. Create an integer array with values from 1 to 10 using
#      a loop (do NOT write all values manually).
#      Hint: Start with an empty array array('i') and use append().

# arr = array('i',[])

# for i in range(1,11):
#     arr.append(i)
# print(arr)

# Q45. Create an integer array arr = array('i', [10, 20, 30, 40, 50]).
#      Reverse it and print.
#      Hint: Convert to list → reverse → convert back to array.

# arr = array('i', [10, 20, 30, 40, 50])

# lst=list(arr)
# lst.reverse()

# arr=array('i',lst)
# print(arr)


# ─────────────────────────────────────────────
#  QUICK REFERENCE — array MODULE
# ─────────────────────────────────────────────
# from array import array
#
# array(typecode, [values]) → create array
# arr.append(x)             → add element at end
# arr.insert(i, x)          → insert at index i
# arr.remove(x)             → remove first occurrence of x
# arr.pop(i)                → remove & return element at i
# arr.index(x)              → index of first occurrence of x
# arr.count(x)              → count occurrences of x
# arr.reverse()             → reverse in-place
# arr.tolist()              → convert to Python list
# arr.typecode              → returns the typecode ('i','f', etc.)
# len(arr)                  → number of elements
# arr[i]                    → access element at index i
# arr[start:end]            → slicing
# arr1 + arr2               → concatenate two arrays (same typecode)
