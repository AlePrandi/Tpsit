#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct node
{
    char c;
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

bool e_pali(char *stringa)
{
    Node *pila = NULL;
    int len = strlen(stringa);

    if (len % 2 == 0)
    {
        for (int i = 0; i < len / 2; i++)
        {
            Node *node = (Node *)malloc(sizeof(Node));
            node->c = stringa[i];
            node->next = pila;
            push(&pila, node);
        }

        for (int i = len / 2; i < len; i++)
        {
            if (is_empty(pila) || pila->c != stringa[i])
            {
                return false;
            }
            Node *node = pop(&pila);
            free(node);
        }
    }
    else
    {
        for (int i = 0; i < len / 2 ; i++)
        {
            Node *node = (Node *)malloc(sizeof(Node));
            node->c = stringa[i];
            node->next = pila;
            push(&pila, node);
        }

        for (int i = len / 2 + 1; i < len; i++)
        {
            if (is_empty(pila) || pila->c != stringa[i])
            {
                return false;
            }
            Node *node = pop(&pila);
            free(node);
        }
    }

    return true;
}

int main()
{
    char *stringa = (char *)malloc(sizeof(char));
    printf("Inserire una stringa: ");
    fflush(stdin);
    scanf("%s", stringa);

    if (e_pali(stringa))
    {
        printf("La stringa %s e' palindroma.\n", stringa);
    }
    else
    {
        printf("La stringa %s non e' palindroma.\n", stringa);
    }

    return 0;
}