/* Adapted from: https://docs.python.org/3.7/extending/embedding.html#very-high-level-embedding
 *
 * Simply `eval` a Python string in C, don't communicate any values between the two. Not very exciting.
 */

#include <assert.h>

#define PY_SSIZE_T_CLEAN
#include <Python.h>

/* https://stackoverflow.com/questions/12348433/how-to-check-the-version-of-the-python-api-at-compile-time-from-a-c-extension-mo */
#if PY_MAJOR_VERSION == 2

int main(int argc, char *argv[]) {
    assert(argc > 1);
    Py_SetProgramName(argv[0]);  /* optional but recommended */
    Py_Initialize();
    PyRun_SimpleString(argv[1]);
    Py_Finalize();
    return 0;
}

#else

int main(int argc, char *argv[]) {
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    assert(program != NULL);
    assert(argc > 1);
    Py_SetProgramName(program);  /* optional but recommended */
    Py_Initialize();
    PyRun_SimpleString(argv[1]);
    assert(Py_FinalizeEx() >= 0);
    PyMem_RawFree(program);
    return 0;
}

#endif
