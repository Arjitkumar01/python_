# ------------------------------------------------ARRAYS-----------------------------------------------------------------------

# from array import array

# numbers = array('i',[1,2,3,4,5,6])

# new_num = array(numbers.typecode,(a for a in numbers) )

# print(new_num)





# recursion code for printing 1 to n

def print_number(n):
    if n==0:
        return
    
    print_number(n-1)
    print(n)
    
print_number(10)