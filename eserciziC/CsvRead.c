/*
author: Prandi Alessandro
date:
es.
testo
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define DIM_RIGA 200
#define NUM_RIGHE 20000

typedef struct {
    int numero;
    char *titolo;
    char *genere;
    int anno;
    char *disp;
}film;

int main() {
    char nomefile[] = "listafilm.csv";
    char buffer[DIM_RIGA];
    FILE *fp;
    char *campo;
    film Lista[NUM_RIGHE];
    int cont = 0;

    fp = fopen(nomefile,"r");
    if(fp == NULL) {
        printf("il file %s non esiste\n", nomefile);
        exit(1);
    }
    while(fgets(buffer,DIM_RIGA, fp)) {

        campo = strtok(buffer, ",");
        Lista[cont].numero = atoi(campo);
        //atoi int atof float
        campo = strtok(NULL, ",");
        Lista[cont].titolo = strdup(campo);

        campo = strtok(NULL, ",");
        Lista[cont].genere = strdup(campo);

        campo = strtok(NULL, ",");
        Lista[cont].anno = atoi(campo);

        campo = strtok(NULL, ",");
        Lista[cont].disp = strdup(campo);
        cont++;
    }
    printf("Lista dei film: \n");
    for(int k=0; k<cont; k++) {
        printf("%d %s %s %d %s \n",Lista[k].numero,Lista[k].titolo,Lista[k].genere,Lista[k].anno,Lista[k].disp);
    }
    return 0;
}
