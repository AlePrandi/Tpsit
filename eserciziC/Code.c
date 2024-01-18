/*
è una struttura dati lineare, una sequenza di nodi ma è di tipo FIFO a differenza della pila
Le code FIFO sono molto usate ad esempio nei buffer nello streaming, servono per salvare i comandi in ordini
bisogna memorizzare sia la HEAD che la TAIL le funzioni base sono ENQUEUE e una DEQUEUE, le push e pop delle code
l'aggiunta si fa dalla TAIL mentre la rimozione si fa dalla HEAD
*/
#include <stdio.h>
#include <stdlib.h>

void enqueue(struct queue_node **head, struct queue_node **tail, struct queue_node *element)
{
    if (head == NULL)
    {
        *head = element;
    }
    else
    {
        //(*tail)->next = element;
    }
    *tail = element;
    //element->next = NULL;
}