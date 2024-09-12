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

void swap(int *n1, int *n2)
{
    int z;
    z = *n1;
    *n1 = *n2;
    *n2 = z;
}

void bubbleSort(int vett[], int dim)
{
    int k, sup, sca;
    sup = dim - 1;
    while (sup > 0)
    {
        sca = 0;
        for (k = 0; k < sup; k++)
        {
            if (*(vett + k) > *(vett + k + 1))
            {
                swap((vett + k), (vett + k + 1));
                sca = k;
            }
        }
        sup = sca;
    }
}

void caricaVett(int vett[], int dim)
{
    for (int k = 0; k < dim; k++)
    {
        printf("inserisci un elemento in posizione %d: ", k);
        scanf("%d", (vett + k));
    }
}

void StampaVett(int vett[], int dim)
{
    for (int i = 0; i < dim; i++)
    {
        printf("%d \n", *(vett + i));
    }
}

int main()
{
    int vett[DIM];
    caricaVett(vett, DIM);
    bubbleSort(vett, DIM);
    StampaVett(vett, DIM);
    return 0;
}