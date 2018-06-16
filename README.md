Lab13 - przygotowanie binarnej dystrybucji

0. Host package with PyPi

1. Wheel package

   * create

   ```bash
   $ python -m pip install --user --upgrade setuptools wheel
   $ pip install wheel
   $ python3 setup.py sdist bdist_wheel
   ```
   
   * use
   
   ```bash
    $ pip install dist/lab13-0.0.1-py3-none-any.whl 
    ```

2. Use C/C++ in pythong

   * 
   
   ```bash
    $ pip install .
    ```
   
   



0. Tutorial m.in. o tym, jak zainstalować własny serwer pypi
http://docs.python-guide.org/en/latest/shipping/packaging/
Opisano w nim:
a) wykorzystanie SimpleHTTPserver do serwowania pakietów przez umieszczenie ich w katalogach
(python2) python -m SimpleHTTPServer 9000
(python3) python -m http.server
potem można już instalować pakiety:
pip install --extra-index-url=http://127.0.0.1:9000/ MyPackage
pip install  http://127.0.0.1:9000/MyPackage.tar.gz
b) wykorzystanie pypiserver jako serwisu pakietów (dodatkowe informacje: https://pypi.org/project/pypiserver/)
Python Package Index (PyPI)
    PyPI is the default Package Index for the Python community. It is open to all Python developers to consume and distribute their distributions.
    
    
    
1. Jeszcze raz tworzenie pakietów do dystrybucji (egg and wheel)
https://packaging.python.org/
https://packaging.python.org/tutorials/packaging-projects/
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://www.digitalocean.com/community/tutorials/how-to-package-and-distribute-python-applications
https://code.tutsplus.com/tutorials/how-to-write-package-and-distribute-a-library-in-python--cms-28693
https://code.tutsplus.com/tutorials/how-to-write-your-own-python-packages--cms-26076
https://packaging.python.org/discussions/wheel-vs-egg/
https://pip.pypa.io/en/latest/user_guide/#installing-from-wheels
https://packaging.python.org/glossary/#term-wheel
Binary Distribution
    A specific kind of Built Distribution that contains compiled extensions.

Built Distribution
    A Distribution format containing files and metadata that only need to be moved to the correct location on the target system, to be installed. Wheel is such a format, whereas distutil’s Source Distribution is not, in that it requires a build step before it can be installed. This format does not imply that Python files have to be precompiled (Wheel intentionally does not include compiled Python files).

Distribution Package
    A versioned archive file that contains Python packages, modules, and other resource files that are used to distribute a Release. The archive file is what an end-user will download from the internet and install.
    A distribution package is more commonly referred to with the single words “package” or “distribution”, but this guide may use the expanded term when more clarity is needed to prevent confusion with an Import Package (which is also commonly called a “package”) or another kind of distribution (e.g. a Linux distribution or the Python language distribution), which are often referred to with the single term “distribution”.
Egg
    A Built Distribution format introduced by setuptools, which is being replaced by Wheel. For details, see The Internal Structure of Python Eggs and Python Eggs
	
Wheel
    A Built Distribution format introduced by PEP 427, which is intended to replace the Egg format. Wheel is currently supported by pip.

Wygenerowanie paczek do dystrybucji:
	python setup.py sdist bdist_wheel
Przy okazji dekompilator: https://docs.python.org/2/_sources/library/dis.rst.txt
Zainstalowanie biblioteki w projekcie:
	pip install ../freezing/dist/pathology-0.2-py3-none-any.whl 
2. Wykorzystanie kodu C/C++ w pythonie (można to robić na różne sposoby)
Instalacja niezbędnych zależności dla kompilatora C/C++
	sudo apt-get install python-dev
	sudo apt-get install python3-dev /// build-essential libssl-dev libffi-dev 
http://intermediate-and-advanced-software-carpentry.readthedocs.io/en/latest/c++-wrapping.html
https://blog.conan.io/2016/04/12/Extending-python-with-C-or-C++-with-pybind11.html
https://docs.python.org/3/extending/extending.html#a-simple-example
Dobre przykłady z książki (moduły ctypes oraz CFFI oraz Native C/C++ extensions)
https://github.com/PacktPublishing/Python-Journey-from-Novice-to-Expert/tree/master/Module%203/14_c_and_cpp_extensions
import ctypes
ctypes.cdll
libc = ctypes.cdll.LoadLibrary('libc.so.6')
libc
libc.printf
cdll.LoadLibrary(util.find_library('libc'))
3. Zamrażanie aplikacji (tworzenie instalatorów, może odbywać się na różne sposoby)
http://docs.python-guide.org/en/latest/shipping/freezing/#freezing-your-code-ref
https://cyrille.rossant.net/create-a-standalone-windows-installer-for-your-python-application/
http://pynsist.readthedocs.io/en/latest/index.html

pip install pyinstaller

pyinstaller -F aaa.py
