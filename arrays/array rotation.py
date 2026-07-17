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

