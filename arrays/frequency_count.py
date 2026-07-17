# FREQUENCY COUNT
# 1-WITHOUT USING DICTIONARY

arr=[1,2,3,2,4,2,3,1,2]
target =2
count = 0
for i in arr:
    if i == target:
        count +=1

print(count)




# 2-NESTED LOOPS
arr=[1,2,3,2,4,2,3,1,2]
visited =[]

for i in range(len(arr)):
    if arr[i] in visited:
        continue
    count=0
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            count +=1
        
    print(f"{arr[i]} --> {count}")
    visited.append(arr[i])


# 3-USING A DICTIONARY
arr=[1,2,3,2,4,2,3,1,2]
freq={}

for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
        
for key,value in freq.items():
    print(f"{key}-->{value}")
        


# 4- DICTIONARY USING .GET()

# arr=[1,2,3,2,4,2,3,1,2]
# freq={}

# for num in arr:
#     freq[num]=freq.get(num,0)+1
    
# for key,value in freq.items():
#     print(f"{key}-->{value}")
        