# Decorator function to print list in form of dictionary
def abc(fun):
    def inner(lst):
        dicti=  {lst[i]:lst[i+1] for i in range(0,len(lst),2)}
        return dicti
        
    return inner

@abc
def xyz():
    return xyz

print(xyz(['a',1,'b',2,'c',3,'d',4]))

#######################################################################################
#Second code
def ori(func):
    def inner1():
        print("i am original function")
        func()
    return inner1

@ori
def using():
    print("i am using original function")

using()

######################################################################################
#third code
arr= ['a','b','c','d']
def deco(fun1):
    def newValue(pos):
        if pos >= len(arr):
            print("index out of range")
        fun1(pos)
    return newValue

@deco
def Value(index):
    print(arr[index])

Value(2)











