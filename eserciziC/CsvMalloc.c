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

void CaricaFile(char *nomefile, film Lista[])
{
    char *campo;
    int cont = 0;
    FILE *fp;
    fp = fopen(nomefile, "r");
    char buffer[DIM_RIGA];
    if (fp == NULL)
    {
        printf("il file %s non esiste\n", nomefile);
        exit(1);
    }
    while (fgets(buffer, DIM_RIGA, fp))
    {

        campo = strtok(buffer, ",");
        (Lista + cont)->numero = atoi(campo);
        //(*(Lista + cont)).numero = atoi(campo);
        // atoi int atof float
        campo = strtok(NULL, ",");
        (Lista + cont)->titolo = strdup(campo);

        campo = strtok(NULL, ",");
        (Lista + cont)->genere = strdup(campo);

        campo = strtok(NULL, ",");
        (Lista + cont)->anno = atoi(campo);

        campo = strtok(NULL, ",");
        (Lista + cont)->disp = strdup(campo);
        cont++;
    }
    fclose(fp);
}

int main()
{
    char nomefile[] = "listafilm.csv";
    char buffer[DIM_RIGA];
    FILE *fp;
    char *campo;
    film *list;
    list = (film *) malloc (leggiRighe(nomefile) * sizeof(film));
    int anno = 0;

    fp = fopen(nomefile, "r");

    CaricaFile(nomefile, list);

    printf("inserisci un anno del film: ");
    scanf("%d", &anno);
    printf("I film in questo anno sono: \n");
    for (film *k = list; k < list + leggiRighe(nomefile); k++)
    {
        if (anno == k->anno)
        {
            printf("%s \n", k->titolo);
        }
    }

    return 0;
}