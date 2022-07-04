#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - prints a python list info
 * @p:python list
 * Return: void
*/
void print_python_list_info(PyObject *p)
{
	long int i, n;
	PyObject *o;

	n = PyList_Size(p);

	printf("[*] Size of the Python List = %li\n", n);
	printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < n; i++)
	{
		o = PyList_GetItem(p, i);
		printf("[*] Element %li: %s\n", i, Py_TYPE(o)->tp_name);
	}


}
