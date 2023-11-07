#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define DIM_RIGA 200
#define NUM_RIGHE 20000
#define MAX 100

typedef struct
{
    int giorno;
    int mese;
    int anno;
} Data;

typedef struct
{
    char *Titolo;
    char *Autore;
    Data *data;

} Libro;

void scambio(Libro *a, Libro *b)
{
    Libro num;
    num = *a;
    *a = *b;
    *b = num;
}

int leggiRighe(char *nomefile)
{
    FILE *fp;
    int conta_righe = 0;
    char *riga = (char *)malloc(DIM_RIGA * sizeof(char));
    fp = fopen(nomefile, "r");
    if (fp == NULL)
    {
        printf("Errore nell'apertura del file.\n");
        exit(1);
    }

    while (fgets(riga, DIM_RIGA, fp))
    {
        conta_righe++;
    }
    fclose(fp);
    free(riga);
    return conta_righe;
}

void stampaArc(Libro *elenco, int n)
{
    for (Libro *i = elenco; i < elenco + n; i++)
    {
        printf("TITOLO: %s AUTORE: %s ANNO: %d/%d/%d\n", i->Titolo, i->Autore, i->data->giorno, i->data->mese, i->data->anno);
    }
}

void stampaAnnata(Libro *elenco, int n)
{
    int anno;
    printf("Inserisci l'anno di pubblicazione che vuoi cercare: ");
    scanf("%d", &anno);
    for (Libro *i = elenco; i < elenco + n; i++)
    {
        if (i->data->anno == anno)
        {
            printf("TITOLO: %s AUTORE: %s ANNO: %d/%d/%d\n", i->Titolo, i->Autore, i->data->giorno, i->data->mese, i->data->anno);
        }
    }
}

void ordinaElenco(Libro *elenco, int cont)
{
    Libro *k;
    int sup, sca;
    sup = cont - 1;
    int j;
    while (sup >= 0)
    {
        j = 0;
        sca = -1;
        for (k = elenco; k < elenco + sup; k++)
        {
            if (k->data->anno > (k + 1)->data->anno)
            {
                scambio(k, (k + 1));
                sca = j;
            }
            else if (k->data->anno == (k + 1)->data->anno)
            {
                if (k->data->mese > (k + 1)->data->mese)
                {
                    scambio(k, (k + 1));
                    sca = j;
                }
                else if (k->data->mese == (k + 1)->data->mese)
                {
                    if (k->data->giorno > (k + 1)->data->giorno)
                    {
                        scambio(k, (k + 1));
                        sca = j;
                    }
                }
                j++;
            }
        }
        sup = sca;
    }
}

int main()
{
    FILE *fp;
    char *riga = (char *)malloc(DIM_RIGA * sizeof(char));
    char *nomefile = "ElencoLibri.csv";
    int n_righe = leggiRighe(nomefile);
    fp = fopen(nomefile, "r");

    if (fp == NULL)
    {
        printf("Errore nell'apertura del file.\n");
        return 1;
    }

    Libro *elenco = (Libro *)malloc(n_righe * sizeof(Libro));

    for (Libro *i = elenco; i < elenco + n_righe; i++)
    {
        i->data = (Data *)malloc(sizeof(Data));
        fgets(riga, DIM_RIGA, fp);
        char *campo = strtok(riga, ",");
        i->Autore = strdup(campo);
        campo = strtok(NULL, ",");
        i->Titolo = strdup(campo);
        campo = strtok(NULL, ",");
        i->data->giorno = atoi(campo);
        campo = strtok(NULL, ",");
        i->data->mese = atoi(campo);
        campo = strtok(NULL, ",");
        i->data->anno = atoi(campo);
    }

    fclose(fp);
    free(riga);
    stampaArc(elenco, n_righe);
    printf("\n");
    stampaAnnata(elenco, n_righe);
    printf("\n");
    printf("Stampa ordinata: \n");
    ordinaElenco(elenco, n_righe);
    for (Libro *i = elenco; i < elenco + n_righe; i++)
    {
        printf("TITOLO: %s AUTORE: %s DATA: %d/%d/%d\n", i->Titolo, i->Autore, i->data->giorno, i->data->mese, i->data->anno);
    }

    for (Libro *i = elenco; i < elenco + n_righe; i++)
    {
        free(i->data);
        free(i->Titolo);
        free(i->Autore);
    }
    free(elenco);

    return 0;
}