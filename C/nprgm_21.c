#include <stdio.h>

#define VADC_MAX_HASH_ENTIES (256)
#ifndef __IN__
#define __IN__
#endif
#ifndef __OUT__
#define __OUT__
#endif

#define ALIGN_64 __attribute__((aligned(8)))
#define MAX_CORES                   39           
#define MAX_CU_PER_CORE 4
#define MAX_SP_CORES (MAX_CORES - 1)
#define MAX_VADCS (MAX_SP_CORES * MAX_CU_PER_CORE) 
#define TD_MAX_VADCS                    MAX_VADCS

typedef char                INT_8;
typedef short               INT_16;
typedef long                INT_32;
typedef long long int       INT_64;

typedef unsigned char           UINT_8;
typedef unsigned short          UINT_16;
typedef unsigned long           UINT_32;
typedef unsigned long long int  UINT_64;
#define bool unsigned char


typedef struct vma_hash_table {
    UINT_32           hash[VADC_MAX_HASH_ENTIES];           /* hash array */
} ALIGN_64 VMA_HASH_TABLE;


typedef struct {
    UINT_32 slotId;                 /* Slot ID on the core for the SP (0-MAX SP's per core) */
    UINT_32 weight;                 /* SP Weight per core */
} ALIGN_64 VADC_SP;

VMA_HASH_TABLE *pVMAHashTable;

UINT_32 g_td_max_num_tds_in_proccesing_unit = 8;
UINT_32 g_td_max_sps_per_vadc = 8;

void assert(bool assert);
void assert(bool assert)
{
   if(assert) printf("OK\n");
   else printf("Not OK. Gonna Panic\n");
}

int vADC_Hash_Init(__IN__ VADC_SP *pVadcSp, __OUT__ VMA_HASH_TABLE *pHashTable)
{
    UINT_32  i, j, spIndex, nSPs = 0;
    UINT_32 weightOffset = 0;
    UINT_32 weights[TD_MAX_VADCS];

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


int main(int argc, char*argv[])
{
    int curcu=2;
    static VADC_SP sp[TD_MAX_TDS];

    if (argc < 1) {
       curcu = atoi(argv[1]);
    }
    printf("Initializing HashTable for %d CUs\n",curcu);
}
