#include <stdio.h>

int main()
{
	int *i = (int *) malloc (2 * sizeof(int));
	*i =10;
	*(i+1)=20;
	*(i+2)=30;
	printf("This program is not complete and will come back soon....\n");	
	printf("%d, %d, %d\n", *i, *(i+1), *(i+2));
	free(i);
}
