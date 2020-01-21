class ParentClass:
    def __int__(Self):
        self.a = 1
        print("Parent Class Object Created")
    def someMethod(self):
        print("Hello")

class ChildClass(ParentClass):
    def __init__(self):
        print("Child Class Object Created")

parent = ParentClass()
child = ChildClass()
