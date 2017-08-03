from liv3 import ffi, lib

n = 4
result = lib.factorial(n)
print "Print on Python \n %i!=%i" %(n, result)