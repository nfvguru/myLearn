#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <string.h>
#include "vmasp.h"


VMA_HASH_TABLE *pVMAHashTable;
VMA_HASH_TABLE *pVMAHashTableNew;

U8 hashPattern[1024] = { 0 };
int HPind =0;

void assert(bool assert)
{
   if(!assert) {
     printf("Not OK. Gonna Panic\n");
   }
}



int vADC_New_Hash_Init(__IN__ VADC_SP *pVadcSp, __OUT__ VMA_HASH_TABLE *pHashTable)
{
    UINT_32  i=0, j=0, spIndex=0, nSPs = 0;
    UINT_32 weightOffset = 0;
    UINT_32 weights[TD_MAX_VADCS] = {0};
    bool processComplete = FALSE;
    VADC_SP spAllocatedWeights[TD_MAX_TDS]={0,0};


    while ( !processComplete ) {
        spIndex = 0;
        processComplete = TRUE;
        for (i = 0; i < g_td_max_num_tds_in_proccesing_unit; ++i)
        {
            /* only used if the weight is not 0 */
            if (pVadcSp[i].weight != 0  &&      // //Make sure in SP this is initialized???????
                spAllocatedWeights[i].weight < pVadcSp[i].weight )    
            {
                assert(spIndex < g_td_max_sps_per_vadc);
                weights[weightOffset++] = spIndex;
                spAllocatedWeights[i].weight++;
                if ( spAllocatedWeights[i].weight < pVadcSp[i].weight ) processComplete = FALSE;
                
            }
            spIndex++;
            if ( nSPs < spIndex) nSPs = spIndex;

        }    
        
    }


    /*
     * treat capacity units - spread the weights .. each spindex will appear more than once.
     * this is to try and speared out the load on the SP's
     *                */
    assert(weightOffset > 0);

    for (i = 0; i < VADC_MAX_HASH_ENTIES; ++i) {
        pHashTable->hash[i] = weights[i%weightOffset];
    }

    assert(nSPs != 0);
    if (nSPs == 0) return -1;

    return(1);
}


int vADC_Hash_Init(__IN__ VADC_SP *pVadcSp, __OUT__ VMA_HASH_TABLE *pHashTable)
{
    UINT_32  i=0, j=0, spIndex=0, nSPs = 0;
    UINT_32 weightOffset = 0;
    UINT_32 weights[TD_MAX_VADCS] = {0};

    for (i = 0; i < g_td_max_num_tds_in_proccesing_unit; ++i)
    {
        /* only used if the weight is not 0 */
        if (pVadcSp[i].weight != 0)      //Make sure in SP this is initialized???????
        {
            spIndex = nSPs;
            assert(nSPs < g_td_max_sps_per_vadc);

            /* update the weight array */
            for (j = 0; j < pVadcSp[i].weight; ++j)
            {
                weights[weightOffset++] = spIndex;
            }
            nSPs++;
        }
    }


    /*
     * treat capacity units - spread the weights .. each spindex will appear more than once.
     * this is to try and speared out the load on the SP's
     *                */
    assert(weightOffset > 0);

    for (i = 0; i < VADC_MAX_HASH_ENTIES; ++i) {
        pHashTable->hash[i] = weights[i%weightOffset];
    }

    assert(nSPs != 0);
    if (nSPs == 0) return -1;

    return(1);
}

float percentage(int base, int cur)
{
    float retval=0;
    if ( base == 0 ) return 0.0;
    retval = ((float) (cur - base ) / base) * 100.00;
    return retval;
}

void printHashTable(VMA_HASH_TABLE *pHashTable, int maxsps, float expected[])
{
    int i = 0, j=0;
    int counts[maxsps];
    int base =0;
   
    for (j=0; j < maxsps; j++) {
       counts[j] = 0;
    }
#ifdef DEBUG    
    printf("Hash Table: \n\t( ");
#endif
    for (i = 0; i < VADC_MAX_HASH_ENTIES; ++i) {
#ifdef DEBUG    
       printf("%lu,", pHashTable->hash[i]);
#endif
       counts[pHashTable->hash[i]] +=1;
    }
#ifdef DEBUG    
    printf(")\n");
#endif
    printf("\nResult: \n");
    for (i = 0; i < maxsps; ++i)
    {
       printf("SP %d process %d out of %d ", 
         i, counts[i], VADC_MAX_HASH_ENTIES );
       if (i==0) {
         base = counts[i];
         printf("\n");
       } else {
         printf("\t( %0.2f%% )\n", percentage(base,counts[i]));
       }
       
      
    }
    printf("\n");
}
//#####################################################################################################################

