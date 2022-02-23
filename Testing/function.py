def fun(name, age):
    # we need to convert "int" into str
    print("my name is "+name+" and my age is "+str(age))
    #if we use "," it means just print out what is written
    print("my name is ", name, " and my age is ", age)
fun("ajay", 28)

def print_name(*people):
    for person in people:
        print("Name of this person is", person)
        print(type(people))
print_name("aj", "pj", "jack", "gd")

def math(num1, num2):
    return num1 + num2
r1=math(5,2)
r2=math(56,45)
print("result of r1 is", r1, "result of r2 is ", r2)