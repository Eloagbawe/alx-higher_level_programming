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
#include </usr/include/python3.8/object.h>
#include </usr/include/python3.8/listobject.h>
*/
/**
 * print_python_list_info - prints a python list info
 * @p - python list
 * Return: void
*/
void print_python_list_info(PyObject *p)
{
	long int len = PyList_Size(p);

	printf(len);
	/**
	 * printf(Py_SIZE(p))
	*/
}
