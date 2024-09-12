#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void caricaVett(int *vett, int dim)
{
    for (int *k = vett; k < vett + dim; k++)
    {
        printf("inserisci un elemento: ");
        scanf("%d", k);
    }
}

int ChiediDim()
{
    int val;
    do
    {
        printf("inserisci una dimensione per il vettore: ");
        scanf("%d", &val);
    } while (val < 0);
    return val;
}

void StampaVett(int *vett, int dim)
{
    for (int *i = vett; i < vett + dim; i++)
    {
        printf("%d \n", *i);
    }
}

int main()
{

    int *vett;
    int dim = ChiediDim();
    vett = (int *)malloc(dim * sizeof(int));
    caricaVett(vett, dim);
    StampaVett(vett, dim);

    free(vett);

    return 0;
}