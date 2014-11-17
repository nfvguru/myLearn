#include <stdio.h>
  
/* Find the number of elements in an array */
#define length(a) ( sizeof a / sizeof *a )
 
static size_t hash ( const char key )
{
   return key - '0';
}
 
 static void jsw_flush ( void );
 static int get_digit ( char *ch );
 
 static void fill_table ( char table[] );
 static void show_table ( const char table[], size_t size );
 
 int main ( void )
 {
   /* This is our hash table */
   char table[10] = {0};
   
   fill_table ( table );
   show_table ( table, length ( table ) );
 
   return 0;
 }
 
 /*
   Discard remaining characters in stdin
   up to the next newline or end-of-file
 */
 void jsw_flush ( void )
 {
   int ch;
 
   do
     ch = getchar();
   while ( ch != '\n' && ch != EOF );
 
   clearerr ( stdin );
 }
 
 /*
   Get a single character digit, '0'-'9'.
   Return 1 on success, 0 on input error,
   end-of-file, or invalid input
 */
 int get_digit ( char *ch )
 {
   int rc;
 
   printf ( "Enter a single digit: " );
   fflush ( stdout );
   
   if ( rc = scanf ( "%1[0123456789]", ch ) == 1 ) {
     /* At least a newline is left over; clear it all */
     jsw_flush();
   }
 
   return rc;
 }
 
 /* Populate the hash table */
 void fill_table ( char table[] )
 {
   char ch;
 
   while ( get_digit ( &ch ) ) {
     /* Create an index from the character */
     unsigned i = hash ( ch );
     
     if ( table[i] != 0 ) {
       /* Duplicate indexes are called collisions */
       printf ( "That index has been filled\n" );
     }
     else {
       /* The element is empty; fill it in */
       table[i] = ch;
     }
   }
 }
 
 /* Display the contents of the hash table */
 void show_table ( const char table[], size_t size )
 {
   size_t i;
 
   for ( i = 0; i < size; i++ ) {
     /* Mark empty elements as 'null' with the ~ character */
     printf ( "%c\n", table[i] != 0 ? table[i] : '~' );
   }
 }
