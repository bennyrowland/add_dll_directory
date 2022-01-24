#include <Python.h>

#include "lib.h"

static PyObject *factorial_ext(PyObject *self, PyObject *args)
{
    unsigned int val = 0;
    if (!PyArg_ParseTuple(args, "I", &val))
        return NULL;

    return PyLong_FromLong(factorial(val));
}

static PyMethodDef sub_methods[] =
{
    {
        "factorial_ext",
        factorial_ext,
        METH_VARARGS,
        "C extension factorial"
    },
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef sub_module_def =
{
    PyModuleDef_HEAD_INIT,
    "_sub",
    "Internal \"_sub\" module",
    -1,
    sub_methods
};

PyMODINIT_FUNC PyInit__sub(void)
{
    return PyModule_Create(&sub_module_def);
}