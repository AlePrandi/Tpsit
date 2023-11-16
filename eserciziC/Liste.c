#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int valore;
    struct node *next;
} Node;

/*
int numeroElementi(Node *head){
    int cont = 0;
    Node *l = head;
    while (l != NULL){
        cont++;
        l = l->next;
    }
    return cont;
}
*/

int numeroElementi(Node *head){
    int cont = 0;
    Node *l = head;
    if (l == NULL){
        return cont;
    }else{
        cont++;
        return numeroElementi(l);  
    }
}


int main()
{
    int n;
    int cont;
    Node *lista = NULL;
    Node *l;

    do
    {
        printf("Inserisci un numero (-1 per terminare): ");
        scanf("%d", &n);
        if (n >= 0)
        {
            if (lista == NULL)
            {
                lista = (Node *)malloc(sizeof(Node));
                l = lista;
            }
            else
            {
                l->next = (Node *)malloc(sizeof(Node));
                l = l->next;
            }
            l->valore = n;
            l->next = NULL;
        }
    } while (n >= 0);
    cont = numeroElementi(lista);
    l = lista;
    printf("Numeri inseriti: \n");
    while (l != NULL)
    {
        printf("%d - %p \n", l->valore, l->next);
        l = l->next;
    }
    printf("Numero di elemnti: %d ", cont);
    return 0;
}