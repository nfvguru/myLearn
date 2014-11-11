#include <stdio.h>
#include <stdlib.h>
int main()
{
	void *i;
	i=malloc(100+15);
	void *ptr= ((int)i+15) & ~0x0F;
	char *lava = (char *) ptr;
	printf("orig=%p new %p, modulus %d \n", i, ptr, ((int)ptr)%16);
	free(i);
}
