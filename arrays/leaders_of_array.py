# leader of array

arr = [5, 10, 20, 15, 8, 3]

answer=[]
max_value=arr[len(arr)-1]
answer.append(max_value)
for i in range(len(arr)-2,-1,-1):
    if max_value < arr[i]:
        answer.append(arr[i])
        max_value=arr[i]
    
print(answer[::-1])