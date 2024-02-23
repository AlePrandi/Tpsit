#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node {
    int dato;
    struct node* next;
} Node;

void push(Node** head, Node* element) {
    if (*head == NULL) {
        *head = element;
        element->next = NULL;
    } else {
        element->next = *head;
        *head = element;
    }
}

Node* pop(Node** head) {
    Node* ret = *head;
    if (*head == NULL) {
        return NULL;
    } else {
        *head = ret->next;
    }
    return ret;
}

bool is_empty(Node* head) {
    return head == NULL;
}

void enqueue(Node** head, Node** tail, Node* elem){
    if(is_empty(*head)){
        *head = elem;
    }
    else{
        (*tail)->next = elem;
    }
    *tail = elem;
    elem->next = NULL;
}

Node* dequeue(Node** head, Node** tail) {
    if (is_empty(*head)) {
        printf("Errore: coda vuota.\n");
        return NULL;
    }

    Node* ret = (*head);
    (*head) = (*head)->next;

    if ((*head) == NULL) {
        free(*head);
        *head = *tail = NULL;
    }

    return ret;
}

int equal(Node* coda1, Node* coda2) {
    Node* nodo1 = coda1;
    Node* nodo2 = coda2;

    while (nodo1 != NULL && nodo2 != NULL) {
        if (nodo1->dato != nodo2->dato)
            return 0;
        nodo1 = nodo1->next;
        nodo2 = nodo2->next;
    }

    return nodo1 == NULL && nodo2 == NULL;
}

void rimuoviTutti(Node* head) {
    while (head != NULL) {
        Node* temp = head;
        head = head->next;
        free(temp);
    }
    free(head);
}

int main() {
    Node* Pila = (Node*) malloc(sizeof(Node));
    Node* coda1 = NULL;
    Node* coda2 = NULL;
    Node* tail1 = NULL;
    Node* tail2 = NULL;
    Node* node1 = (Node*) malloc(sizeof(Node));
    Node* node2 = (Node*) malloc(sizeof(Node));
    Node* node3 = (Node*) malloc(sizeof(Node));
    Node* node4 = (Node*) malloc(sizeof(Node));

    node1->dato = 1;
    node2->dato = 2;
    node3->dato = 3;
    node4->dato = 4;

    push(Pila, node1);
    enqueue(&coda1, &tail1, node1);
    enqueue(&coda1, &tail1, node2);
    Node* el = pop(Pila);

    printf("Elemento rimosso dalla pila: %d\n", el->dato);
    enqueue(&coda2, &tail2, node3);
    enqueue(&coda2, &tail2, node4);

    if (equal(coda1, coda2)) {
        printf("Le code sono uguali\n");
    } else {
        printf("Le code non sono uguali\n");
    }

    Node* rimosso = dequeue(&coda1, &tail1);
    if (rimosso != NULL) {
        printf("Elemento estratto dalla prima coda: %d\n", rimosso->dato);
        free(rimosso);
    }

    rimuoviTutti(coda1);
    rimuoviTutti(coda2);

    return 0;
}
