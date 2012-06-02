# must re-declare sin(1)
cdef extern from "math.h":
  double sin(double)
