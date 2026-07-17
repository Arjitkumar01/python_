#========================================================== Trapping rain water problem===========================================================


# BRUTE FORCE APPROCH 

  

# height = [3, 0, 2, 0, 4]
# height = [2, 0, 2]
# height = [3, 0, 1, 3]
height = [4, 2, 0, 3, 2, 5]

trapped_water=0
water=0

for i in range(len(height)):
    
    left_max=height[i]
    for j in range(i):
        if height[j]>left_max:
            left_max=height[j]
        
    
    right_max=height[i]
    for k in range(i+1,len(height)):
        if height[k]>right_max:
            right_max=height[k]
            
            
    water=min(left_max,right_max)-height[i]
    
    trapped_water+=water
    
print(f"water trapped:{trapped_water}")
        
    

# PREFFIX ARRAYS APPROCH

height = [4, 2, 0, 3, 2, 5]
trapped_water=0


left_max=[0]*len(height)
right_max=[0]*len(height)

left_max[0]=height[0]
for i in range(1,len(height)):
    # if left_max[i]<height[i+1]:
    #     left_max[i+1]=height[i+1]
    # else:
    #     left_max[i+1]=left_max[i]
    left_max[i]=max(left_max[i-1],height[i])
        
right_max[len(height)-1]=height[len(height)-1]
for j in range(len(height)-2,-1,-1):
    # if right_max[j]<height[j-1]:
    #     right_max[j-1]=height[j-1]
    # else:
    #     right_max[j-1]=right_max[j]
    right_max[j]=max(right_max[j+1],height[j])
        
for k in range(len(height)):
    water=min(left_max[k],right_max[k])-height[k]
    
    trapped_water+=water
print(f"trapped water :{trapped_water}")


# two pointer approch

        

height = [4, 2, 0, 3, 2, 5]
trapped_water=0

left=0
right=len(height)-1

left_max=0
right_max=0

while left<right:
    
    if height[left]<=height[right]:
        left_max=max(left_max,height[left])
        trapped_water+=left_max-height[left]
        left+=1
        
        
    else:
        right_max=max(right_max,height[right])
        trapped_water+=right_max -height[right]
        right-=1
            
        
print(trapped_water)