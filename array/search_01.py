# Q1.  Write a function linear_search(arr, target) that returns
#      the INDEX of the target if found, else returns -1.
#      Example:
#        linear_search([10, 30, 20, 50, 40], 20) → 2
#        linear_search([10, 30, 20, 50, 40], 99) → -1

def linear_search(arr,target):
    
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

arr=[10, 30, 20, 50, 40]
target=20
print(linear_search(arr,target))