# PAIR SUM

arr=[2,7,11,15]
target=18

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]== target:
            print(f"pair found:{arr[i]},{arr[j]}")
        

# optimal approch:

arr=[2,7,11,15]
target=18

left=0
right=len(arr)-1

while left<right:
    if arr[left]+arr[right]==target:
        print(f"pair found:{arr[left]},{arr[right]}")
        break
    
    elif arr[left] +arr[right] > target:
        right-=1
    else:
        left +=1
else:
    print(f"pair not found")