/*
author: Prandi Alessandro
date:
es.
testo
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 200
#define N_FILM 30

typedef struct {
    int posizione;
    char titolo[MAX];
    char genere[MAX];
    int anno;
    char disponibil[MAX];
} Film;

void CaricaLista(Film Lista[]) {
    char Nomefile[MAX] = "listafilm.csv";
    FILE *fp = fopen(Nomefile,"r");
    char riga[MAX];
    char *tok;
    int k = 0;
    while(fgets(riga,MAX,fp)!= NULL) {
        tok=strtok(riga,",");
        Lista[k].posizione=atoi(tok);//atoi int atof float
        tok=strtok(NULL,",");
        strcpy(Lista[k].titolo,tok);
        tok=strtok(NULL,",");
        strcpy(Lista[k].genere,tok);
        tok=strtok(NULL,",");
        Lista[k].anno=atoi(tok);
        tok=strtok(NULL,",");
        strcpy(Lista[k].disponibil,tok);
        k++;
    }
    fclose(fp);
}

int main() {
    Film Lista[N_FILM];
    CaricaLista(Lista);
    printf("Lista dei film: \n");
for(int k=0;k<N_FILM;k++){
        printf("%d %s %s %d %s \n",Lista[k].posizione,Lista[k].titolo,Lista[k].genere,Lista[k].anno,Lista[k].disponibil);
    }

    return 0;
}
