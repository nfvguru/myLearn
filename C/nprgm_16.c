#include <stdio.h>
/*#define hashIpAddress(x)\
        (unsigned int)(((x)[0])^((x)[1])^((x)[2])^((x)[3]));
*/

void printBinary(unsigned char hexN )
{
	static int count=0;
	if (!hexN){
		int i;
		//printf("|count=%d|", count);
		for(i=count; i < 8; i++){
			printf("0");
		}
		count=0;
		return;
	}
	count++;
	printBinary( hexN >> 1);
	if ( hexN & 1)
		printf("1");
	else
		printf("0");

	//printf("\n");
}

void printValues(unsigned char *valA, int size )
{
	int i;
	for (i=0; i < size; i++)
	{
		printf(" | %d -> %.2x -> ", valA[i], valA[i]);
		printBinary(valA[i]);	
	}
	printf("\n");
}

int main()
{
	char * ip= "192.168.4.1";
	printf ("%s\n", ip);
	unsigned char value[4]={0};
	//printValues(ip, 4);
	int index =0;
	//str1=ip;
	while (*ip) {
		if(isdigit((unsigned char )*ip)){
			value[index] *= 10;
			value[index] += *ip - '0';
		} else {
			index++;
		}
		ip++;
	}
	printValues(value, 4);
}
