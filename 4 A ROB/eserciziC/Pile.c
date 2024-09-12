#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int val;
    struct node* next;
}Node;

int is_empty(Node*head){
    if(head==NULL)return 1;
    else return 0;
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

void stampaPila(Node* head){
    Node* p = head;
    while(p!=NULL){
        printf("%d ",p->val);
        p=p->next;
    }
}


int main(){
    int n;
    Node* head = NULL;
    do{
        printf("Inserisci un numero naturale o -1 per terminare: ");
        scanf("%d",&n);
        if(n>=0)
        {
            Node * element = (Node*)malloc(sizeof(Node));
            element->val = n;
            push(&head, element);
        }
        
    }while(n>=0);
    stampaPila(head);
    printf("Faccio una pop: ");
    Node*removed = pop(&head);
    printf("%d \n", removed->val);
    stampaPila(head);
    return 0;
}