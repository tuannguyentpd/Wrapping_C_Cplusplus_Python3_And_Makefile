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


#ifndef __ARRAY_H__
#define __ARRAY_H__

void sortArray(int *a, int n);
void printArray(int *a, int n);
void randomArray(int *a, int n);

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

#endif