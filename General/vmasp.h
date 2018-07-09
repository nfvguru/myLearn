#ifndef MY_HASH_H
#define MY_HASH_H
#include <byteswap.h>

#define VADC_MAX_HASH_ENTIES (256)
#ifndef __IN__
#define __IN__
#endif
#ifndef __OUT__
#define __OUT__
#endif

#define ALIGN_64 __attribute__((aligned(8)))
#define MAX_CORES                   51           
#define TD_MAX_TDS                      (50)
#define MAX_CU_PER_CORE 4
#define MAX_SP_CORES (MAX_CORES - 1)
#define MAX_VADCS (MAX_SP_CORES * MAX_CU_PER_CORE) 
#define TD_MAX_VADCS                    MAX_VADCS

#ifndef SWAP32
#define SWAP32(x)       __bswap_32((x))
#endif


typedef char                INT_8;
typedef short               INT_16;
typedef long                INT_32;
typedef long long int       INT_64;

typedef unsigned char           UINT_8;
typedef unsigned short          UINT_16;
typedef unsigned long           UINT_32;
typedef unsigned long long int  UINT_64;

#define U8      unsigned char
#define U16     unsigned short
#define U32     unsigned long

#ifndef __TYPES_HAVE_bits32_t_
typedef unsigned long   bits32_t; /* 32 bits */
#endif
#ifndef __TYPES_HAVE_inaddr_t_
typedef bits32_t        inaddr_t; /* IP address */
#endif


#define FALSE 0
#define TRUE 1
#define bool unsigned char


typedef struct vma_hash_table {
    UINT_32           hash[VADC_MAX_HASH_ENTIES];           /* hash array */
} ALIGN_64 VMA_HASH_TABLE;


typedef struct {
    UINT_32 slotId;                 /* Slot ID on the core for the SP (0-MAX SP's per core) */
    UINT_32 weight;                 /* SP Weight per core */
} ALIGN_64 VADC_SP;

VMA_HASH_TABLE *pVMAHashTable;

UINT_32 g_td_max_num_tds_in_proccesing_unit = 50;
UINT_32 g_td_max_sps_per_vadc = 50;

void assert(bool assert);
#endif /* MY_HASH_H */
