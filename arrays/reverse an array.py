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