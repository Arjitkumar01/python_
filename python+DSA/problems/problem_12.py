def rearrange(arr):
    pos=[]
    neg=[]
    
    for i in arr:
        if i >0:
            pos.append(i)
        else:
            neg.append(i)
    
    result=[]
    for i in range(len(pos)):
        result.append(pos[i])
        result.append(neg[i])
        
    return result

arr=[1,2,3,-1,-2,-3]
print(rearrange(arr))
        