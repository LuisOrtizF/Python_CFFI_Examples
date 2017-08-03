from cffi import FFI

ffi = FFI()

ffi.cdef("""int factorial(int n);""")

ffi.set_source("liv", 
  r""" #include <stdio.h>
	int factorial(int n) {
       printf("Print on C \n n=%i \n", n);
       return (n > 1) ? (n * factorial(n - 1)) : 1;
    }
  """, libraries=[])

ffi.compile(verbose=True)