def zero_at_the_end(arr):
     
    n=len(arr)
    k=0
    for i in range(n):
        if arr[i]!=0:
            arr[i],arr[k]=arr[k],arr[i]
            k+=1
    return arr


arr=[1,0,2,3,0,4]

print(zero_at_the_end(arr))