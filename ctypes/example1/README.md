To build the shared library on Mac OS X:

    $ gcc -shared -Wl,-install_name,hello.so -o hello.so -fPIC hello.c


To use:

    >>> import ctypes
    >>> hello = ctypes.CDLL('hello.so')
    >>> hello.myprint()
