# this used to filter anything from a list like doing some comparision
# we have to typecast it to list to get the output otherwise it gives  the address of filter

numbers=[1,2,3,4,5,6,7,8,9,10]

result=filter(lambda x: x%2==0,numbers)

print(list(result))
