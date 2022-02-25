i=[x for x in range(10)]
print(i)
a = list(map(lambda x: x ** 2, range(10)))
print(a)

b = list(filter(lambda x: x%3==0, range(10)))
print(b)

c=list(map(lambda x : x**3, range(5)))
print(c)

y=[{'a':5},{'a':4},{'a':8}]
print(y)
print(y[1])

# to print list of dictionary in descending order
print(sorted(y, key = lambda x:x['a'],reverse =True ))


# to print list of dictionary in ascending order
print(sorted(y, key = lambda x:x['a']))

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

