#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int valore;
    struct node *next;
}Node;

int main(){
    int n;
    Node *lista = NULL;
    Node *l;

    do{
        printf("Inserisci un numero (-1 per terminare): ");
        scanf("%d",&n);
        if(n >= 0){
            if (lista == NULL){
                lista = (Node *) malloc(sizeof(Node));
                l = lista;
            }else{
                l->next = (Node *) malloc(sizeof(Node));
                l = l->next;
            }
            l->valore = n;
            l->next = NULL;
        }
    }while(n >= 0);

    l = lista;
    printf("Numeri inseriti: \n");
    while( l != NULL){
        printf("%d - %p \n", l->valore, l->next);
        l= l->next;
    }
    return 0;
}