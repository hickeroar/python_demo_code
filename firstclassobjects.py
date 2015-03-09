from testmod import MyTestModule



def firstClassCall(myClass):
    testm = myClass()
    testm.foo("blahblahblahblah")


firstClassCall(MyTestModule)



def myfunc(astring):
    print astring

def myotherfunc(funcObj):
    funcObj("called from myotherfunc")

myfunc("called from main")
myotherfunc(myfunc)