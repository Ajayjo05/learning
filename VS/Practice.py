import functools, operator
d=[1,3,5,7,9]

print("sum is",functools.reduce(lambda a,b:a+b,d))
print("multiplication is",functools.reduce(lambda a,b:a*b,d))

breakpoint()
dt={'k1':'ajay','k2':'john'}
dt['k3']=input("enter the name")
dt['k4']=int(input("enter rno"))

breakpoint()

print(dt)
