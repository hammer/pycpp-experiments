cimport cqueue
cimport python_exc

cdef class Queue:
  cdef cqueue.Queue *_c_queue

  def __cinit__(self):
    self._c_queue = cqueue.queue_new()
    if self._c_queue is NULL:
      python_exc.PyErr_NoMemory()

  def __dealloc__(self):
    if self._c_queue is not NULL:
      cqueue.queue_free(self._c_queue)
