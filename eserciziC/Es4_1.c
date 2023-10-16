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
#define DIM 5

void swap(int *n1, int *n2)
{
    int z;
    z = *n1;
    *n1 = *n2;
    *n2 = z;
}

void bubbleSort(int vett[], int dim)
{
    int *k, sup, sca, j;
    sup = dim - 1;
    while (sup > 0)
    {
        j = 0;
        sca = 0;
        for (k = vett; k < vett + sup; k++)
        {
            if ( *k > *(k + 1))
            {
                swap(k, (k + 1));
                sca = j;
            }
            j++;
        }
        sup = sca;
    }
}

void caricaVett(int vett[], int dim)
{
    for (int *k = vett; k < vett + dim; k++)
    {
        printf("inserisci un elemento: ");
        scanf("%d", k);
    }
}

void StampaVett(int vett[], int dim)
{
    for (int *i = vett; i < vett + dim; i++)
    {
        printf("%d \n", *i);
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