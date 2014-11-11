#include <stdio.h>

void print_bye(unsigned char * loc, int size)
{
	int i=0;
	printf("======================MEM VALUES========================\n");
	for (i=0; i < size; i++ ) {
		printf("%p --> %.2x\n", loc+i , loc[i]);	
	}
}
int main()
{
	int j = 2;
	char k = 'a';
	float m = 2.3;
	double n = 5.6;
	printf("Value %d", j);
	print_bye(&j,sizeof(int));
	printf("Value %c", k);
	print_bye(&k,sizeof(char));
	printf("Value %f", m);
	print_bye(&m,sizeof(float));
	printf("Value %f", n);
	print_bye(&n,sizeof(double));
}
