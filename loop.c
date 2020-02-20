#include <stdio.h>
#include<malloc.h>
#include<time.h>
#include<stdlib.h>

#define MAX_NUMBER 10000

int** matrix_Multi(int **a, int na, int ma, int **b, int nb, int mb);
int print_Matrix(int **a, int n, int m);
int** random_Matrix(int **a, int n, int m);

void sortArray(int *a, int n);
void printArray(int *a, int n);
void randomArray(int *a, int n);

void matrix_Multi_s(int *a[], int na, int ma, int *b[], int nb, int mb);
void print_Matrix_s(int *a[], int n, int m);
void random_Matrix_s(int *a[], int n, int m);

int sum(int a, int b);
int minus(int a, int b);
int mul(int a, int b);
int div_(int a, int b);
int mod(int a, int b);

/*
int main(){

    int a[3][3] = {{23,4,3},{45,4,3},{4,4,6}};
    print_Matrix(a, 3, 3);
    int b[3][2] = {{43,34},{4,56},{1,2}};
    print_Matrix(b, 3, 2);
    

   srand(time(NULL));

    int **a=(int**)malloc(3*sizeof(int*));
    for (int i=0;i<3;++i){
        a[i] = (int*)malloc(3*sizeof(int));
    }
    random_Matrix(a, 3, 3);
    print_Matrix(a, 3, 3);
    int **b=(int**)malloc(3*sizeof(int*));
    for (int i=0;i<3;++i){
        b[i] = (int*)malloc(2*sizeof(int));
    }
    random_Matrix(b, 3, 2);
    print_Matrix(b, 3, 2);

    int **result = matrix_Multi(a, 3, 3, b, 3, 2);

    printf("Matrix A Multi Matrix B:\n");
    print_Matrix(result, 3, 2);

    return 0;
}
*/

/*************     Test Functions     ************/
int sum(int a, int b){
    return a+ b;
}

int minus(int a, int b){
    return a-b;
}

int mul(int a, int b){
    return a*b;
}

int div_(int a, int b){
    return a/b;
}

int mod(int a, int b){
    return a%b;
}


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

    int i, j, row, col;

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

void sortArray(int *a, int n){
    if (n<2) return;
    int temp;
    for (int i=0;i<n-1;++i){
        for (int j=i+1;j<n;++j){
            if (a[i]>a[j]){
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
}

void printArray(int *a, int n){
    for (int i=0;i<n;++i){
        printf("%d\t", a[i]);
    }
    printf("\n");
}

void randomArray(int *a, int n){
    srand(time(NULL));
    for (int i=0;i<n;++i){
        a[i] = rand()%MAX_NUMBER;
    }
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

    int i, j, row, col;

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