#!/usr/bin/python3 -u

import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_bytes.argtypes = [ctypes.py_object]
s = b"Hello"
lib.print_python_bytes(s);
