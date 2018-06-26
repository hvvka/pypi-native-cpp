#include <Python.h>


static PyObject* factorial(PyObject *self, PyObject* o)
{
    double x = PyFloat_AsDouble(o);
    int number = static_cast<int>(x);
    double result = 1.0;

    for (auto i = 1; i <= number; ++i)
    {
        result *= i;
    }

    return PyFloat_FromDouble(result);
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
    "better_than_python",                   // Module name to use with Python import statements
    "Provides some functions, but faster",  // Module description
    -1,                                     // global
    better_than_python_methods              // Structure that defines the methods of the module
};


PyMODINIT_FUNC PyInit_better_than_python(void) {
    return PyModule_Create(&better_than_python_module);
}
