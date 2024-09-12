#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    char val;
    struct node* next;
} Node;

int is_empty(Node* head) {
    return (head == NULL) ? 1 : 0;
}

void push(Node**head, Node*element){
    if(is_empty(*head)){
        *head = element;
        element->next=NULL;
    }else{
        element->next=*head;
        *head = element;
    }
}

Node* pop(Node**head){
    Node * ret = *head;
    if(is_empty(*head)){
        return NULL;
    }else{
        *head = ret->next;
    }
    return ret;
}

void stampaPila(Node* head) {
    Node* p = head;
    while (p != NULL) {
        printf("%c ", p->val);
        p = p->next;
    }
}

int main() {
    char stringa[] = "{1 + [2 + 3]) * 5}";
    char dizionario[3][2] = { {'{', '}'}, {'[', ']'}, {'(', ')'} };
    char par_ap[] = { '{', '[', '(' };
    char par_ch[] = { '}', ']', ')' };
    Node* pila = NULL;
    int pos = -1;
    int errore = 0;

    for (int k = 0; stringa[k] != NULL; k++) {
        Node* element = (Node*) malloc(sizeof(Node));
        element->val = stringa[k];
        for (int i = 0; i < 3; i++) {
            if (element->val == par_ap[i]) {
                push(&pila, element);
            }
            if (element->val == par_ch[i]) {
                char parentesi = pop(&pila);
                if (parentesi == NULL || dizionario[i][0] != parentesi) {
                    pos = k;
                    errore = 1;
                    break;
                }
            }
        }
    }

    if (errore) {
        printf("Errore in posizione %d !!\n", pos);
    } else {
        printf("Corretto!!\n");
    }

    return 0;
}
