
class MyClass:

    _protectedProp = "flop"

    __privateProp = "foo"

    def __privateMethod(self):
        return "bar"

    def getPrivateMethodData(self):
        return self.__privateMethod()

    def getPrivateProperty(self):
        return self.__privateProp


myobj = MyClass()

print myobj._protectedProp

print myobj._MyClass__privateProp
print myobj._MyClass__privateMethod()

print myobj.getPrivateProperty()
print myobj.getPrivateMethodData()