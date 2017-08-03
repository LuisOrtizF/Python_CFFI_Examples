from cffi import FFI

includes = open('./C_code/liv.h').read()
source = open('./C_code/liv.c').read()

ffibuilder = FFI()
ffibuilder.dlopen('./C_code/liv.so')
ffibuilder.cdef(includes, 'liv3')
ffibuilder.set_source('liv3', source)
ffibuilder.compile()