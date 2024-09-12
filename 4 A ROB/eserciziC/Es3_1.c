/*
author: Prandi Alessandro
date:
es.
testo
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define DIM 10

int calcolaSomma(int vett[], int dim)
{
    int somma = 0;
    for (int *k = vett; k < vett + dim; k++)
    {
        somma += *k;
    }

    return somma;
}

void caricaVett(int vett[], int dim)
{
    for (int *k = vett; k < vett + dim; k++)
    {
        printf("inserisci un elemento: ");
        scanf("%d", k);
    }
}

int main()
{
    int vett[DIM];
    int somma;

    caricaVett(vett, DIM);
    somma = calcolaSomma(vett, DIM);

    printf("la somma e': %d", somma);

    return 0;
}