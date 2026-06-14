# ============================================================
#           PYTHON ARRAYS - ANSWERS (EASY)
# ============================================================


# ── SECTION 1 : CREATING & ACCESSING ─────────────────────────

# Q1. Create an array of 5 integers and print it
arr = [10, 20, 30, 40, 50]
print(arr)                  # [10, 20, 30, 40, 50]


# Q2. Array of 5 fruits — first, last, middle elements
fruits = ["apple", "banana", "cherry", "mango", "grape"]
print(fruits[0])            # apple     → first
print(fruits[-1])           # grape     → last (negative index)
print(fruits[2])            # cherry    → middle


# Q3. Array from 1 to 10 using range(), print each on new line
arr = list(range(1, 11))
for num in arr:
    print(num)


# Q4. Print elements at index 0, 2, 4
arr = [10, 20, 30, 40, 50]
print(arr[0])               # 10
print(arr[2])               # 30
print(arr[4])               # 50


# Q5. Print last 3 elements using slicing
arr = [5, 10, 15, 20, 25, 30]
print(arr[-3:])             # [20, 25, 30]


# ── SECTION 2 : MODIFYING ARRAYS ─────────────────────────────

# Q6. append() at end, insert() at beginning
arr = [1, 2, 3, 4, 5]
arr.append(6)               # add 6 at end
arr.insert(0, 0)            # add 0 at index 0 (beginning)
print(arr)                  # [0, 1, 2, 3, 4, 5, 6]


# Q7. remove() and pop()
arr = [1, 2, 3, 4, 5]
arr.remove(3)               # removes first occurrence of 3
popped = arr.pop()          # removes and returns last element
print(popped)               # 5
print(arr)                  # [1, 2, 4]


# Q8. Change element at index 2
arr = [10, 20, 30, 40, 50]
arr[2] = 99
print(arr)                  # [10, 20, 99, 40, 50]


# Q9. Sort ascending and descending
arr = [3, 1, 4, 1, 5, 9, 2, 6]
arr.sort()
print(arr)                  # [1, 1, 2, 3, 4, 5, 6, 9]
arr.sort(reverse=True)
print(arr)                  # [9, 6, 5, 4, 3, 2, 1, 1]


# Q10. Reverse using reverse() and slicing
arr = [1, 2, 3, 4, 5]

# Way 1 — reverse() method (in-place)
arr.reverse()
print(arr)                  # [5, 4, 3, 2, 1]

# Way 2 — slicing (returns a new array)
arr = [1, 2, 3, 4, 5]
print(arr[::-1])            # [5, 4, 3, 2, 1]


# ── SECTION 3 : SEARCHING & COUNTING ─────────────────────────

# Q11. Check if 30 is in the array
arr = [10, 20, 30, 40, 50]
print(30 in arr)            # True
print(99 in arr)            # False


# Q12. Max and min using built-ins
arr = [5, 3, 8, 1, 9, 2, 7]
print(max(arr))             # 9
print(min(arr))             # 1


# Q13. Sum and average
arr = [4, 2, 7, 1, 9, 3]
total   = sum(arr)
average = total / len(arr)
print(total)                # 26
print(average)              # 4.333...


# Q14. Count occurrences of 2
arr = [1, 2, 3, 2, 4, 2, 5]
print(arr.count(2))         # 3


# Q15. Find index of element 30
arr = [10, 20, 30, 40, 50]
print(arr.index(30))        # 2


# ── SECTION 4 : LOOPING THROUGH ARRAYS ───────────────────────

# Q16. Print each element multiplied by 2
arr = [2, 4, 6, 8, 10]
for num in arr:
    print(num * 2)          # 4 8 12 16 20


# Q17. Print only even numbers
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in arr:
    if num % 2 == 0:
        print(num)          # 2 4 6 8 10


# Q18. Print each fruit with its index using enumerate()
arr = ["apple", "banana", "cherry", "mango"]
for index, fruit in enumerate(arr):
    print(f"{index} : {fruit}")
# 0 : apple
# 1 : banana
# 2 : cherry
# 3 : mango


# Q19. Sum of all elements WITHOUT sum()
arr = [1, 2, 3, 4, 5]
total = 0
for num in arr:
    total += num
print(total)                # 15


# Q20. Largest number WITHOUT max()
arr = [3, 7, 2, 9, 1, 5]
largest = arr[0]
for num in arr:
    if num > largest:
        largest = num
print(largest)              # 9


# ── SECTION 5 : ARRAY OPERATIONS ─────────────────────────────

# Q21. Merge two arrays
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
merged = arr1 + arr2
print(merged)               # [1, 2, 3, 4, 5, 6]


