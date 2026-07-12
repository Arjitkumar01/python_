# SEARCHING 
# 1-LINEAR SEARCH
# 2-BINARY SEARCH

# FIND MAX & MIN IN ARRAY

# REVERSE A ARRAY
# 1-USING EXTRA ARRAY
# 2-TWO POINTER

# FREQUENCY COUNT
# 1-WITHOUT USING DICTIONARY
# 2-NESTED LOOPS
# 3-USING A DICTIONARY
# 4- DICTIONARY USING .GET()

# ARRAY ROTATION
# 1-USING EXTRA VARIABLE
# 2- ROTATION BY K 

# PREFIX SUM 

# 1 linear search

# arr = [1,3,9,5,7,2]

# target=4

# for i in range(len(arr)):
    
        
#     if arr[i] == target:
#         print("element found at index : ",i)
#         break
        
# if arr[i] != target:
#         print("element not found ")
        
        
        
        
# binary search 

# arr = [1, 3, 5, 7, 9, 11, 13, 15]

# left =0
# right =len(arr)-1
# target = 9

# while left <= right:
#     mid = (left+right)//2
    
#     if arr[mid] == target:
#         print("index : ",mid)
#         break
#     elif target < arr[mid]:
#         right= mid-1
#     else:
#         left = mid +1
        
        
# max and min 
# using builtin function 

# arr=[1,2,4,6,8,9,7,4,3,3,5]

# print(max(arr))
# print(min(arr))

# without using builtin function


# arr=[1,2,4,6,8,9,7,4,3,3,5]

# maximum=arr[0]
# minimum=arr[0]

# for i in arr:
#     if maximum < i:
#         maximum =i
    
#     if minimum > i:
#         minimum = i 
        
# print("max :",maximum)
# print("min :",minimum)
    
# REVERSE A ARRAY
# 1-USING EXTRA ARRAY

# arr=[1,2,3,4,5,6]

# new_arr=[]

# for i in range(len(arr)-1,-1,-1):
#     a=arr[i]
#     new_arr.append(a)
    
# print("reversed array:",new_arr)


# 2-TWO POINTER

# arr=[1,2,3,4,5,6]

# left=0
# right=len(arr)-1

# while left <right :
#     arr[left],arr[right]=arr[right],arr[left]
    
#     left +=1
#     right -=1
    
# print("reversed arr : ",arr)


# FREQUENCY COUNT
# 1-WITHOUT USING DICTIONARY

# arr=[1,2,3,2,4,2,3,1,2]
# target =2
# count = 0
# for i in arr:
#     if i == target:
#         count +=1

# print(count)




# 2-NESTED LOOPS
# arr=[1,2,3,2,4,2,3,1,2]
# visited =[]

# for i in range(len(arr)):
#     if arr[i] in visited:
#         continue
#     count=0
#     for j in range(len(arr)):
#         if arr[i]==arr[j]:
#             count +=1
        
#     print(f"{arr[i]} --> {count}")
#     visited.append(arr[i])


# 3-USING A DICTIONARY
# arr=[1,2,3,2,4,2,3,1,2]
# freq={}

# for num in arr:
#     if num in freq:
#         freq[num]+=1
#     else:
#         freq[num]=1
        
# for key,value in freq.items():
#     print(f"{key}-->{value}")
        


# 4- DICTIONARY USING .GET()

# arr=[1,2,3,2,4,2,3,1,2]
# freq={}

# for num in arr:
#     freq[num]=freq.get(num,0)+1
    
# for key,value in freq.items():
#     print(f"{key}-->{value}")
        


# ARRAY ROTATION
# 1-USING EXTRA VARIABLE

# arr=[1,2,3,4,5]

# first=arr[0]

# for i in range(0,len(arr)-1):
#     arr[i]=arr[i+1]

# arr[len(arr)-1]=first

# print(f"final array :{arr}")




# arr=[1,2,3,4,5]

# last=arr[-1]

# for i in range(len(arr)-1,-1,-1):
#     arr[i]=arr[i-1]

# arr[0]=last

# print(f"final array :{arr}")





# 2- ROTATION BY K 



# arr=[1,2,3,4,5]

# k=2
# n=len(arr)

# k= k%n

# for i in range(k):
#     first = arr[0]
#     for j in range(n-1):
#         arr[j]=arr[j+1]
#     arr[n-1]=first
# print(f"final array :{arr}")

# arr=[1,2,3,4,5]

# k=2
# n=len(arr)

# k= k%n

# for i in range(k):
#     last = arr[n-1]
#     for j in range(n-1,0,-1):
#         arr[j]=arr[j-1]
#     arr[0]=last
# print(f"final array :{arr}")


        


# PREFIX SUM 
# normal approch 
# arr=[1,2,3,4,5,6]

# left=1
# right = 3
# total=0

# for i in range(left,right+1):
#     total+=arr[i]
    
# print(f"total :{total}")

# preffix sum idea:

# arr=[1,2,3,4,5,6]

# prefix=[0]* len(arr)

# prefix[0]=arr[0]
# for i in range(1,len(arr)):
#     prefix[i]=prefix[i-1] + arr[i]
    
# left =1
# right=3

# if left==0:
#     total=prefix[right]
# else:
#     total=prefix[right] - prefix[left-1]
    
# print(f"preffixed array :{prefix}")
# print(f"total : {total}")


# SLIDING WINDOW TECHNIQUE:

# arr=[1,2,3,4,5,6,7,8]

# k=3
# temp_sum=0
# for i in range(k):
#     temp_sum+=arr[i]
    
# maximum=temp_sum
# for j in range(k,len(arr)):
#     temp_sum=temp_sum -arr[j-k]+arr[j]
    
#     if temp_sum>maximum:
#         maximum=temp_sum
        
# print(f"maximum xum : {maximum}")
    


# merging two sorted array

arr1=[1,2,3,4]
arr2=[5,6,7,8]

result=[]
i,j=0,0
while i < len(arr1) and j < len(arr2):
    if arr1[i]==arr2[j]:
        result.append(arr1[i])
        result.append(arr2[j])
        i=i+1
        j=j+1
    elif arr1[i]<arr2[j]:
        result.append(arr1[i])
        i=i+1
    else:
        result.append(arr2[j])
        j=j+1
        
while i <len(arr1):
    result.append(arr1[i])
    i+=1
 
while j <len(arr2):
    result.append(arr2[j])
    j+=1   
        
print(result)

# standard case:
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]

result = []

i = 0
j = 0

while i < len(arr1) and j < len(arr2):

    if arr1[i] <= arr2[j]:
        result.append(arr1[i])
        i += 1
    else:
        result.append(arr2[j])
        j += 1

while i < len(arr1):
    result.append(arr1[i])
    i += 1

while j < len(arr2):
    result.append(arr2[j])
    j += 1

print(result)


# remove duplicate elements (two pointer technique)

arr=[1,1,2,2,3,4,4,5]

write =0

for read in range(1,len(arr)):
    if arr[read]!=arr[write]:
        write+=1
        arr[write]=arr[read]
        
print(arr)

# move all zero to the end

arr=[0,1,0,3,4,5,0,2,0,8]

write=0
for read in range(len(arr)):
    if arr[read]!=0:
        arr[write],arr[read]=arr[read],arr[write]
        write+=1
        
print(arr)

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
    


        
    
    
        
        
        
