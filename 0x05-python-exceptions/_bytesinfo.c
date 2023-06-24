#include "stdio.h"

/**
 * print_python_bytes - function to print bytes
 * @p: pointer to string
 *
 * Return;
 */

void print_python_bytes(char *p)
{
	if (p == NULL)
	{
		return;
	}
	printf("[.] bytes info\n  size: %ld\n  trying string: %s\n  bytes: ", _strlen(p), p);

	int i = 0;
	if (_strlen(p) < 10)
	{
		while (i < _strlen(p))
		{
			printf("%x ", p[i]);
			i++;
		}
	}
	else
	{
		while (i < 10)
		{
			printf("%x ", p[i]);
			i++;
		}
	}
}