static int attache_atoi (const char *s)
{
  int value;

  value = 0;
  while ((*s >= '0') && (*s <= '9'))
    value = (value * 10) + (*s++ - '0');
  return value;
}

U32 atoinet_ext(const char *name,U32 *ip_p)
{
  union {
    char bytes[4];
    inaddr_t whole_thing;
  } in_pieces;
  int i;
  const char *piece;

  /* Skip leading whitespace */
  while (name && ((*name == ' ') || (*name == '\t')))
    name++;

  for (i = 0; i < 4; i++) {
    piece = name;
    while (name && ((*name >= '0') && (*name <= '9')))
      name++;
    if (piece == name)
      return 0;                 /* zero length piece */
#if defined(NO_ALTEON_CHANGES)
    in_pieces.bytes[i] = (char)attache_atoi(piece);
#else  /* defined(NO_ALTEON_CHANGES) */
{
    unsigned int temp = attache_atoi(piece);
    if (temp > 255)
        return 0;
    in_pieces.bytes[i] = (char)temp;
}
#endif /* defined(NO_ALTEON_CHANGES) */
    if (i == 3)
      break;                    /* don't need a . after last piece */
    if (name && (*name != '.'))
      return 0;                 /* do need a . after other pieces */
    name++;
  }
    if (name && (*name != '\0'))
      return 0;

  *ip_p = (U32)in_pieces.whole_thing;
  return 1; /* status ok */
}

inaddr_t
  atoinet(const char *name)
{
    U32 ip;

    if (atoinet_ext(name,&ip)) /* success */
    {   
        return ip;
    }
    else /* error*/
    {
        return 0;       
    }
}


bool get_ip_addr(const char *p, U32 *addr, const char *name)  /* zero allowed as 0.0.0.0 or 0  */
{
    bool rc = TRUE;
    *addr = atoinet(p);
    if (*addr == 0) {
        if (strcmp(p, "0.0.0.0") && strcmp(p, "0")) {
            if (*name) {
                printf("Error: bad %s \"%s\"\n", name, p);
            }
            rc = FALSE;
        }
    }
    return(rc); 
}

void printHashAlgo(const U32 addr)
{
   U32 tmp_hash = (addr>>24);
   printf("addr  -%lu\n", addr);
   printf("first -  %u\n", (U8)tmp_hash);
   tmp_hash =  (addr>>24) ^ (addr>>16);
   printf("second -  %u\n", (U8)tmp_hash);
   tmp_hash =  (addr>>24) ^ (addr>>16)^ (addr>>8);
   printf("third -  %u\n", (U8)tmp_hash);
   tmp_hash =  (addr>>24) ^ (addr>>16)^ (addr>>8)^ addr;
   printf("fourth -  %u\n", (U8)tmp_hash);
}

static __inline__ U8 tdHash_32b(const U32 addr, bool is_reduction_required, U32 num_of_macs)
{
     U32 temp_hash_32b = (addr>>24) ^ (addr>>16) ^ (addr>>8) ^ addr;
     return *(U8*)&temp_hash_32b;
}

static __inline__ U8 tdHash_ipv4(const U32 addr, bool is_reduction_required, U32 num_of_macs)
{
    return tdHash_32b(addr, is_reduction_required, num_of_macs);
}

static __inline__ int getVMASp(U8 hash, VMA_HASH_TABLE *pHashTable)
{
    U8 index;
    U32 spIndex;
    index = hash % VADC_MAX_HASH_ENTIES;
    spIndex = pHashTable->hash[index];
    return(spIndex);
}


U32 vma_mp_get_sp(U32 cip, U32 dip, U32 cport, U16 dport, bool old);
U32 vma_mp_get_sp(U32 cip, U32 dip, U32 cport, U16 dport, bool old)
{
    U32 sp,addr;
    U8 hash;

    addr = cip;
    hash = tdHash_ipv4(addr, FALSE, 0);
    if( old) {
       //printHashAlgo(addr);
       if (HPind < 1024)  hashPattern[HPind] = hash;
       HPind++;
       sp = getVMASp(hash, pVMAHashTable) + 1;
    } else {
       sp = getVMASp(hash, pVMAHashTableNew) + 1;
    }
    return sp;
}

static inline float totalPerc(int total, int cur)
{
    if ( total == 0) return 0.0;
    return (((float) cur/total) * 100);
}


