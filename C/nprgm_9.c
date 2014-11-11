#include <stdio.h>

#define mysizeof(type) (char *) (&type+1) - (char *) (&type)
int main()
{
	float a;
	int  b;
	char c;
	printf("size of float=%d, int=%d, char=%d\n", mysizeof(a), mysizeof(b), mysizeof(c));
}
