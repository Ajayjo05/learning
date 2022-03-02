a=list(map(lambda x : x**2, range (11)))
print(a)

b=list(filter(lambda x: x%2==0, range(11)))
print(b)


y=[{'a':5},{'a':4},{'a':8}]
print(y)
print(y[1])

# to print list of dictionary in descending order
print(sorted(y, key = lambda x:x['a'],reverse =True ))


# to print list of dictionary in ascending order
print(sorted(y, key = lambda x:x['a']))

d={'k1':45,'k2':36,'k3':57}
print(sorted(d.values()))  #to print sorted values 
if 'k1' in d: #to check the key exist in dictionary
    print("yes k1 exists in dictionary")

d['k4']=78
print(d)
d.popitem()     #to pop the last item from the dictionary
print(d)
