#include <stdio.h>
#include <math.h>

float roundOff(float n, int a)
{
	return ( (int)(( n * pow(10, a) + 0.5)) / pow(10,a));
}
int main()
{
	float val= 10.98765;
	printf("Value is %f\n", val);
	printf("Value Rounded is %f\n", roundOff(val,3));
}
