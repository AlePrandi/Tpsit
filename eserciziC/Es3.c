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
    for (int k = 0; k < dim; k++)
    {
        somma += *(vett + k);
    }

    return somma;
}

void caricaVett(int vett[], int dim)
{
    for (int k = 0; k < dim; k++)
    {
        printf("inserisci un elemento in posizione %d: ", k);
        scanf("%d", (vett + k));
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