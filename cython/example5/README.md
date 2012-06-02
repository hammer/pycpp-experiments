To build

    $ python setup.py build_ext --inplace
    

To use

    >>> from integrate import integrate, SinOfSquareFunction
    >>> integrate(SinOfSquareFunction(), 0, 1, 1000000)").timeit(1)


To benchmark

    >>> from timeit import Timer
    >>> Timer("from integrate import integrate, SinOfSquareFunction; integrate(SinOfSquareFunction(), 0, 1, 1000000)").timeit(1)