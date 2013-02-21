import math

x = 2
y = 3
n = 1
a = math.cos(3 * (x - n)) + \
    math.sin(3 * (y - n))
a = 3 + 4j
r = a.real
b = [1, 2, 3,]
def compare(a, b):
    if a is b:
        print "a and b are the same object"
    if a == b:
        print "a and b have the same value"
    if type(a) == type(b):
        print "a and b have the same type"

compare(a,a)
            