# Q22. Elements greater than 5
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x for x in arr if x > 5]
print(result)               # [6, 7, 8, 9, 10]


# Q23. Remove duplicates
arr = [1, 2, 2, 3, 4, 4, 5]
unique = list(dict.fromkeys(arr))   # preserves order
print(unique)               # [1, 2, 3, 4, 5]

# Alternative using set (order not guaranteed)
# unique = list(set(arr))


# Q24. Square every element
arr = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in arr]
print(squared)              # [1, 4, 9, 16, 25]


# Q25. Print in reverse using a loop (no reverse() or [::-1])
arr = [10, 20, 30, 40, 50]
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")  # 50 40 30 20 10
print()


# ── SECTION 6 : 2D ARRAYS ────────────────────────────────────

# Q26. Create 3x3 matrix and print each row
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    print(row)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]


# Q27. Access element at row 1, column 2
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])         # 6


# Q28. Print all elements using nested loop
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
# 1 2 3
# 4 5 6
# 7 8 9


# Q29. 2D array of zeros — 3 rows, 4 columns
rows, cols = 3, 4
zeros = [[0] * cols for _ in range(rows)]
for row in zeros:
    print(row)
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]


# Q30. Sum of all elements in a 2D matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
total = 0
for row in matrix:
    for element in row:
        total += element
print(total)                # 45


# ============================================================
#       SECTION 7 : Python's array MODULE — ANSWERS
# ============================================================

from array import array


# Q31. Create an integer array and print it with its type
arr = array('i', [10, 20, 30, 40, 50])
print(arr)          # array('i', [10, 20, 30, 40, 50])
print(type(arr))    # <class 'array.array'>


# Q32. Float array — print each element
arr = array('f', [1.5, 2.5, 3.5, 4.5])
for num in arr:
    print(num)
# 1.5  2.5  3.5  4.5


# Q33. Append to integer array
arr = array('i', [1, 2, 3, 4, 5])
arr.append(6)
print(arr)          # array('i', [1, 2, 3, 4, 5, 6])


# Q34. Insert at index 2
arr = array('i', [10, 20, 30, 40, 50])
arr.insert(2, 99)
print(arr)          # array('i', [10, 20, 99, 30, 40, 50])


# Q35. Remove and pop
arr = array('i', [5, 10, 15, 20, 25])
arr.remove(15)      # removes first occurrence of 15
arr.pop()           # removes last element (25)
print(arr)          # array('i', [5, 10, 20])


# Q36. Access elements
arr = array('i', [3, 1, 4, 1, 5, 9])
print(arr[0])       # 3   → first element
print(arr[-1])      # 9   → last element
print(arr[3])       # 1   → index 3


# Q37. Slicing
arr = array('i', [10, 20, 30, 40, 50])
print(arr[1:4])     # array('i', [20, 30, 40])


# Q38. count() and index()
arr = array('i', [1, 2, 3, 2, 4, 2])
print(arr.count(2))     # 3
print(arr.index(3))     # 2


# Q39. Concatenate two arrays using +
arr1 = array('i', [1, 2, 3])
arr2 = array('i', [4, 5, 6])
merged = arr1 + arr2
print(merged)       # array('i', [1, 2, 3, 4, 5, 6])


# Q40. Convert array to list using tolist()
arr = array('i', [1, 2, 3, 4, 5])
lst = arr.tolist()
print(arr)          # array('i', [1, 2, 3, 4, 5])
print(lst)          # [1, 2, 3, 4, 5]
print(type(lst))    # <class 'list'>


# Q41. Try adding float to integer array — ERROR
# arr = array('i', [1, 2, 3])
# arr.append(4.5)
# ERROR: TypeError: integer argument expected, got float
#
# Reason: The array module enforces strict type checking.
# An 'i' (integer) array can only store whole numbers.
# To store floats you need array('f', ...) or array('d', ...)


# Q42. Sum of float array without sum()
arr = array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
total = 0
for num in arr:
    total += num
print(round(total, 2))      # 16.5


# Q43. Sort an integer array
arr = array('i', [5, 3, 8, 1, 9, 2])
lst = arr.tolist()          # convert to list
lst.sort()                  # sort the list
arr = array('i', lst)       # convert back to array
print(arr)                  # array('i', [1, 2, 3, 5, 8, 9])


# Q44. Create array from 1 to 10 using a loop
arr = array('i')
for i in range(1, 11):
    arr.append(i)
print(arr)          # array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# Q45. Reverse an integer array
arr = array('i', [10, 20, 30, 40, 50])
lst = arr.tolist()          # convert to list
lst.reverse()               # reverse the list
arr = array('i', lst)       # convert back to array
print(arr)          # array('i', [50, 40, 30, 20, 10])
