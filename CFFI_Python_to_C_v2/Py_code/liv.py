from liv4 import ffi
@ffi.def_extern()
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)