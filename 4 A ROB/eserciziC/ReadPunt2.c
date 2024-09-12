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

typedef struct
{
    int numero;
    char *titolo;
    char *genere;
    int anno;
    char *disp;
} film;

int main()
{
    char nomefile[] = "listafilm.csv";
    char buffer[DIM_RIGA];
    FILE *fp;
    char *campo;
    film Lista[NUM_RIGHE];
    int cont = 0;
    int anno = 0;
    film *k = Lista;

    fp = fopen(nomefile, "r");
    if (fp == NULL)
    {
        printf("il file %s non esiste\n", nomefile);
        exit(1);
    }
    while (fgets(buffer, DIM_RIGA, fp))
    {

        campo = strtok(buffer, ",");
        k->numero = atoi(campo);  
        //(*(Lista + cont)).numero = atoi(campo); 
        // atoi int atof float
        campo = strtok(NULL, ",");
        k->titolo = strdup(campo);

        campo = strtok(NULL, ",");
        k->genere = strdup(campo);

        campo = strtok(NULL, ",");
        k->anno = atoi(campo);

        campo = strtok(NULL, ",");
        k->disp = strdup(campo);
        cont++;
        k = Lista + cont;
    }
    /*
        printf("Lista dei film: \n");
        for (int k = 0; k < cont; k++)
        {
            printf("%d %s %s %d %s \n", Lista[k].numero, Lista[k].titolo, Lista[k].genere, Lista[k].anno, Lista[k].disp);
        }
    */
    printf("inserisci un anno del film: ");
    scanf("%d", &anno);
    printf("I film in questo anno sono: \n");
    for (film *k = Lista; k < Lista + cont; k++)
    {
        if (anno == k->anno)
        {
            printf("%s \n", k->titolo);
        }
    }
    return 0;
}