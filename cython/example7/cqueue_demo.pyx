cimport cqueue
cimport cpython.exc # python_exc is deprecated

cdef class Queue:
  # Typo in the paper: not a pointer
  cdef cqueue.Queue *_c_queue

  def __cinit__(self):
    self._c_queue = cqueue.queue_new()
    if self._c_queue is NULL:
      cpython.exc.PyErr_NoMemory()

  def __dealloc__(self):
    if self._c_queue is not NULL:
      cqueue.queue_free(self._c_queue)

  cdef append(self, int value):
    cqueue.queue_push_tail(self._c_queue, <void*>value)
    cpython.exc.PyErr_NoMemory()
