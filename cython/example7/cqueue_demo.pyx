cimport cqueue
cimport cpython.exc # python_exc is deprecated

cdef class Queue:
  # Typo in the paper: not a pointer (fixed in complete listing)
  cdef cqueue.Queue* _c_queue

  def __cinit__(self):
    self._c_queue = cqueue.queue_new()
    if self._c_queue is NULL:
      cpython.exc.PyErr_NoMemory()

  def __dealloc__(self):
    if self._c_queue is not NULL:
      cqueue.queue_free(self._c_queue)

  # emptiness indicator
  def __nonzero__(self):
    return not cqueue.queue_is_empty(self._c_queue)

  #
  # methods for adding values to the queue
  #
  cpdef append(self, int value):
    if not cqueue.queue_push_tail(self._c_queue, <void*>value):
      cpython.exc.PyErr_NoMemory()

  cdef extend(self, int* values, Py_ssize_t count):
    cdef Py_ssize_t i
    for i in range(count):
      if not cqueue.queue_push_tail(self._c_queue, <void*>values[i]):
        cpython.exc.PyErr_NoMemory()

  #
  # methods for removing values from the queue
  #
  cpdef int peek(self) except? 0:
    cdef int value = <int>cqueue.queue_peek_head(self._c_queue)
    if value == 0:
      # this may mean that the queue is empty, or
      # that it happens to contain a 0 value
      if cqueue.queue_is_empty(self._c_queue):
        raise IndexError("Queue is empty")
    return value

  cpdef int pop(self) except? 0:
    cdef int value = <int>cqueue.queue_pop_head(self._c_queue)
    if value == 0:
      # this may mean that the queue is empty, or
      # that it happens to contain a 0 value
      if cqueue.queue_is_empty(self._c_queue):
        raise IndexError("Queue is empty")
    return value

  
