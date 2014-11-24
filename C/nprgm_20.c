#include <stdio.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>

int main()
{
	int mid;
	key_t key;
	struct msqid_ds msgid;
	key=ftok(".", 'z');
	if((mid=msgget(key, IPC_CREAT | 0660)) == -1){
		perror("MSG");
		return 1;
	}
	msgctl(mid,IPC_STAT,&msgid);
	printf("Own UID =%u\n", msgid.msg_perm.uid);
	printf("Own GID =%u\n", msgid.msg_perm.gid);
	printf("Cre UID =%u\n", msgid.msg_perm.cuid);
	printf("Cre GID =%u\n", msgid.msg_perm.cgid);
	printf("Access Mode=%X\n", msgid.msg_perm.mode);
	printf("----Additional-------------\n");
	printf("cur # bytes %u\n", msgid.__msg_cbytes);
	printf("cur # msgs %u\n", msgid.msg_qnum);
	printf("Max # byute%u\n", msgid.msg_qbytes);
	msgctl(mid,IPC_RMID, (struct msqid_ds *)0);
	return 0;
}
