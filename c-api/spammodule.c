#include <Python.h>

// Implements the module "spam", which has one function, "system".


// Module method implementations
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
  const char *command;
  int sts;

  if (!PyArg_ParseTuple(args, "s", &command))
    return NULL;
  sts = system(command);
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
