class Student:
    __name = None
    __roll = None
    __branch = None

    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    def __display(self):
        print("name of student is:", self.__name)
        print("roll no of student is:", self.__roll)
        print("branch of student is:", self.__branch)

    # private method and variable can be accessed within the class only not outside.
    def accessPrivateFunction(self):  # Way to access private method.
        self.__display()


class Sub(Student):
    def __init__(self, name, roll, branch):
        Sub.__init__(self, name, roll, branch)

    def displaydetails(self):
        print("name is:", self.__name)
        print("roll no is:", self.__roll)


# object of sub class
# s1 = Sub("ajay", 111, "CS")
# s1.displaydetails()
# object of super class
s2 = Student("ajay", 111, "CS")
s2.accessPrivateFunction()
