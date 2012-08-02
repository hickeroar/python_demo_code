from grab import Grab

g = Grab()

g.go('http://google.com')

print g.response.body