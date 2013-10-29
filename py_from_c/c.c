#include <Python.h>
/*
this already includes:

- <stdio.h>
- <string.h>
- <errno.h>, and <stdlib.h>
*/

static PyObject * c_plus( PyObject *self, PyObject *args )
{
    const char *command;
    int sts;

    if( !PyArg_ParseTuple(args, "s", &command ) )
        return NULL;
    sts = system(command);
    return Py_BuildValue("i", sts);
}
