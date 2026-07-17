# max sum of sub arrays :

# BRUTE FORCE:

# arr=[-2,-3,4,-1,-2,1,5,-3]


# maximum=float('-inf')

# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         sum=0
#         for k in range(i,j+1):
#             sum+=arr[k]
#         maximum=max(sum,maximum)
# print(f"maximum no: {maximum}")
            
# small optimisation
arr=[-2,-3,4,-1,-2,1,5,-3]


maximum=float('-inf')

for i in range(len(arr)):
    current_sum=0
    for j in range(i,len(arr)):
        current_sum+=arr[j]
        maximum=max(current_sum,maximum)
print(f"maximum no: {maximum}")

# preffix sum

arr=[-2,-3,4,-1,-2,1,5,-3]
maximum=float('-inf')

prefix=[0]*len(arr)

prefix[0]=arr[0]
current_sum=0

for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
    
for j in range(len(arr)):
    for k in range(j,len(arr)):
        
        if j==0:
            current_sum=prefix[k]
        else:
            current_sum=prefix[k]-prefix[j-1]
            
        maximum=max(current_sum,maximum)
            
    
print(f"maximum : {maximum}")

# kadane's algorithm


arr=[3,-4,5,4,-1,7,-8]

current_sum=0
maximum=float('-inf')

for i in range(len(arr)):
    current_sum+=arr[i]
    maximum=max(maximum,current_sum)
    
    if current_sum<0:
        current_sum=0


print(f"maximum sum:{maximum}")

# to print the subarray


arr=[3,-4,5,4,-1,7,-8]

current_sum=0
maximum=float('-inf')
start=0
ans_start=0
end=0

for i in range(len(arr)):
    current_sum+=arr[i]
    
    if current_sum >maximum:
        maximum=current_sum
        ans_start=start
        end=i
        
    
    if current_sum<0:
        current_sum=0
        start=i+1


print(f"Sub Array:{arr[ans_start:end+1]}")
