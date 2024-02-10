/*
fare una pila in cui caricati gli elementi si riordinano in modo da stampare prima i pari e poi i dispari
*/

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct numero{
    int num;
    struct numero* next;
}Numero;

bool is_empty(Numero* head){
    return head == NULL;
}

void push(Numero **head, Numero *element){
    if(is_empty(*head)){
        *head = element;
        element->next = NULL;
    }
    else{
        element->next = *head;
        *head = element;
    }
}

Numero* pop(Numero **head){
    Numero* stack;
    if(is_empty(*head)){
        return NULL;
    }
    else{
        stack = *head;
        *head = stack->next;
    }
    return stack;
}

Numero* pila_pari_dispari(Numero* head){
    Numero* p;
    while(head->next != NULL){
        p = (Numero*)malloc(sizeof(Numero));
        if(head->num % 2 == 0)
            push(&p, head);
        head = head->next;
    }
    while(head->next != NULL){
        p = (Numero*)malloc(sizeof(Numero));
        if(head->num % 2 != 0)
            push(&p, head);
        head = head->next;
    }
    return p;
}

void print_stack(Numero* head){
    Numero* s = head;
    while(s != NULL){
        printf("%d", s->num);
        s = s->next;
    }
}

int main(){
    Numero* head;
    Numero* el;
    Numero* pila_finale;
    int n;
    do{
        head = (Numero*)malloc(sizeof(Numero));
        el = (Numero*)malloc(sizeof(Numero));
        printf("inserisci un numero: ");
        scanf("%d", &n);
        if (n >= 0){
            el->num = n;
            push(&head, el);
            head = head->next; 
        }
    }while(n >= 0);
    pila_finale = pila_pari_dispari(head);
    print_stack(pila_finale);
    free(head); free(el); free(pila_finale);
    return 0;
}