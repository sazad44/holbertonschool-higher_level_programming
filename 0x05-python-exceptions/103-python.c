#include <Python.h>
#include <sys/types.h>
#include <pyport.h>
#include <object.h>
#include <listobject.h>
#include <string.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p)
{
	unsigned int psize = (unsigned int)(((PyVarObject *)(p))->ob_size), i;
	unsigned int pall = (unsigned int)(((PyListObject *)(p))->allocated);
	PyObject **plitem = ((PyListObject *)(p))->ob_item;
	char *pltype = (char *)((PyListObject *)(p)->ob_type->tp_name);
	char *ptype = NULL;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!strcmp("list", pltype))
	{
		printf("[*] Size of the Python List = %u\n", psize);
		printf("[*] Allocated = %u\n", pall);
		for (i = 0; i < psize; i++)
		{
			ptype = (char *)(plitem[i])->ob_type->tp_name;
			printf("Element %d: %s\n", i, ptype);
			if (!strcmp("bytes", ptype))
				print_python_bytes(plitem[i]);
			else if (!strcmp("float", ptype))
				print_python_float(plitem[i]);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

void print_python_bytes(PyObject *p)
{
	char *pstr;
	Py_ssize_t plen;
	unsigned int psize, i;
	char *ptype = NULL;

	setbuf(stdout, NULL);
	ptype = (char *)(p->ob_type->tp_name);
	printf("[.] bytes object info\n");
	if (!strcmp("bytes", ptype))
	{
		PyBytes_AsStringAndSize(p, &pstr, &plen);
		psize = (int)PyBytes_Size(p);
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
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

void print_python_float(PyObject *p)
{
	char *pftype = (char *)((PyListObject *)(p)->ob_type->tp_name);
	char floatarr[100];
	unsigned int i;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!strcmp("float", pftype))
	{
		sprintf(floatarr, "%3.15f", PyFloat_AsDouble(p));
		for (i = 0; floatarr[i]; i++)
		{
			if (floatarr[i] == '0' && ((i > 2) && floatarr[0] != '-'))
				floatarr[i] = '\0';
			if (floatarr[i] == '0' && (i > 3))
				floatarr[i] = '\0';
		}
		printf("  value: %s\n", floatarr);
	}
	else
		printf("  [ERROR] Invalid Float Object\n");
}
