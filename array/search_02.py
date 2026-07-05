# Q2.  Write a function is_present(arr, target) that returns
#      True if target exists in the array, False otherwise.
#      (Use linear search — do NOT use the 'in' keyword)
#      Example:
#        is_present([5, 3, 8, 1], 3) → True
#        is_present([5, 3, 8, 1], 7) → False

def is_present(arr,target):
    
    for i in arr:
        if i==target:
            return True
    return False

arr=[5,3,8,1]
target=3
print(is_present(arr,target))