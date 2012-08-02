import testmod
from testmod.test import ChildTestModule

testm = testmod.MyTestModule()
testm.foo("blahblahblah")

childtestm = ChildTestModule()
childtestm.foo("blahblah")



from testmod import MyTestModule

testm = MyTestModule()
testm.foo("blahblahblahblah")