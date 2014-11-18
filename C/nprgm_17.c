#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netinet/ip_icmp.h>
#include <netinet/udp.h>
#include <netinet/tcp.h>
#include <netinet/ip.h>
#include <sys/socket.h>
#include <arpa/inet.h>

void ProcessPacket(unsigned char * buffer, int size);
void print_ip_header(unsigned char * buffer, int size);
void print_tcp_packet(unsigned char * buffer, int size);
void print_udp_packet(unsigned char * buffer, int size);
void print_icmp_packet(unsigned char * buffer, int size);
void PrintData (unsigned char * buffer, int size);

int sock_raw;
int tcp=0, udp=0, icmp=0, igmp=0, others=0, total=0, i, j;
struct sockaddr_in source, dest;

int main()
{
	int loop=0;
	int saddr_size, data_size;
	struct sockaddr saddr;
	struct in_addr in;

	unsigned char * buffer =(unsigned char *)malloc(65536);
	printf("..............L A V A N Z  SNIFFER...........................\n");
	sock_raw = socket(AF_INET, SOCK_RAW, IPPROTO_TCP);
	if (sock_raw < 0) { printf("socket Error!!!\n"); return 1;}
	while( loop < 1 ){
		saddr_size = sizeof saddr;
		data_size = recvfrom(sock_raw, buffer, 65536, 0, &saddr, &saddr_size);
		if(data_size < 0) {printf("recv error!!!\n"); return 1;}
		loop++;
		ProcessPacket(buffer, data_size);	
	}
	close(sock_raw);
	printf("\n");
	return 0;
}

void ProcessPacket(unsigned char * buffer, int size) 
{
	struct iphdr *iph = (struct iphdr*) buffer;
	++total;
	switch(iph->protocol)
	{
		case 1: //ICMP
			++icmp;
			break;
		case 2: // IGMP
			++igmp;
			break;
		case 6: //TCP
			++tcp;
			print_tcp_packet(buffer, size);
			break;

		case 17: //UDP
			++udp;
			break;

		default:
			++others;
			break;
	}
	printf("Total %d ==> TCP : %d, UDP:%d, ICMP=%d, IGMP:%d, OTHERS:%d \n", \
		total, tcp, udp, icmp, igmp, others);
	printf("---------------------------------------------------------------\n");
}
void print_ip_header(unsigned char *buffer, int size) 
{
	unsigned short iphdrlen;
	struct iphdr *iph = (struct iphr *) buffer;

	memset(&source, 0, sizeof(source));
	source.sin_addr.s_addr = iph->saddr;
	printf("%x\n", ntohl(iph->saddr));

	memset(&dest, 0, sizeof(dest));
	dest.sin_addr.s_addr = iph->daddr;

	printf("<========================== IP Header ===================>i\n");
	printf("IP Version    : %d\n", (unsigned int)iph->version);
	printf("IP Header Len : %d DWORDS (%d Bytes)\n",\
				(unsigned int)iph->ihl,((unsigned int)(iph->ihl))*4);
	printf("TOS           : %d\n", (unsigned int)iph->tos);
	printf("Total Length  : %d Bytes\n",ntohs(iph->tot_len));
	printf("Identification: %d\n",ntohs(iph->id));
	printf("TTL	      : %d\n", (unsigned int)iph->ttl);
	printf("Protocol      : %d\n", (unsigned int)iph->protocol);
	printf("Checksum      : %d\n", ntohs(iph->check));
	printf("Source IP     : %s\n", inet_ntoa(source.sin_addr));
	printf("Dest.  IP     : %s\n", inet_ntoa(dest.sin_addr));
	printf("<========================================================>i\n");

}
void print_tcp_packet(unsigned char *buffer, int size) 
{
	unsigned short iphdrlen;
	struct iphdr *iph = (struct iphdr *) buffer;
	iphdrlen = iph->ihl*4;
	struct tcphdr *tcph=(struct tcphdr*) (buffer + iphdrlen);
	print_ip_header(buffer, size);
}

void print_udp_packet(unsigned char *buffer, int size) {}
void print_icmp_packet(unsigned char *buffer, int size) {}
void PrintData (unsigned char *buffer, int size) {}

/* 
Ref: 
http://www.binarytides.com/packet-sniffer-code-c-linux/
http://simplestcodings.blogspot.in/2010/10/create-your-own-packet-sniffer-in-c.html 
*/
