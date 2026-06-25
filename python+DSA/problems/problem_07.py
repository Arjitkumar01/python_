def maxConsecBits(arr):
    maxCount, count = 0, 1
    for i in range(1, len(arr)):
    
        if arr[i] == arr[i - 1]:
            count += 1
        
        else:
            maxCount = max(maxCount, count)
            count = 1

    return max(maxCount, count)

arr=[1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1]

print(maxConsecBits(arr))