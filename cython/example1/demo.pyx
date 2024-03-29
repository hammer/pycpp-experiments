from math import sin

def f(double x):
  return sin(x**2)

def integrate_f(double a, double b, int N):
  s = 0
  dx = (b-a)/N
  for i in range(N):
    s += f(a+i*dx)
  return s * dx