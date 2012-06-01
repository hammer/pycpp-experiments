from distutils.core import setup, Extension

noddy = Extension("noddy", ["noddytype.c"])

setup(name="noddy",
      version="1.0",
      ext_modules=[noddy])
