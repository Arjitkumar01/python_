# move all zero to the end

arr=[0,1,0,3,4,5,0,2,0,8]

write=0
for read in range(len(arr)):
    if arr[read]!=0:
        arr[write],arr[read]=arr[read],arr[write]
        write+=1
        
print(arr)