#include <stdio.h>

int countBits(unsigned int a)
{
	unsigned int count=0;
	while ( a)
	{
		a &= (a - 1);
		count ++;
	}
	return count;
}
int main()
{
	int a = 15;
	printf("No of Bits sets=%d\n\n", countBits(1));
	printf("No of Bits sets=%d\n\n", countBits(3));
	printf("No of Bits sets=%d\n\n", countBits(7));
	printf("No of Bits sets=%d\n\n", countBits(15));
	printf("No of Bits sets=%d\n\n", countBits(31));
	printf("No of Bits sets=%d\n\n", countBits(63));
	printf("No of Bits sets=%d\n\n", countBits(127));
	printf("No of Bits sets=%d\n\n", countBits(255));
	printf("No of Bits sets=%d\n\n", countBits(511));
	printf("No of Bits sets=%d\n\n", countBits(1023));
}
