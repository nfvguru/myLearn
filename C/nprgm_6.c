#include <stdio.h>

int main()
{
	int no;
	printf("Enter a number: ");
	scanf("%d", &no);
	( no & 1 && printf("odd\n"))|| printf("even\n");
}
