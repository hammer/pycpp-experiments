#include <Python.h>

// Implements the module "spam", which has one function, "system".


// Module method implementations
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
  const char *command;
  int sts;

  // Parse Python arguments into C variables
  if (!PyArg_ParseTuple(args, "s", &command))
    return NULL;

  // Do some work on the method arguments
  sts = system(command);

  // Build a Python object out of a C variable, and return
  return Py_BuildValue("i", sts);
}


// Method table
static PyMethodDef SpamMethods[] = {
    {"system",  spam_system, METH_VARARGS, "Execute a shell command."}
};


// Module initialization
PyMODINIT_FUNC
initspam(void)
{
  (void) Py_InitModule("spam", SpamMethods);
}
