#ifndef MAX_NUMBER
#define MAX_NUMBER 10000
#endif

#ifndef __STDIO_H__
#define __STDIO_H__
#include <stdio.h>
#endif
#ifndef __MALLOC_H__
#define __MALLOC_H__
#include<malloc.h>
#endif
#ifndef __TIME_H__
#define __TIME_H__
#include<time.h>
#endif
#ifndef __STDLIB_H__
#define __STDLIB_H__
#include<stdlib.h>
#endif


#ifndef __MATRIX_H__
#define __MATRIX_H__

int** matrix_Multi(int **a, int na, int ma, int **b, int nb, int mb);
int print_Matrix(int **a, int n, int m);
int** random_Matrix(int **a, int n, int m);

void matrix_Multi_s(int *a[], int na, int ma, int *b[], int nb, int mb);
void print_Matrix_s(int *a[], int n, int m);
void random_Matrix_s(int *a[], int n, int m);


/*************     Dynamic     ************/
int** random_Matrix(int **a, int n, int m){
    for (int i=0;i<n;++i){
        for (int j=0;j<m;++j){
            a[i][j] = rand() % MAX_NUMBER;
        }
    }
    return a;
}

int print_Matrix(int **a, int n, int m){
    printf("Matrix data:\n");
    for (int i=0;i<n;++i){
        for (int j=0;j<m;++j){
            printf("%d\t", a[i][j]);
        }
        printf("\n");
    }

    return 0;
}

int** matrix_Multi(int **a, int na, int ma, int **b, int nb, int mb){
    if (ma!=nb){
        printf("ma not equal nb!\n");
        return NULL;
    }

    int i, row, col;

    int **result=(int**)malloc(na*sizeof(int*));
    for (i=0;i<na;++i){
        result[i] = (int*)malloc(mb*sizeof(int));
    }

    for (row=0;row<na;++row){
        for (col=0;col<mb;++col){
            result[row][col] = 0;
            for(i=0;i<ma;++i){
                result[row][col] += a[row][i]*b[i][col];
            }
        }

    }

    return result;
}

/*************     Static     ************/
void random_Matrix_s(int *a[], int n, int m){
    for (int i=0;i<n;++i){
        for (int j=0;j<m;++j){
            a[i][j] = rand() % MAX_NUMBER;
        }
    }
}

void print_Matrix_s(int *a[], int n, int m){
    printf("Matrix data:\n");
    for (int i=0;i<n;++i){
        for (int j=0;j<m;++j){
            printf("%d\t", a[i][j]);
        }
        printf("\n");
    }
}

void matrix_Multi_s(int *a[], int na, int ma, int *b[], int nb, int mb){
    if (ma!=nb){
        printf("ma not equal nb!\n");
    }

    int i, row, col;

    int **result=(int**)malloc(na*sizeof(int*));
    for (i=0;i<na;++i){
        result[i] = (int*)malloc(mb*sizeof(int));
    }

    for (row=0;row<na;++row){
        for (col=0;col<mb;++col){
            result[row][col] = 0;
            for(i=0;i<ma;++i){
                result[row][col] += a[row][i]*b[i][col];
            }
        }

    }
}

#endif