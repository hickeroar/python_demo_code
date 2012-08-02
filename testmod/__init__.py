
class MyTestModule:

    # Explain self keyword!
    def foo(self, myString):
        print self.bar(myString)

    def bar(self, theString):
        return "The String is: " + theString