# container with most water

height= [1,8,6,2,5,4,8,3,7]
max_water=0

for i in range(len(height)):
    for j in range(i+1,len(height)):
        ht=0
        wt=j-i
        # if height[i]<=height[j]:
        #     ht=height[i]
        # else:
        #     ht=height[j]
        ht = min(height[i], height[j])
        
        current_water= ht *wt
        
        if max_water<current_water:
            max_water=current_water
            
print(max_water)


# optimised method

height= [1,8,6,2,5,4,8,3,7]
max_water=0
left =0
right=len(height)-1

while left <right:
    wt =right-left
    ht=min(height[left],height[right])
    current_water=ht*wt
    if current_water>max_water:
        max_water=current_water
    
    if height[left]<height[right]:
        left+=1
    else:
        right-=1
        
print(f"answer:{max_water}")