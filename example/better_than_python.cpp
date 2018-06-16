#include <Python.h>

static PyObject* factorial(PyObject *self, PyObject* o)
{
    double x = PyFloat_AsDouble(o);
    int number = (int) x;
//    double result = (double) count_factorial(number);
    double result = 2.0;
    return PyFloat_FromDouble(result);
}

int count_factorial(int number)
{
    if (number == 1 || number == 2)
    {
        return 1;
    }
    else
    {
        return number * count_factorial(number--);
    }
}

static PyMethodDef better_than_python_methods[] = {
    // The first property is the name exposed to Python, fast_tanh, the second is the C++
    // function name that contains the implementation.
    { "factorial", (PyCFunction)factorial, METH_O, nullptr },

    // Terminate the array with an object containing nulls.
    { NULL, NULL, 0, NULL }
};

static struct PyModuleDef better_than_python_module = {
    PyModuleDef_HEAD_INIT,
    "better_than_python",                        // Module name to use with Python import statements
    "Provides some functions, but faster",  // Module description
    -1,  /// global
    better_than_python_methods                   // Structure that defines the methods of the module
};

PyMODINIT_FUNC PyInit_better_than_python(void) {
    return PyModule_Create(&better_than_python_module);
}
