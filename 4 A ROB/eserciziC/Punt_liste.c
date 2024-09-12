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

Elemento *primoPari(Elemento *l)
{
    while (l != NULL)
    {

        if (l->dato % 2 == 0)
            return l->next;
        else
            l = l->next;
    }
    return NULL;
}

int main()
{
    int n;
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

    Elemento *pos = primoPari(lista);
    printf("La prima posizione pari e: %p", pos);
    free(lista);
    return 0;
}