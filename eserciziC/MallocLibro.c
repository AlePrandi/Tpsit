#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define DIM_RIGA 200
#define NUM_RIGHE 20000
#define MAX 100
/*
Scrivi un programma in linguaggio C che
gestisca un archivio di libri. Il programma deve utilizzare una struttura Libro per rappresentare ciascun libro, con le seguenti
informazioni:
-Titolo (massimo 100 caratteri)
-Autore (massimo 100 caratteri)
-Anno di pubblicazione
Il programma deve consentire all'utente
di eseguire le seguenti operazioni:
-Stampare l'archivio dei libri:
-Stampa tutte le informazioni sui libri presenti nell'archivio.
-Stampa l’archivio dei libri pubblicati in un certo anno.
-Stampa tutti i libri pubblicati in ordine di anno.
Assicurati che il programma gestisca
correttamente la memoria dinamica e che non ci siano perdite di memoria.
Inoltre, gestisci eventuali errori nell'apertura del file CSV.
Ricorda di fornire un'interfaccia utente
chiara e intuitiva per consentire all'utente di eseguire queste operazioni.
*/

typedef struct{
    int giorno;
    int mese;
    int anno;
}Data;

typedef struct{
    char Titolo[MAX];
    char Autore[MAX];
    Data pubbl;

}Libro;

int leggiRighe(char *nomefile)
{
    FILE *fp;
    int conta_righe = 0;
    char *riga;
    fp = fopen(nomefile, "r");
    while (fgets(riga, DIM_RIGA, fp))
    {
        conta_righe++;
    }
    fclose(fp);
    return conta_righe;
}