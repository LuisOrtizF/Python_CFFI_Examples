# CFFI_Examples
These examples show how to use the CFFI Tool for embedding C or Python code.

### Ex1: Convert C code to one shared library (.so) and use this one with Python.
### Ex2: Convert Python code to one Linux shared library (.so) and use this one with C.
* To compile C code, before create (.so) file using 'liv2_build.py' and after(in terminal):
```
$export LD_LIBRARY_PATH=.
$gcc -o test2 test2.c liv2*.so
```
### Ex3: Similar to Ex1 but call external (.h, .c) files.
### Ex4: Similar to Ex2 but call external (.h, .py) files.  

## NOTE:

<p style="background:black">
<code style="background:black;color:red">If you find any of these codes helpful, please share my <a href="https://github.com/LuisOrtizF">GitHub</a> and STAR</code>:star:<code style="background:black;color:red">this repository to help other enthusiasts to find these tools. Remember, the knowledge must be shared. Otherwise, it is useless and lost in time.
</code>
</p>
