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


        

    







        





    










    
    

    





    



arr=[2,3,4,2,2,2,2,2,2,2]
candidate=None
count=0

for num in arr:
    if count==0:
        candidate=num
    if num == candidate:
        count+=1
    else:
        count-=1
        
print("majority element: {candidate}")


        



    
#  product of array except self

# arr=[1,2,3,4]

# prefix=[0]*len(arr)

# prefix[0]=arr[0]

# for i in range(1,len(arr)):
#     prefix[i]=prefix[i-1] * arr[i]
    
# for i in range(len(arr)):
    
    
# sort colors:
arr=[1,0,2,1,0,2]
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
        
        
index=0
for color in [0,1,2]:
    if color in freq:
        for i in range(freq[color]):
            arr[index]=color
            index+=1

print(arr)
            
print(freq)
