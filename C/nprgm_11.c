#include <stdio.h>

int main()
{
	int a[5], b[5], c[10]; 
	void reaMe ( int a [], int k);
	void prnMe ( int a [], int k);
	void sorMe ( int a [], int k);
	void merMe ( int a [], int b [], int c [], int k);
	printf("Enter elements for Array 1\n");
	reaMe(a, 5);
	printf("Array A:");
	prnMe(a, 5);
	printf("Enter elements for Array 2\n");
	reaMe(b, 5);
	printf("Array B:");
	prnMe(b, 5);
	sorMe(a, 5);
	printf("Array A:");
	prnMe(a, 5);
	sorMe(b, 5);
	printf("Array B:");
	prnMe(b, 5);
	merMe(a, b, c, 5);
	printf("Array C:");
	prnMe(c, 10);
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

void sorMe ( int a [], int k) {
	int i,j;
	int temp;
	for (i=0; i < (k-1) ; i++)
	{
	   	for(j=i+1; j < k; j++ )
	   	{
			//printf("%d,%d = [%d] [%d] ", i, j, a[i], a[j]);
			if ( a[i] < a[j] ){
				//printf("swap ");
				temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		}
		//printf(" \n");
	}
}

void merMe ( int a [], int b [], int c [], int k) 
{
	int i=0, j=0, l=0;
	while ( i < k && j < k ) {
		if(a[i] < b[j] ) {
			c[l] = b[j];
			j++;
		} else {
			c[l] = a [i];
			i++;
		}
		l++;
		
	}
	while ( i < k ) {
		c[l] = a [i];
		i++; l++;
	}
	while ( j < k ) {
		c[l] = b [j];
		j++; l++;
	}
}
