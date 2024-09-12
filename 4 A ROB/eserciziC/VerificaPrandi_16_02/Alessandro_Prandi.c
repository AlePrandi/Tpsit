#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

typedef struct pila
{
    int num_arrivo;
    int valore;
    struct pila *next;
} Pila;

typedef struct coda
{
    int num_arrivo;
    int valore;
    struct coda*next;
} Coda;

bool is_emptyPila(Pila *head)
{
    return head == NULL;
}

void push(Pila**head, Pila*element){
    if(is_emptyPila(*head)){
        *head = element;
        element->next=NULL; 
    }else{
        element->next=*head;
        *head = element;
    }
}



bool is_emptyCoda(Coda *head)
{
    return head == NULL;
}


Pila* pop(Pila**head){
    Pila * ret = *head;
    if(is_emptyPila(*head)){
        return NULL;
    }else{
        *head = ret->next;
    }
    return ret;
}

void stampaPila(Pila* head){
    Pila* p = head;
    printf("Pila: \n");
    while(p!=NULL){
        printf("Valore: %d  ",p->valore);
        printf("Num_Arrivo: %d",p->num_arrivo);
        printf("\n");
        p=p->next;
    }
}

void enqueue(Coda **head, Coda **tail, Coda *elem)
{
    if (is_emptyCoda(*head))
    {
        *head = elem;
    }
    else
    {
        (*tail)->next = elem;
    }
    *tail = elem;
    elem->next = NULL;
}

Coda *dequeue(Coda **head, Coda **tail)
{
    Coda *ret = *head;
    if (is_emptyCoda(*head))
    {
        printf("\nErrore coda vuota");
        return NULL;
    }
    else
    {
        *head = ret->next;
    }
    if (*head == NULL)
    {
        *tail = NULL;
    }
    return ret;
}

void stampaCoda(Coda* head){
    Coda* l = head;
    printf("Coda: \n");
    while (l != NULL)
    {
        printf("Valore: %d ", l->valore);
        printf("Num_Arrivo: %d \n", l->num_arrivo);
        l = l ->next;
    }
}

int main(){
    int n_pila;
    int n_coda;
    srand(time(NULL));
    Pila* pila = NULL;
    Coda* head = (Coda *) malloc(sizeof(Coda));
    Coda* tail = (Coda *) malloc(sizeof(Coda));

    head = NULL;
    tail = NULL;
    for(int i=0;i < 5;i++){

        n_pila = 1  + rand() % 10;
        n_coda = 1  + rand() % 10;

        Pila * el_pila = (Pila*)malloc(sizeof(Pila));
        Coda * el_coda = (Coda*)malloc(sizeof(Coda));

        el_pila->valore = n_pila;
        el_pila->num_arrivo = i + 1;
        el_pila->next = NULL;

        el_coda->valore = n_coda;
        el_coda->num_arrivo = i + 1;
        el_coda->next = NULL;
        push(&pila, el_pila);
        enqueue(&head, &tail, el_coda);
    }

    stampaPila(pila);
    stampaCoda(head);

    Pila* p = pila;
    Coda* h = head;
    Coda* t = tail;

    while(p->next != NULL || h->next != NULL){
        Pila *temp_pila = pop(&p);
        Coda *temp_coda = dequeue(&h, &tail);

        printf("Num arrivo: %d\n", temp_pila->num_arrivo);
        printf("Valore: %d \n", temp_pila->valore);
        printf("Num arrivo: %d\n", temp_coda->num_arrivo);
        printf("Valore: %d \n", temp_coda->valore);

        if(temp_coda->valore > temp_pila->valore){
            temp_coda->valore -= temp_pila->valore;
            enqueue(&h, &t, temp_coda);
        }else{
            if(temp_pila->valore > temp_coda->valore){
                temp_pila->valore -= temp_coda->valore;
                push(&p, temp_pila);
            }else{
                free(temp_coda);
                free(temp_pila);
            }
        }
    }if(p->next == NULL){
        printf("\n");
        printf("Ha vinto la Coda \n");
        stampaCoda(h);
    }else{
        printf("\n");
        printf("Ha vinto la Pila \n");
        stampaPila(p);
    }
}