#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>

const int MAX=5;
#define PIPE_BUF 1000
int main()
{
	FILE *fin;
	char buffer[PIPE_BUF], proj='a';
	int i, n, mid[MAX];
	key_t k;
	for (i=0; i<= MAX; i++, proj++) {
		k = ftok(".", proj);
		if ( (mid[i]=msgget(k,IPC_CREAT | 0660 )) == -1 ) {
			perror("MSGGET=");
			return 1;
		}
	}
	fin=popen("ipcs", "r");
	while ((n=read(fileno(fin),buffer,PIPE_BUF)) > 0) 
		write(fileno(stdout), buffer, n);
	pclose(fin);

	for(i=0; i<= MAX; i++) 
		msgctl(mid[i], IPC_RMID, (struct msgid_ds *)0);

	return 0;			
}
