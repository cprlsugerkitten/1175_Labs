#include <stdio.h>
#include <time.h> 
#include <stdlib.h>

#define N 1024

int A[N][N];
int B[N][N];
int C[N][N];

int main(){
	srand((unsigned)time(NULL));
	for (int i = 0; i< N; i++)
	{
		for(int j = 0; j< N; j++)
		{
			A[i][j] = rand()/(int)RAND_MAX;
			B[i][j] = rand()/(int)RAND_MAX;
		}
	}
	clock_t start_time = clock();
	//matrix multiplication code
	
	for(int i = 0; i<N; i++)
	{
		for(int j = 0; j<N; j++)
		{
			float sum = 0;
			for (int k =0; k<N; k++)
			{
				sum += A[i][k] * B[k][j];
			}
			C[i][j] = sum;
		}
	}
	
	clock_t end_time = clock();
	float elapse = (float) (end_time - start_time) / CLOCKS_PER_SEC;
	printf("elapse: %.4f seconds\n", elapse);
	
	
	return 0;
}
