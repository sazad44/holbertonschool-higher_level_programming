#include <Python.h>
#include <sys/types.h>
#include <pyport.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints info about python lists
 * @p: a pointer to a python object
 * Return: No Value
 */
void print_python_list_info(PyObject *p)
{
	int psize = (int)PyList_Size(p), i = 0;
	int all = (int)(((PyListObject *)(p))->allocated);
	PyObject *ptype = NULL;

	printf("[*] Size of the Python List = %d\n", psize);
	printf("[*] Allocated = %d\n", all);
	for (i = 0; i < psize; i++)
	{
		ptype = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, (char *)Py_TYPE(ptype)->tp_name);
	}
}
