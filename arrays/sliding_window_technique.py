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