def plusone(arr):
    num=0  
    for i in arr:
        num=num *10 + i      
    num+=1
    return num
arr=[9,9,9]

print(plusone(arr))
