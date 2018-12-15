#include <Python.h>
#include <sys/types.h>
#include <pyport.h>
#include <object.h>
#include <listobject.h>
PyObject *ptype = NULL;
int plsize = 0, i = 0;

/**
 * print_python_list_info - prints info about python lists
 * @p: a pointer to a python object
 * Return: No Value
 */
void print_python_list_info(PyObject *p)
{
	int psize = (int)PyList_Size(p);
	PyObject *tmptype = NULL;

	if (psize)
		tmptype = PyList_GetItem(p, 0);
	if ((tmptype != ptype) || (psize > plsize))
		plsize = psize;
	printf("[*] Size of the Python List = %d\n", psize);
	printf("[*] Allocated = %d\n", plsize);
	for (i = 0; i < psize; i++)
	{
		ptype = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, (char *)Py_TYPE(ptype)->tp_name);
	}
}
