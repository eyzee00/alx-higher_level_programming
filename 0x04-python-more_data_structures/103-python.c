#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject list object
 * Return: (void)
 */
void print_python_list(PyObject *p)
{
	int size, alloc, i = 0;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	while (i < size)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		i += 1;
	}
}
/**
 * print_python_bytes - prints basic info about Python byte objects
 * @p: PyObject byte object
 * Return: (void)
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i = 0, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %d bytes: ", size);
	while (i < size)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i != (size - 1))
			printf(" ");
		else
			printf("\n");
		i += 1;
	}
}