void printVmaMap(int numIPs, int numSPs)
{
    //printf("Printing VMA SP for %d IPs\n", numIPs);
    char * mymask="255.255.255.255";
    char myIP[32] = {0};
    int  thirdO = 2;
    int  fourthO = 3;
    int  loopC  = 0;
    U32 ip, ip_old, nmask;
    U32 sport = 0, dport = 0, sp1 = 1, sp2=1;
    U32 dip = 0;
    int sp1stats[256]={0};
    int sp2stats[256]={0};

    get_ip_addr(mymask, &nmask, "Subnet Mask");
    nmask = SWAP32(nmask);

    printf("\t====IP=====\tHASH\t=====OLD ALGO =====\t======NEW ALGO====\n");
    for ( loopC = 0; loopC < numIPs; loopC++ ) {
        snprintf(myIP,sizeof(myIP),"2.2.%d.%d",thirdO, fourthO);
//
        get_ip_addr(myIP, &ip, "Source IP address");
        ip = SWAP32(ip) & nmask;
        ip_old = ip;
        while ((ip & nmask) == ip_old) {
           sp1 = vma_mp_get_sp(ip, SWAP32(dip), sport, dport, TRUE);
           sp1stats[sp1]++;
           sp2 = vma_mp_get_sp(ip, SWAP32(dip), sport, dport, FALSE);
           sp2stats[sp2]++;
           ip++;
        }
//
        printf("\t%s%-10s%u%-10s\tSP %lu%-10s\tSP %lu\n", myIP," ", hashPattern[HPind-1]," ",sp1," ",sp2);
        fourthO++;
        if (fourthO > 255 ) {
            fourthO = 1;
            thirdO++;
            if(thirdO > 255 ) {
               printf("Max reached. Exiting...\n");
               return;
            }
        }
     
    }
    printf("================= Distribution of IPs ===========================\n\n");

    printf("\t====SP=====\t=====OLD ALGO=====\t======NEW ALGO====\n");
    
    for ( loopC = 0; loopC < numSPs ; loopC++ ) {
        printf("\tSP %d%-10s\t%d - %0.2f %%%-10s\t%d - %0.2f %%\n", loopC+1," ",
                sp1stats[loopC+1], totalPerc(numIPs, sp1stats[loopC+1])," ",
                sp2stats[loopC+1], totalPerc(numIPs, sp2stats[loopC+1]));
    }
    
}

void printHashPattern(void)
{
    int i=0;

    for (i=0; i<HPind; i++) {
       printf("%u,",hashPattern[i]);
    }
    printf("\n");
}

//#####################################################################################################################

int main(int argc, char*argv[])
{
    static VADC_SP sp[TD_MAX_TDS];
    float expected[TD_MAX_TDS] = {0};
    int originalcu=0, curcu=2;
    int spindex=0;
    int i=0,weight=0;
    float perCuShare=0;
    int numIps=1;

    if (argc > 1) {
       curcu = atoi(argv[1]);
    }
    if (argc > 2) {
       numIps = atoi(argv[2]);
    }
    originalcu = curcu;
    printf("========================================================================================\n");
    printf("\nProcessing for  %d CUs, %d IPs\n",curcu, numIps); 
    while ( curcu > 0 ) {
        if( curcu >= 4 )  weight = 4;
        else weight = curcu;
        
        sp[spindex].weight = weight;
        spindex++;
        curcu -= weight;
        if ( spindex >= g_td_max_sps_per_vadc )
        {
           printf("Max SPs is possible is %lu. Unallocatd CUs is %d\n", g_td_max_sps_per_vadc, curcu);
           originalcu -= curcu;
           break;
        }
    }
    perCuShare=(float)(256/(float)originalcu);
    for ( i=0; i < spindex; i++) {
        expected[i] = (float) (perCuShare * sp[i].weight);
    }

    pVMAHashTable = (VMA_HASH_TABLE *) malloc(sizeof(VMA_HASH_TABLE));
    vADC_Hash_Init(sp, pVMAHashTable);
    //printf("=============================>>>   Legacy Algorithm  <<<====================================\n");
    //printHashTable(pVMAHashTable,spindex, &expected[0]);
    pVMAHashTableNew = (VMA_HASH_TABLE *) malloc(sizeof(VMA_HASH_TABLE));
    vADC_New_Hash_Init(sp, pVMAHashTableNew);
    //printf("===============================>>>   New Algorithm  <<<=====================================\n");
    //printHashTable(pVMAHashTableNew,spindex, &expected[0]);
    printf("===============================>>>   VMASP  <<<=====================================\n");
    printVmaMap(numIps, spindex);
    //printHashPattern();
    
}
