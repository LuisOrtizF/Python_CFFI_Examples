from cffi import FFI

includes = open('./Py_code/liv.h').read()
source = open('./Py_code/liv.py').read()

ffi = FFI()

ffi.embedding_api(includes)

ffi.set_source('liv4', includes)

ffi.embedding_init_code(source)

ffi.compile()
