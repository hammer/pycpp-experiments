from cmath cimport sin

cdef double f(double x):
  return sin(x*x)

def integrate_f(double a, double b, int N):
  cdef int i
  cdef double s, dx
  s = 0
  dx = (b-a)/N
  for i in range(N):
    s += f(a+i*dx)
  return s * dx