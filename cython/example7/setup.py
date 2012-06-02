from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("cqueue_demo",
                         ["cqueue_demo.pyx"],
                         libraries=["calg"])]

setup(
  name = 'C Dequeue',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
