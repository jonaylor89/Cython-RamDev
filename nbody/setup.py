
from distutils.core import setup
from Cython.Build import cythonize

setup(name="cynbody",
      ext_modules=cythonize("cynbody.pyx"))
