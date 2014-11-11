#include <stdio.h>

void printNum (int x)
{
	if ( x > 0 ) {
		printf("%d\n",  x);
		printNum(x-1);
	} else
		printf("\n");
	return;
}
int main()
{
	printNum(10);
	return 0;
}

