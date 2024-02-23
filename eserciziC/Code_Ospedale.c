#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct paziente {
    char* nome;
    int eta;
    char* colore;
    struct paziente* next;
} Paziente;

typedef struct pronto_soccorso {
    Paziente* head[4];
    Paziente* tail[4]; // rosso, giallo, verde, bianco
} ProntoSoccorso;

bool is_empty(Paziente* head) {
    return head == NULL;
}

void enqueue(Paziente** head, Paziente** tail, Paziente* elem) {
    if (is_empty(*head)) {
        *head = elem;
    }
    else {
        (*tail)->next = elem;
    }
    *tail = elem;
    elem->next = NULL;
}

Paziente* dequeue(Paziente** head, Paziente** tail) {
    Paziente* ret = *head;
    if (is_empty(*head)) {
        printf("\nErrore coda vuota");
        return NULL;
    }
    else {
        *head = ret->next;
    }
    if (*head == NULL) {
        *tail = NULL;
    }
    return ret;
}

void stampaPazienti(ProntoSoccorso* ps) {
    for (int i = 0; i < 4; i++) {
        Paziente* current = ps->head[i];
        while (current != NULL) {
            printf("Nome: %s, Eta: %d, Colore: %s\n", current->nome, current->eta, current->colore);
            current = current->next;
        }
    }
}

int main() {
    ProntoSoccorso pronto_soccorso = { { NULL, NULL, NULL, NULL } };

    Paziente* paziente1 = (Paziente*)malloc(sizeof(Paziente));
    paziente1->nome = "Mario Rossi";
    paziente1->colore = "rosso";
    paziente1->eta = 40;
    paziente1->next = NULL;
    enqueue(&pronto_soccorso.head[0], &pronto_soccorso.tail[0], paziente1);

    Paziente* paziente2 = (Paziente*)malloc(sizeof(Paziente));
    paziente2->nome = "Luigi Verdi";
    paziente2->colore = "rosso";
    paziente2->eta = 35;
    paziente2->next = NULL;
    enqueue(&pronto_soccorso.head[0], &pronto_soccorso.tail[0], paziente2);

    Paziente* paziente3 = (Paziente*)malloc(sizeof(Paziente));
    paziente3->nome = "Giovanni Bianchi";
    paziente3->colore = "verde";
    paziente3->eta = 50;
    paziente3->next = NULL;
    enqueue(&pronto_soccorso.head[2], &pronto_soccorso.tail[2], paziente3);

    Paziente* paziente4 = (Paziente*)malloc(sizeof(Paziente));
    paziente4->nome = "Maria Neri";
    paziente4->colore = "bianco";
    paziente4->eta = 60;
    paziente4->next = NULL;
    enqueue(&pronto_soccorso.head[3], &pronto_soccorso.tail[3], paziente4);

    printf("Gestione dei pazienti:\n");
    stampaPazienti(&pronto_soccorso);

    for (int i = 0; i < 4; i++) {
        Paziente* current = pronto_soccorso.head[i];
        while (current != NULL) {
            Paziente* temp = current;
            current = current->next;
            free(temp);
        }
    }

    return 0;
}
