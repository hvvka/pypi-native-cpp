import setuptools

spam = setuptools.Extension('better_than_python', sources=['better_than_python.cpp'])

if __name__ == '__main__':
    setuptools.setup(
        name='Spam',
        version='1.0',
        ext_modules=[spam],
    )
