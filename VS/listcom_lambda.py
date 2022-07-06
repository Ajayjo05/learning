import re

from sqlalchemy import null
s = 'Make the World a *Better Place*'
pattern = r'\*(.*?)\*'
replacement = r'<b>\1<\\b>'
html = re.sub(pattern, replacement, s)

print(html)


string = "at what time?  "
match = re.sub("\s","!!!",string)
print (match)

#enumerate function
g=['milk','sugar','tea']
e=enumerate(g)
for item in e:
    print(list(item))

# g=['milk','sugar','tea']
# e=enumerate(g)
# for item,count in e:
#     print(item,count)


st="an example of split function"
s=st.rsplit()
for word in s:

    if len(word)%2==0:
        print(list(word))

print(st.count('an'))   # to count the number of occurences of a character or word

res=len(st.split())
print("total number of words in string are=",res)


a=[]
for i in range(0,11):
    a.append(i)
print(a)



#list comprehension with if
y=[x for x in range(11) if x%2==0]
print(y)

#list comprehension with if-else
y=[x if x%2==0 else "odd" for x in range(10)]
print(y)

y=[x**2 for x in range(10)]
print(y)


y= list(map(lambda x:x**2,[1,3,5,7]))
print(y)

y=list(filter(lambda x:x%2==0,range(15)))
print(y)


