# two sum sorted array

arr = [1, 2, 4, 6, 10]
target = 8

left=0
right=len(arr)-1
found=False


while left < right:
    if arr[left]+arr[right]==target:
        print(f"pair found :{arr[left]},{arr[right]}")
        found=True
    
        break
        
    elif arr[left]+arr[right]>target:
        right-=1
        
    else:
        left+=1

if not found:
    print("pair not found")