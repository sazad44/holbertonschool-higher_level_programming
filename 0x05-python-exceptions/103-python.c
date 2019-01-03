#include <Python.h>
#include <sys/types.h>
#include <pyport.h>
#include <object.h>
#include <listobject.h>

void print_python_list(PyObject *p)
{
	unsigned int psize = (unsigned int)(((PyVarObject *)(p))->ob_size), i;
	unsigned int pall = (unsigned int)(((PyListObject *)(p))->allocated);
	char *ptype = (char *)(((PyListObject *)(p))->ob_type->tp_name);

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %u\n", psize);
	printf("[*] Allocated = %u\n", pall);
	for (i = 0; i < psize; i++)
		printf("Element %d: %s\n", i, ptype);
}

void print_python_bytes(PyObject *p)
{
	char *pstr;
	Py_ssize_t plen;
	unsigned int psize;
	unsigned int i;

	setbuf(stdout, NULL);
	PyBytes_AsStringAndSize(p, &pstr, &plen);
	psize = (int)PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %d\n", psize);
	printf("  trying string: %s\n", pstr);
	if (psize < 10)
		printf("  first %d bytes: ", (psize + 1));
	else
		printf("  first 10 bytes: ");
	for (i = 0; i < psize + 1 && i < 10; i++)
		printf("%02x ", (unsigned char)pstr[i]);
	printf("\n");
}

void print_python_float(PyObject *p)
{
	(void)p;
}
