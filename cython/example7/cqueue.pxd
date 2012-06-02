cdef extern from "libcalg-1.0/libcalg/queue.h":
  # Opaque handle
  ctypedef struct Queue:
    pass
  ctypedef void* QueueValue

  # Typo in the paper: new_queue()
  Queue* queue_new()
  void queue_free(Queue* queue)

  int queue_push_head(Queue* queue, QueueValue data)
  QueueValue queue_pop_head(Queue* queue)
  QueueValue queue_peek_head(Queue* queue)

  int queue_push_tail(Queue* queue, QueueValue data)
  QueueValue queue_pop_tail(Queue* queue)
  QueueValue queue_peek_tail(Queue* queue)

  # Cython's bint type maps an int in C to a Boolean in Python
  bint queue_is_empty(Queue* queue)
