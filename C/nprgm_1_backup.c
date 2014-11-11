#include <stdarg.h>
#include <stdio.h>

int mymean(int x, ...)
{
	va_list myargs;
	int mmean = 0;
	va_start(myargs, x);
	int i;
	for (i = 0; i < x; i++)
	{
		printf ("mymean= %d\n", mmean);
		mmean += va_arg (myargs, int);
	}
	va_end(myargs);
	mmean /= x ;
	return mmean;
}
int main()
{
	printf ("Mean is %d\n", mymean(5, 1, 2, 3, 4, 5));
}
