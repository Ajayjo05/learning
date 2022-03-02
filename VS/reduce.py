# reduce() stores the intermediate result and only 
# returns the final summation value. Whereas, 
# accumulate() returns a iterator containing the 
# intermediate results. 
# The last number of the iterator returned is summation
# value of the list.


import functools, operator, itertools

lis=[1,3,5,7,9]
print("sum of list elements is:",end="")
print(functools.reduce(operator.add,lis))

print("Multiplication of list is:",end="")
print(functools.reduce(operator.mul,lis))


# reduce with lambda
print("sum of list elements is:",end="")
print(functools.reduce(lambda a,b:a+b,lis))

print("multiplication of list elements is:",end="")
print(functools.reduce(lambda a,b:a*b,lis))

# accumulate method with lambda

print("sum of list is:",end="")
print(list(itertools.accumulate(lis,lambda a,b:a+b)))

