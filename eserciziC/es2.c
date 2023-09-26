#include <stdio.h>
#include <stdlib.h>

int main(){
    int a = 5;
    int b;
    int* pi;
    pi = &a;
    b =  *pi;

    printf("%d",b);
    return 0;
}