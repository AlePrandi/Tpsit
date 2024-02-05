#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct film{
    char* titolo;
    char* genere;
    int anno;
    struct film* next;
}Film;

bool is_empty(Film* head){
    return head == NULL;
}

void enqueue(Film** head, Film** tail, Film* elem){
    if(is_empty(*head)){
        *head = elem;
    }
    else{
        (*tail)->next = elem;
    }
    *tail = elem;
    elem->next = NULL;
}

Film* dequeue(Film** head, Film** tail){
    Film* ret = *head;
    if(is_empty(*head)){
        printf("\nErrore coda vuota");
        return NULL;
    }
    else{
        *head = ret->next;
    }
    if(*head == NULL){
        *tail = NULL;
    }
    return ret;
}

int calcolaLunghezza(Film* head){
    Film* h = head;
    int lung = 0;
    while (h != NULL)
    {
        lung++;
        h = h->next;
    }
    return lung; 
}

void stampaCoda(Film* head){
    Film* l = head;
    while (l != NULL)
    {
        printf("\n%s ", l->genere);
        printf("\n%s ", l->titolo);
        printf("\n%d\n ", l->anno);
        l = l ->next;
    }
}

void rimuoviTutti(Film** head, Film** tail){
    Film* corrente =  *head;
    Film* next;
    while(corrente != NULL){
        next=corrente->next;
        free(corrente);
        corrente=next;
    }
    *head=NULL;
    *tail=NULL;
}

int main() {
    Film* head = (Film*)malloc(sizeof(Film));
    Film* tail = (Film*)malloc(sizeof(Film));

    head = NULL;
    tail = NULL;

    Film* elemento = (Film*)malloc(sizeof(Film));

    elemento->genere = "Guerra";
    elemento->titolo = "Napoleon";
    elemento->anno = 2021;
    elemento->next = NULL;

    enqueue(&head, &tail, elemento);

    Film* elemento2 = (Film*)malloc(sizeof(Film));

    elemento2->genere = "Rossi";
    elemento2->titolo = "Mario";
    elemento2->anno = 16;
    elemento2->next = NULL;

    enqueue(&head, &tail, elemento2);

    stampaCoda(head);
    printf("\nDimensione della coda: %d", calcolaLunghezza(head));

    Film* temp = dequeue(&head, &tail);
    printf("\n%s", temp->genere);

    stampaCoda(head);
    printf("\nDimensione della coda: %d", calcolaLunghezza(head));

    rimuoviTutti(&head, &tail);
    Film* temp1 = dequeue(&head, &tail);

    free(elemento);
    free(elemento2);
    return 0;
}