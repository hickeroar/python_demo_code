myword = "superword"


def subtractLetter(thestring):
    while thestring:
        # NOTE TO SELF: Explain the [0:-1] syntax
        thestring = thestring[0:-1]
        yield thestring


for astring in subtractLetter(myword):
    print astring

"""
Explain:
range vs xrange!
"""