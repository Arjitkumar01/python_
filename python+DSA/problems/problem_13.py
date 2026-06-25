def leaders(arr):
    result = []
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                break
        else:
            result.append(arr[i])
    
    return result

arr=[1,2,3,4,5,2]
print(leaders(arr))