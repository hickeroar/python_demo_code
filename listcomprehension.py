mylist = list(xrange(0,11))

for x in [y for y in mylist if y % 2 == 0]:
    print x



"""
Boilerplate:
for x in mylist:
    if y % 2 == 0:
        print x
"""


"""
newList = [y for y in mylist if y % 2 == 0]
print newList
"""