# PREFIX SUM 
# normal approch 
arr=[1,2,3,4,5,6]

left=1
right = 3
total=0

for i in range(left,right+1):
    total+=arr[i]
    
print(f"total :{total}")

# preffix sum idea:

arr=[1,2,3,4,5,6]

prefix=[0]* len(arr)

prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1] + arr[i]
    
left =1
right=3

if left==0:
    total=prefix[right]
else:
    total=prefix[right] - prefix[left-1]
    
print(f"preffixed array :{prefix}")
print(f"total : {total}")
