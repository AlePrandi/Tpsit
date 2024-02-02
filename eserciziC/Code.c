/*
è una struttura dati lineare, una sequenza di nodi ma è di tipo FIFO a differenza della pila
Le code FIFO sono molto usate ad esempio nei buffer nello streaming, servono per salvare i comandi in ordini
bisogna memorizzare sia la HEAD che la TAIL le funzioni base sono ENQUEUE e una DEQUEUE, le push e pop delle code
l'aggiunta si fa dalla TAIL mentre la rimozione si fa dalla HEAD

Es.3 Gestione di una Coda di Persone

È richiesto di creare un programma in linguaggio C che gestisca una coda di persone.
Ogni persona è rappresentata da un elemento che contiene le seguenti informazioni:

- Nome
- Cognome
- Età

Il programma dovrà eseguire le seguenti operazioni:

1. Inserimento nella coda: Implementare una funzione chiamata “inserisciInCoda”
che consenta l'inserimento di una persona nella coda. La funzione chiederà
all'utente di inserire il nome, cognome ed età della persona e successivamente inserirà l'elemento nella coda.

2. Visualizzazione della coda: Implementare una funzione chiamata “visualizzaCoda” che
stampi a video le informazioni di tutte le persone presenti nella coda. Se la coda è vuota,
verrà stampato un messaggio adeguato.

3. Rimozione dalla coda: Implementare una funzione chiamata “rimuoviDallaCoda”
che rimuova la persona più anziana presente nella coda. Nel caso in cui ci siano persone
con la stessa età massima, verrà rimossa la prima persona inserita con quell'età.

4. Uscita dal programma: Implementare una funzione chiamata “uscitaProgramma”
che liberi la memoria allocata per la coda e termini il programma.
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct persona{
    char* nome;
    char* cognome;
    int eta;
    struct persona* next;
}Persona;

bool is_empty(Persona* head){
    return head == NULL;
}

void enqueue(Persona** head, Persona** tail, Persona* elem){
    if(is_empty(*head)){
        *head = elem;
    }
    else{
        (*tail)->next = elem;
    }
    *tail = elem;
    elem->next = NULL;
}

Persona* dequeue(Persona** head, Persona** tail){
    Persona* ret = *head;
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

int calcolaLunghezza(Persona* head){
    Persona* h = head;
    int lung = 0;
    while (h != NULL)
    {
        lung++;
        h = h->next;
    }
    return lung; 
}

void stampaCoda(Persona* head){
    Persona* l = head;
    while (l != NULL)
    {
        printf("\n%s ", l->cognome);
        printf("\n%s ", l->nome);
        printf("\n%d\n ", l->eta);
        l = l ->next;
    }
}

void rimuoviTutti(Persona** head, Persona** tail){
    Persona* corrente =  *head;
    Persona* next;
    while(corrente != NULL){
        next=corrente->next;
        free(corrente);
        corrente=next;
    }
    *head=NULL;
    *tail=NULL;
}

int main() {
    Persona* head = (Persona*)malloc(sizeof(Persona));
    Persona* tail = (Persona*)malloc(sizeof(Persona));

    head = NULL;
    tail = NULL;

    Persona* elemento = (Persona*)malloc(sizeof(Persona));

    elemento->cognome = "Bianchi";
    elemento->nome = "Andrea";
    elemento->eta = 18;
    elemento->next = NULL;

    enqueue(&head, &tail, elemento);

    Persona* elemento2 = (Persona*)malloc(sizeof(Persona));

    elemento2->cognome = "Rossi";
    elemento2->nome = "Mario";
    elemento2->eta = 16;
    elemento2->next = NULL;

    enqueue(&head, &tail, elemento2);

    stampaCoda(head);
    printf("\nDimensione della coda: %d", calcolaLunghezza(head));

    Persona* temp = dequeue(&head, &tail);
    printf("\n%s", temp->cognome);

    stampaCoda(head);
    printf("\nDimensione della coda: %d", calcolaLunghezza(head));

    rimuoviTutti(&head, &tail);
    Persona* temp1 = dequeue(&head, &tail);

    free(elemento);
    free(elemento2);
    return 0;
}