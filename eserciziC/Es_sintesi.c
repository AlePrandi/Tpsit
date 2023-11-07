#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define DIM 20000
#define LUNG_RIGA 200

typedef struct
{
    int giorno;
    int mese;
    int anno;
} Data;

typedef struct
{
    char *cognome;
    char *nome;
    Data nascita[DIM];
} Classe;

void scambio(Classe *a, Classe *b)
{
    Classe num;
    num = *a;
    *a = *b;
    *b = num;
}

int contaRighe()
{
    int n = 0;
    char *riga;
    FILE *fp = fopen("classe.csv", "r");
    while (fgets(riga, LUNG_RIGA, fp))
    {
        n++;
    }
    fclose(fp);
    return n;
    ;
}

void ordinaClasse(Classe alunno[], int cont)
{
    Classe *k;
    int sup, sca;
    sup = cont - 1;
    int j;
    while (sup > 0)
    {
        j = 0;
        sca = 0;
        for (k = alunno; k < alunno + sup; k++)
        {
            if (k->nascita->anno > (k + 1)->nascita->anno)
            {
                scambio(k, (k + 1));
                sca = j;
            }
            else if (k->nascita->anno == (k + 1)->nascita->anno)
            {
                if (k->nascita->mese > (k + 1)->nascita->mese)
                {
                    scambio(k, (k + 1));
                    sca = j;
                }
                else if (k->nascita->mese == (k + 1)->nascita->mese)
                {
                    if (k->nascita->giorno > (k + 1)->nascita->giorno)
                    {
                        scambio(k, (k + 1));
                        sca = j;
                    }
                }
            }
            j++;
        }
        sup = sca;
    }
}

int main()
{
    Classe *alunno;
    char nomefile[] = "classe.csv";
    char riga[LUNG_RIGA];
    FILE *fp;
    char *campo;
    int num = 0;
    int n_righe = contaRighe();
    alunno = (Classe *)malloc(n_righe * sizeof(Classe));
    Classe *cont = alunno;
    printf("Numero righe: %d\n", n_righe);
    fp = fopen(nomefile, "r");
    if (fp == NULL)
    {
        printf("Il file non esiste! \n");
        exit(1);
    }

    while (fgets(riga, LUNG_RIGA, fp))
    {
        campo = strtok(riga, ",");
        cont->cognome = strdup(campo);
        campo = strtok(NULL, ",");
        cont->nome = strdup(campo);
        campo = strtok(NULL, ",");
        cont->nascita->giorno = atoi(campo);
        campo = strtok(NULL, ",");
        cont->nascita->mese = atoi(campo);
        campo = strtok(NULL, ",");
        cont->nascita->anno = atoi(campo);
        cont++;
        num++;
    }

    fclose(fp);
    printf("Stampa ordinata: \n");
    ordinaClasse(alunno, num);
    for (Classe *k = alunno; k < alunno + num; k++)
    {
        printf("%s %s %d %d %d \n", k->cognome, k->nome, k->nascita->giorno, k->nascita->mese, k->nascita->anno);
    }
    return 0;
}