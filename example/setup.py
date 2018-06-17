import setuptools

better_than_python = setuptools.Extension('better_than_python', sources=['better_than_python.cpp'])

if __name__ == '__main__':
    setuptools.setup(
        name='better_than_python.cpp',
        version='1.0',
        ext_modules=[better_than_python],
    )
