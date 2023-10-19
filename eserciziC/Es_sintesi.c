#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#define LUNG_MAX 150
#define DIM 20000
#define LUNG_RIGA 200

typedef struct
{
    int giorno;
    int mese;
    int anno;
}Data;


typedef struct {
    char* cognome;
    char* nome;
    Data nascita[DIM];
} Classe;

void scambio(Classe *a, Classe *b)
{
    Classe num;
    num = *a;
    *a = *b;
    *b = num;
}

/*
int leggiFile(Struttura film[]) {
    FILE*fp=fopen("listafilm.csv","r");
    int k=0;
    char riga[LUNG_RIGA];
    char *tok;
    while(fgets(riga,LUNG_RIGA,fp)!=NULL) {
        tok=strtok(riga,",");
        film[k].n=atoi(tok);
        tok=strtok(NULL,",");
        strcpy(film[k].titolo,tok);
        tok=strtok(NULL,",");
        strcpy(film[k].genere,tok);
        tok=strtok(NULL,",");
        film[k].anno_uscita=atoi(tok);
        tok=strtok(NULL,",");
        strcpy(film[k].disponibilita,tok);
        k++;
    }
    fclose(fp);
    return k;
}
*/
int contaRighe(char riga[],Classe Alunno[], int cont){
    int n=0;
    FILE* fp2=fopen("classe.csv","r");
    while(fgets(riga,LUNG_RIGA,fp2)){
        n++;
    }
    fclose(fp2);
    return n;;
}

void ordinaClasse(Classe alunno[], int cont, Data nascita[]){
    Classe *k;
    int sup, sca;
    sup = cont - 1;
    int j;
    while (sup > 0)
    {
        j=0;
        sca = 0;
        for (k = alunno; k < alunno+sup; k++)
        {
            if (k->nascita->anno > (k + 1)->nascita->anno)
            {
                scambio(k, (k + 1));
                sca = j;
            }else if(k->nascita->anno == (k + 1)->nascita->anno){
                if(k->nascita->mese > (k + 1)->nascita->mese){
                    scambio(k, (k + 1));
                    sca = j;
                }else if(k->nascita->mese == (k + 1)->nascita->mese){
                    if(k->nascita->giorno > (k + 1)->nascita->giorno){
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

int main() {
    Classe* alunno;
    Data* nascita;
    char fileName[]="classe.csv";
    char riga[LUNG_RIGA];
    FILE* fp;
    char* campo;
    int num=0;
    int scelta;
    int n_righe=contaRighe(riga,alunno,DIM);
    alunno=(Classe*)malloc(n_righe*sizeof(Classe));
    nascita=(Data*)malloc(n_righe*sizeof(Data));
    Classe *cont=alunno;
    printf("Numero righe: %d\n",n_righe);
    fp=fopen(fileName,"r");
    if(fp==NULL){
        printf("Il file non esiste! \n");
        exit(1);
    }
    while(fgets(riga,LUNG_RIGA,fp)){
        campo=strtok(riga,",");
        cont->cognome=strdup(campo);
        campo=strtok(NULL,",");
        cont->nome=strdup(campo);
        campo=strtok(NULL,",");
        cont->nascita->giorno=atoi(campo);
        campo=strtok(NULL,",");
        cont->nascita->mese=atoi(campo);
        campo=strtok(NULL,",");
        cont->nascita->anno=atoi(campo);
        cont++;
        num++;
    }
    fclose(fp);
    printf("Stampa ordinata: \n");
    ordinaClasse(alunno,num,nascita);
    for(Classe *k=alunno; k<alunno+num; k++) {
        printf("%s %s %d %d %d \n",k->cognome,k->nome,k->nascita->giorno,k->nascita->mese,k->nascita->anno);
    }
    return 0;
}