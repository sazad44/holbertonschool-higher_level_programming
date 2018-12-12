#include <stdio.h>
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
	int i, psize, plsize;
	char *ptype;

	plsize = (int)PyList_Size(p);
	psize = (int)Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", plsize);
	printf("[*] Allocated = %d\n", psize);
	for (i = 0; i <= plsize; i++)
	{
		ptype =  (char *)PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, ptype);
	}
}
