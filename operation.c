
#ifndef __OPERATION_H__
#define __OPERATION_H__

int sum(int a, int b);
int minus(int a, int b);
int mul(int a, int b);
int div_(int a, int b);
int mod(int a, int b);

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

#endif