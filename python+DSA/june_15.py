# Linear search:

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr=[1,2,3,4,5,11,7,8,9,10,6]
print(linear_search(arr, 11))


# Binary Search:  Array must be sorted

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]

print(binary_search(arr, 15))


# Bubble sort   swapp the number if they are not in order

arr = [5, 2, 8, 1]

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)


# Selection sort    finds the smallest and place it at the beginning

arr = [5, 2, 8, 1]

for i in range(len(arr)):
    min_idx = i

    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)


# insertion sort

arr = [5, 2, 8, 1]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print(arr)
