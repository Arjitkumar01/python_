def rotation(arr,d):
    
    for i in range(0,d):
        
        element= arr.pop(0)
        arr.append(element)
        
    return arr

arr=[1,2,3,4,5]

print(rotation(arr,2))
    
        

        
    
    