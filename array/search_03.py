# Q3.  Write a function search_and_print(arr, target) that:
#      - Prints "Found at index X" if target is found
#      - Prints "Not found" if target is not in the array
#      Example:
#        search_and_print([4, 2, 7, 1, 9], 7) → Found at index 2
#        search_and_print([4, 2, 7, 1, 9], 5) → Not found

def search_and_print(arr,target):
    
    for i in range(len(arr)):
        if arr[i]==target:
            return f"Found at index {i}"
    return "Not found"

arr=[4,2,7,1,9]
target=7
print(search_and_print(arr,target))