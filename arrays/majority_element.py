#    ============================================================= # MAJORITY ELEMENTS================================================================
# using hashing
arr=[1,2,2,3,3,3,3,3,3,3,3,3,3,2,1,2]

frequency = {}
found=False

for num in arr:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num]=1
        

for key in frequency:
    if frequency[key] >len(arr)//2:
        print(f"majority element: {key}")
        found=True
        break
        
if not found:
    print("no majority element:")

# BRUTE FORCE

arr=[1,2,2,1,2]

for i in range(len(arr)):
    count=0
    
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            count+=1
            
    if count>len(arr)//2:
        print(f"majority element:{arr[i]}")
        break
    
else:
    print(f"element not found")


# MOORE'S VOTING ALGO

arr=[2,2,2,2,1,2]

candidate=None
count=0

for num in arr:
    if count == 0:
        candidate= num 
        
    if num == candidate:
        count+=1
    else:
        count-=1
        
print(f"majority element: {candidate}")
