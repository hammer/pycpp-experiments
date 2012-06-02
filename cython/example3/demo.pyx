from math import sin

# cdef'ed functions are no longer available from Python
# Use cpdef to make the function available to Python as well
cdef double f(double x) except *:
  return sin(x**2)

def integrate_f(double a, double b, int N):
  cdef int i
  cdef double s, dx
  s = 0
  dx = (b-a)/N
  for i in range(N):
    s += f(a+i*dx)
  return s * dx