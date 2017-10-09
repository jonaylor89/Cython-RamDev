
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "fib",
    ext_modules = cythonize('cyfib.pyx')
)
