/*
fare una pila in cui caricati gli elementi si riordinano in modo da stampare prima i pari e poi i dispari
*/

/*
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
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct sequenza
{
    int valore;
    struct sequenza *next;
} Sequenza;

bool is_empty(Sequenza *head)
{
    return head == NULL;
}

void enqueue(Sequenza **head, Sequenza **tail, Sequenza *elem)
{
    if (is_empty(*head))
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

Sequenza *dequeue(Sequenza **head, Sequenza **tail)
{
    Sequenza *ret = *head;
    if (is_empty(*head))
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

void stampaCoda(Sequenza *head)
{
    Sequenza *l = head;
    while (l != NULL)
    {
        if (l->next != NULL)
            printf("%d, ", l->valore);
        else        
            printf("%d\n", l->valore);
            
        l = l->next;
    }
}

int main()
{
    int num;

    Sequenza *headPari = NULL;
    Sequenza *headDispari = NULL;

    Sequenza *tailPari = NULL;
    Sequenza *tailDispari = NULL;

    do
    {
        printf("inserire un numero: ");
        scanf("%d", &num);
        if (num > 0)
        {
            if (num % 2 == 0)
            {
                Sequenza *element = (Sequenza *)malloc(sizeof(Sequenza));
                element->valore = num;
                enqueue(&headPari, &tailPari, element);
            }
            else
            {
                Sequenza *element = (Sequenza *)malloc(sizeof(Sequenza));
                element->valore = num;
                enqueue(&headDispari, &tailDispari, element);
            }
        }
    } while (num > 0);
    stampaCoda(headPari);
    stampaCoda(headDispari);
    return 0;
}