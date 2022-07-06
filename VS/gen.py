


#d=list(range(10))
'''from re import M


def myfunction():
    yield 1 
    yield 2
    yield 3

x=myfunction() 
#for value in x:
print(x.__next__())
print(x.__next__())
print(x.__next__())
'''

txt = "welcome,to,the,jungle"

x= txt.split(",")
if len(x)%2==0:
    print(x)


def fun1():
    print("hello")

fun2=fun1

fun2()
