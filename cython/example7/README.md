To build

    $ python setup.py build_ext --inplace


To use

    >>> from cqueue_demo import Queue as Q
    >>> q = Q()
    >>> q.append(1)
    >>> q.peek()
    >>> q.pop()


