from functools import reduce

number=[1,2,3,4,5,6]

result = reduce(lambda x,y: x+y,number)
print(result)




numbers = [5, 8, 2, 10, 3]

largest = reduce(lambda x, y: x if x > y else y, numbers)

print(largest)

        