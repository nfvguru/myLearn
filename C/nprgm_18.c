#include <stdio.h>
#include <sys/types.h>
#include <sys/ipc.h>

int main()
{
	key_t key;
	char r;
	for ( r='a'; r <= 'd'; r++)
	{	key=ftok(".", r);
		printf("%c- %X\n", r, key);
	}
	printf("Hello World!\n");
}
