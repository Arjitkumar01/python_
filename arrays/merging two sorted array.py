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