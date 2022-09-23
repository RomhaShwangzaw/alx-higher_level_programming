#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: A Python object, whose info is to be listed.
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
	int len, alloc, i;
	PyObject obj;

	len = PyList_Size(p);
	alloc = p->allocated;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < len; i++)
	{
		obj = PyList_getItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
