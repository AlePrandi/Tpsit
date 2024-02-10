#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct node
{
    char *codice;
    float peso;
    float tara;
    struct node *next;
} Node;

int is_empty(Node *head)
{
    return (head == NULL) ? 1 : 0;
}

void push(Node **head, Node *element)
{
    if (is_empty(*head))
    {
        *head = element;
        element->next = NULL;
    }
    else
    {
        element->next = *head;
        *head = element;
    }
}

Node *pop(Node **head)
{
    Node *ret = *head;
    if (is_empty(*head))
    {
        return NULL;
    }
    else
    {
        *head = ret->next;
    }
    return ret;
}

void stampaPila(Node* head){
    Node* p = head;
    while(p!=NULL){
        printf("\nCodice: %s ",p->codice);
        printf("\nPeso: %.2f", p->peso);
        printf("\nTara: %.2f", p->tara);
        p=p->next;
    }
}

int main(){
    Node* head = NULL;
    Node * container1 = (Node*)malloc(sizeof(Node));
    Node * container2 = (Node*)malloc(sizeof(Node));
    Node * container3 = (Node*)malloc(sizeof(Node));
    Node * container4 = (Node*)malloc(sizeof(Node));

    container1->codice = "a1";
    container1->peso = 2000;
    container1->tara = 300;
    container1->next = NULL;
    container2->codice = "a2";
    container2->peso = 2123;
    container2->tara = 300;
    container2->next = NULL;
    container3->codice = "a3";
    container3->peso = 2876;
    container3->tara = 300;
    container3->next = NULL;
    container4->codice = "a4";
    container4->peso = 2345;
    container4->tara = 300;
    container4->next = NULL;
    
    push(&head, container1);
    push(&head, container2);
    push(&head, container3);
    push(&head, container4);
    stampaPila(head);
}
