#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include "myhash.h"


VMA_HASH_TABLE *pVMAHashTable;
VMA_HASH_TABLE *pVMAHashTableNew;

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


int main(int argc, char*argv[])
{
    static VADC_SP sp[TD_MAX_TDS];
    float expected[TD_MAX_TDS] = {0};
    int originalcu=0, curcu=2;
    int spindex=0;
    int i=0,weight=0;
    float perCuShare=0;

    if (argc > 1) {
       curcu = atoi(argv[1]);
    }
    originalcu = curcu;
    printf("\nHashTable for %d CUs\n",curcu); 
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
    printf("=============================>>>   Legacy Algorithm  <<<====================================\n");
    printHashTable(pVMAHashTable,spindex, &expected[0]);
    pVMAHashTableNew = (VMA_HASH_TABLE *) malloc(sizeof(VMA_HASH_TABLE));
    vADC_New_Hash_Init(sp, pVMAHashTableNew);
    printf("===============================>>>   New Algorithm  <<<=====================================\n");
    printHashTable(pVMAHashTableNew,spindex, &expected[0]);
    
}
