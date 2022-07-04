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
	Py_ssize_t i, n;
	PyListObject *o = (PyListObject *)p;

	n = o->ob_base.ob_size;
	if (n >= 0)
	{
		printf("[*] Size of the Python List = %zu\n", n);
		printf("[*] Allocated = %li\n", o->allocated);

		for (i = 0; i < n; i++)
		{
			printf("[*] Element %zu: %s\n", i, Py_TYPE(o->ob_item[i])->tp_name);
		}
	}
}
