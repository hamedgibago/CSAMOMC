from setuptools import setup
from Cython.Build import cythonize

setup(
    #ext_modules=cythonize("BatAlgorithm.pyx"),
    #ext_modules=cythonize("run.pyx"),
    ext_modules = cythonize(["*.pyx"]),
    packages=['matplotlib.pyplot','numpy'],
    #package_dir={"": "..//Lib//site-packages"}
)
