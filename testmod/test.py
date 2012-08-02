from testmod import MyTestModule

class ChildTestModule(MyTestModule):

    def bar(self, theString):
        return "Super String: " + theString
