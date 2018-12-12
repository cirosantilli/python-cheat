/* Adapted from: https://docs.python.org/3.7/extending/embedding.html#very-high-level-embedding
 *
 * Simply `eval` a Python string in C, don't communicate any values between the two. Not very exciting.
 */

#include <Python.h>

int
main(int argc, char *argv[])
{
  Py_SetProgramName(argv[0]);  /* optional but recommended */
  Py_Initialize();
  PyRun_SimpleString(argv[1]);
  Py_Finalize();
  return 0;
}
