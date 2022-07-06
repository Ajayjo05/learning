def inc(x):
    return x+1
    

def dec(x):
    return x-1
    

def start(func, x):
    result=func(x)
    return result


start(inc, 4)

start(dec, 5)