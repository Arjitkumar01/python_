def maximum_triplet(arr):
    
    n=len(arr)
    
    arr.sort()
    
    return arr[-1] * arr[-2] * arr[-3]

arr=[1,2,3,4,5]

print(maximum_triplet(arr))