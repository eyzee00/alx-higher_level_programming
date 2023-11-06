#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - gets info about python lists and prints them
 * @p: Reference of a Python object struct
 * Return: (void)
 */
void print_python_list_info(PyObject *p)
{
	int counter = 0;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	while (counter < Py_SIZE(p))
	{
		printf("Element %d: %s\n", counter, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		i++;
	}
}
