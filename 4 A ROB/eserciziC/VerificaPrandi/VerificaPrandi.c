#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define DIM_RIGA 200

typedef struct
{
    int euro;
    char *cognome;
    char *data;
} Alunno;

typedef struct
{
    char *cognome;
    int quota;
} Mio;

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

void cercaCognome(Alunno *elenco, int cont, char *cognome, Mio *mio, int maxSing)
{
    Alunno *k;
    for (k = elenco; k < elenco + cont; k++)
    {
        if (strcmp(k->cognome, cognome) == 0)
        {
            mio->quota = k->euro;
            mio->cognome = cognome;
            if (mio->quota < maxSing)
            {
                printf("L'alunno %s ha una quota di %d euro, deve ancora versare %d euro\n", mio->cognome, mio->quota, maxSing - mio->quota);
            }
            else
            {
                printf("L'alunno %s ha versatto tutta la quota\n", mio->cognome);
            }
        }
    }
}

void stampaTot(int versati, int totale)
{
    if (versati < totale)
    {
        printf("La quota versata e inferiore a %d euro, mancano %d euro\n",
               totale, totale - versati);
    }
    else
    {
        if (versati == totale)
        {
            printf("tutti gli alunni hanno versato la quota\n");
        }
    }
}

void Report(Alunno *elenco, int cont, int quotaTot)
{
    Alunno *k;
    for (k = elenco; k < elenco + cont; k++)
    {
        if (k->euro == quotaTot)
            printf("%s %d\n", k->cognome, k->euro);
        else
        {
            if (k->euro < quotaTot)
                printf("%s %d DA CONTROLLARE\n", k->cognome, k->euro);
        }
    }
}

int main()
{
    FILE *fp;
    char *riga = (char *)malloc(DIM_RIGA * sizeof(char));
    Mio *mio = (Mio *)malloc(1 * sizeof(Mio));
    char *nomefile = "4AROB_GITA.csv";
    int TotSing = 100; // max singola quota
    int n_righe = leggiRighe(nomefile);
    int Euro_max = leggiRighe(nomefile) * TotSing;
    int Euro_vers = 0;
    fp = fopen(nomefile, "r");

    if (fp == NULL)
    {
        printf("Errore nell'apertura del file.\n");
        return 1;
    }

    Alunno *elenco = (Alunno *)malloc(n_righe * sizeof(Alunno));

    for (Alunno *i = elenco; i < elenco + n_righe; i++)
    {
        fgets(riga, DIM_RIGA, fp);
        char *campo = strtok(riga, ";");
        i->data = strdup(campo);
        campo = strtok(NULL, ";");
        i->cognome = strdup(campo);
        campo = strtok(NULL, ";");
        i->euro = atoi(campo);
        Euro_vers += i->euro; // Aggiungo gli euro versati da ognuno
    }

    fclose(fp);
    free(riga);
    printf("\n"); // \n usato per spaziare nell'output
    stampaTot(Euro_vers, Euro_max);
    printf("\n"); // \n usato per spaziare nell'output
    cercaCognome(elenco, n_righe, "Prandi", mio, TotSing);
    printf("\n"); // \n usato per spaziare nell'output
    Report(elenco, n_righe, TotSing);
    printf("\n"); // \n usato per spaziare nell'output
    for (Alunno *i = elenco; i < elenco + n_righe; i++)
    {
        free(i->data);
        free(i->cognome);
    }

    free(elenco);

    return 0;
}