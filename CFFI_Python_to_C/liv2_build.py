from cffi import FFI

ffi = FFI()

ffi.embedding_api("""
	int factorial(int n);
""")

ffi.embedding_init_code("""
	from liv2 import ffi
	@ffi.def_extern()
	def factorial(n):
		if n == 0:
			return 1
		else:
			return n * factorial(n-1)
""")

ffi.set_source("liv2", "")

ffi.compile()
