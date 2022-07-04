#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
#include <assert.h>

/**
 * print_python_list_info - prints a python list info
 * @p:python list
 * Return: void
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, n;
	PyObject *o;

	n = PyList_Size(p);

	printf("[*] Size of the Python List = %zu\n", n);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < n; i++)
	{
		o = PyList_GetItem(p, i);
		printf("[*] Element %zu: %s\n", i, Py_TYPE(o)->tp_name);
	}


}
