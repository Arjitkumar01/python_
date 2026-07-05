class Solution:
    
    def segregateElements(self, arr):
        # code here
        result=[]
        out=0
        for i in range(len(arr)):
            if arr[i] <0:
                out=arr.pop(i)
                result.append(out)
                
            else:
                continue
        return result
    
arr=[1,2,-1,3,-6,4,5,6]
s1=Solution()
s1.segregateElements(arr)
print(s1.segregateElements(arr))
        