def my_function1():
    print("hello")

ab=my_function1()
print(ab)

def outer():
    def inner():
        print("i am inner function")
    

    inner()
outer()

def hey(args,**kwargs): #**kwargs values in form of key value pair
    print("i am simple argument=",args)
    for key,value in kwargs.items():
        print((key,value))
hey('hello',first='ajay',mid='kumar',last='joshi')

def heyengineer(*args): # to take multiple arguments through a single parameter
    for val in args:
        print(val)
heyengineer("hello",'i','am','a','software','engineer')