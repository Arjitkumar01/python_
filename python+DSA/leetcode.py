# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s = str(x)

#         return s == s[::-1]
        
# num = int(input())

# obj = Solution()
# print(obj.isPalindrome(num))


# class Solution:
#     def addDigits(self, num: int) -> int:
#         if num == 0:
#             return 0
#         while num >= 10:
#             num = sum(int(digit) for digit in str(num))
#         return num
            
# num = int(input())

# obj = Solution()
# print(obj.addDigits(num))



# def swap_case(s):
#     result=""
    
#     for ch in s:
#         if ch.islower():
#             result+=ch.upper()
#         elif ch.isupper():
#             result+=ch.lower()
#         else:
#             result += ch
            
    
#     return result

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)

A = []
n=int(input())

for i in range(n):
    to_add=int(input())
    A.append(to_add)
    
print(A) 
A.sort()
new_list=set(A)
print(new_list)
final =list(new_list)
print(final[-2])



