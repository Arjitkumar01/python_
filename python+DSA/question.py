# def find_occurrence(arr,target):
#     result=[]
    
#     for i in range(len(arr)):
#         if arr[i] == target:
#             result.append(i)
#     return result


# arr = [5, 3, 7, 3, 9, 3, 1]

# target=3
# print(find_occurrence(arr,target))
        
        

arr = [4, 2, 4, 4, 1, 7, 4, 9]
target = 4

def count_occurence(arr,target):
    
    count=0
    for i in range(len(arr)):
        if arr[i]==target:
            count+=1
        
    return count 
print(count_occurence(arr,target))


def segregateElements(self, arr):
        # code here
        result=[]
        for i in range(len(arr)):
            if arr[i] < 0:
                result.append(i)
                arr.remove(i)
                
        return arr.extend(result)

arr=[1,2,-1,3,-6,4,5,6]

print(segregateElements(arr))
        