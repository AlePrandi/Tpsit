#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct El
{
    int dato;
    struct El *next;
} Elemento;

int calcolaLung(Elemento *lista)
{
    Elemento *l = lista;
    int lung = 0;
    while (l != NULL)
    {
        lung++;
        l = l->next;
    }
    return lung;
}

int somma(Elemento *head, int M)
{
    if (head == NULL)
    {
        return -1;
    }

    int somma_M = 0;
    Elemento *l = head;

    while (l != NULL)
    {
        if (l->dato % M == 0)
        {
            somma_M += l->dato;
        }
        l = l->next;
    }

    return somma_M;
}

int main()
{
    int n, num;
    int lung = 0;
    Elemento *lista = NULL;
    Elemento *l;
    do
    {
        printf("inserire un numero naturale o -1 per terminare: ");
        scanf("%d", &n);
        if (n >= 0)
        {
            if (lista == NULL)
            {
                lista = (Elemento *)malloc(sizeof(Elemento));
                l = lista;
            }
            else
            {
                l->next = (Elemento *)malloc(sizeof(Elemento));
                l = l->next;
            }
            l->dato = n;
            l->next = NULL;
        }
    } while (n >= 0);

    l = lista;
    printf("numeri inseriti: ");
    printf("\n");
    while (l != NULL)
    {
        printf("%d - %p \n", l->dato, l->next);
        l = l->next;
    }

    printf("Inserisci un numero da cercare i multipli: ");
    scanf("%d", &num);
    int somM = somma(lista, num);
    printf("La somma e: %d", somM);
    free(lista);
    return 0;
}