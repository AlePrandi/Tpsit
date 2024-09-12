#include <stdio.h>
#include <stdlib.h>
#define DIM 5

void scambio(int *n1, int *n2)
{
    int z;
    z = *n1;
    *n1 = *n2;
    *n2 = z;
}

void selectionSort(int v[], int n)
{

    int k, kmin, j;
    for (k = 0; k < n - 1; k++)
    {
        kmin = k;
        for (j = k + 1; j < n; j++)
        {
            if (*(v + kmin) > *(v + j)) // confronti
                kmin = j;
        }
        if (kmin != k)
            scambio((v + k), (v + kmin)); // scambi
    }
    return;
}

void caricaVett(int vett[], int dim)
{
    for (int *i = vett; i < vett + dim; i++)
    {
        printf("inserisci un elemento: ");
        scanf("%d", i);
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
    selectionSort(vett, DIM);
    StampaVett(vett, DIM);
    return 0;
}