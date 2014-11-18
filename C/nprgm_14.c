#include <stdio.h>

int main()
{
	int a[5];
	void reaMe ( int a [], int k);
	void prnMe ( int a [], int k);
	void sorMe ( int a [], int k);
	void swaMe ( int *x, int *y);
	printf("Enter elements for Array 1\n");
	reaMe(a, 5);
	printf("Array A:");
	prnMe(a, 5);
	sorMe(a, 5);
	printf("Array A:");
	prnMe(a, 5);
}

void reaMe( int a [], int k) {
	int i;
	for (i=0; i < k ; i ++) 
		scanf("%d", &a[i]);
	fflush(stdin);	
}

void prnMe ( int a [], int k) {
	int i;
	for (i=0; i < k ; i ++) 
		printf("%d-->%d ",i, a[i]);
	printf("\n");
}

void swaMe(int *x, int *y)
{
	int temp;
	temp = *x;
	*x = *y;
	*y = temp;

}

void sorMe ( int a [], int k) {
	int i,j;
	int temp;
	for (i=0; i < (k-1) ; i++)
	{
	   	for(j=0; j < (k-(i+1)); j++ )
	   	{
			//printf("%d,%d = [%d] [%d] ", i, j, a[i], a[j]);
			if ( a[j] > a[j+1] ){
				//printf("swap ");
				swaMe(&a[j], &a[j+1]);
			}
		}
		//printf(" \n");
	}
}

