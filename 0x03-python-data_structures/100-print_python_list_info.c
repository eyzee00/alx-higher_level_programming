#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - prints infor about python lists
 * @p: the python list we want info about
 * Return; (void)
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = 0, allocated_space = 0, counter = 0;
	PyObject *item = NULL;

	size = PyList_Size(p);
	allocated_space = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated_space);
	while (counter < size)
	{
		item = PyList_GET_ITEM(p, counter);
		printf("Element %ld: %s\n", counter, item->ob_type->tp_name);
		counter = counter + 1;
	}
}
