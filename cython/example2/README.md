To build

    $ python setup.py build_ext --inplace
    

To use

    >>> from demo import integrate_f
    >>> integrate_f(0, 1, 10000)


To benchmark

    >>> from timeit import Timer
    >>> Timer("from demo import integrate_f; integrate_f(0, 1, 1000000)").timeit(1)
