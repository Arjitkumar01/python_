# sort colors:
arr=[1,0,2,1,0,2]
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
        
        
index=0
for color in [0,1,2]:
    if color in freq:
        for i in range(freq[color]):
            arr[index]=color
            index+=1

print(arr)
            
print(freq)
