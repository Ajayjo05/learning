class Student:
    _name = None
    _rno = None
    _branch = None

    def __init__(self, name, rno, branch):
        self._name = name
        self._rno = rno
        self.branch = branch

    def _display(self):
        print("name of student is", self._name)
        print("roll no. of student is", self._rno)
        print("branch of student is", self._branch)


class Sub(Student):
    def __init__(self, name, rno, branch):
        Student.__init__(self, name, rno, branch)

    def displaydetails(self):
        # Accessing protected data member of super class Student
        print("Name is:", self._name)
        print("Roll no. is", self._rno)

        # to access protected method of super class
        #self._display()

obj = Sub("ajay", 101, "IT")
obj.displaydetails()
