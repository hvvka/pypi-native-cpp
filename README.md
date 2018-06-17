# pypi-native-cpp


0. Host package

* SimpleHTTPServer

   ```bash
   $ python -m http.server
   $ cd dist
   $ pip install http://127.0.0.1:8000/lab13-0.0.1.tar.gz
   ```

* pypiserver

   ```bash
   $ pip install pypiserver
   $ pypi-server -p 8080 ./dist
   $ pip search --index http://localhost:8080 lab13
   $ pip install http://localhost:8080/lab13
   ```

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

* compile and add library
   
   ```bash
   $ cd example
   $ python setup.py build
   $ python setup.py install
   ```
   
3. Compile to binary distribution

```bash
$ pip install pyinstaller 
$ cd example
$ pyinstaller -F functions.py
```
   
   
[1]: http://docs.python-guide.org/en/latest/shipping/packaging/  "PyPi server"
