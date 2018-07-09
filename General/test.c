#include <stdio.h>
#include <stdlib.h>

#define U8      unsigned char
#define U16     unsigned short
#define U32     unsigned long

#define BASEIP 33686019

U32 valueArray[32]= { 0 };
int indexo = 0;

void bin(U32 n)
{
    /* step 1 */
    if (n > 1)
        bin(n/2);

    /* step 2 */
    valueArray[indexo] = n % 2 ;
    indexo++;
}

void printBinary(U32 val) 
{
    int i=0, j=0, k=0, l=0;
    indexo=0;
    for( i = 0; i < 32; i++) valueArray[i]= 0;
    bin(val);
    //printf("indexo= %d\n", indexo);
    k= 32 - indexo;
    //printf("k= %d\n", k);
    for ( l = 0; l < k; l++) {
       printf("0");
       j++;
       if( j >= 8 ) {
         j=0;
         printf(" ");
       }
    } 
    //printf("j= %d\n", j);
    for( i = 0; i < (32-l); i++) {
       printf("%lu",valueArray[i]);
       j++;
       if( j >= 8 ) {
         j=0;
         printf(" ");
       }
    }
    printf("\n");
}

void printHashAlgo(const U32 addr)
{
   U32 tmp_hash = 0;
   printf("A = Addr         : ");
   printBinary(addr);
  
   printf("B = Addr >> 24   : ");
   printBinary((addr>>24));
   printf("C = Addr >> 16   : ");
   printBinary((addr>>16));
   printf("D = Addr >> 8    : ");
   printBinary((addr>>8));
   printf("------------------------------------------------------------------\n");
   tmp_hash =  (addr>>24) ^ (addr>>16)^ (addr>>8)^ addr;
   printf("A ^ B ^ C ^ D    : ");
   printBinary(tmp_hash);
   printf("Hash Value (last 8 bits)  -  %u  <<<<<<<<<<<<<<\n\n", (U8)tmp_hash);
}


int main(int argc, char*argv[])
{
    int maxips=1;
    int loop;
    if (argc > 1) {
       maxips = atoi(argv[1]);
    }
    for (loop =0; loop < maxips; loop ++ ) {
       printf("\n=====> SRC IP : 2.2.2.%d  <==================================\n",loop+3);
       printHashAlgo(BASEIP + loop);
    }

}
