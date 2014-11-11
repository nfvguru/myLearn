#include <stdio.h>

inline int mysum(int x) {return  x==0?0:x%10+mysum(x/10);};
int main()
{
	int a=1234567;
	printf("Sum of Digits = %d \n", mysum(a));
}
