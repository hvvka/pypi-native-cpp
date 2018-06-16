from setuptools import setup, find_packages
from os import path
from distutils.core import setup, Extension, DEBUG

here = path.abspath(path.dirname(__file__))
sfc_module = Extension('better_than_python', sources=['example/better_than_python.cpp'])

setup(
    name='lab13',
    version='0.0.1',
    description='lab13',
    long_description=open('README.md').read(),
    url='https://github.com/hvvka/',
    author='Hanna',
    author_email='226154@student.pwr.edu.pl',
    packages=find_packages(exclude=['test*']),
    ext_modules=[sfc_module]
)
