def third_largest(arr):
    
    if len(arr)<3:
        return -1
    
    first =-1
    first_idx=float('-inf')
    
    for i in range(len(arr)):
        if arr[i]>first:
            first=arr[i]
            first_idx = i
        

    second =-1
    second_idx=float('-inf')
    
    for i in range(len(arr)):
        if i == first_idx:
            continue
        
        if arr[i]>second:
            second = arr[i]
            second_idx =i
            
    third =-1
    third_idx=float('-inf')
    
    for i in range(len(arr)):
        if i == first_idx or i== second_idx:
            continue
        
        if arr[i]>third:
            third = arr[i]
            third_idx =i  
            
    return third

arr=[5,5,5]
print(third_largest(arr))