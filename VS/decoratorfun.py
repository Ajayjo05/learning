#decorator function
def decorator_list(fun):
    def inner(list_of_tuple):
        return [fun (val[0],val[1]) for val in list_of_tuple ]
    return inner


@decorator_list   # decorator implementation
def add_together(a,b): #original function which uses concept of decorator
    return a+b

print(add_together([(1,3),(5,6),(7,8)]))

@decorator_list
def mul(a,b):
    return a*b
print(mul([(1,3),(5,6),(7,9)]))

@decorator_list
def div(a,b):
    return a/b
print(div([(6,2),(9,3),(63,7)]))