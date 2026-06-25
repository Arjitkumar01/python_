def second_largest(arr):
    largest= -1
    secondLLargest = -1
    
    for i in range(len(arr)):
        if arr[i]> largest:
            largest = arr[i]
            
        
    for i in range(len(arr)):
        if arr[i] >secondLLargest and arr[i] !=largest:
            
            secondLLargest=arr[i]
            
    return f" second largest element: {secondLLargest}"

arr=[10,10]
print(second_largest(arr))
        
        